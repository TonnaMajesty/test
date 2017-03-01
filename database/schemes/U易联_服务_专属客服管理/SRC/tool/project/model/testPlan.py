# coding:utf-8
'''
测试方案模型
'''
import os
from SRC import settings
from SRC.common import xmlHelper
import xml.etree.ElementTree as ET

from SRC.common.const import BROWSER_ID
from SRC.common.fileHelper import isNoneOrEmpty, isAbsolutePath, delsuffix, pathJoin, delFirstChar
from SRC.common.utils_user import randomStr
from SRC.tool.project.model.testCase import TestCase


class TestPlan():
	def __init__(self, name, path=''):
		self.path = path
		self.name = name
		self.hub = []  # 浏览器列表
		self.sceneList = []  # 场景列表
		self.acceptBrowser = BROWSER_ID
		self.testCaseDir = settings.TESTCASE['testCaseDir']  # 测试用例脚本目录
		self.readTestPlanXML()  # 分析xml文件

	def addTestCase(self, testCasePath, enabled, paramPath):
		displayParamPath = ''
		absoluteParamPath = ''
		if not isNoneOrEmpty(paramPath):
			if not isAbsolutePath(paramPath):
				paramPath = delFirstChar(paramPath, ['/', '\\'])

				displayParamPath = delsuffix(paramPath, '.xml')
				absoluteParamPath = pathJoin(settings.PARAMETERIZATION['dataDir'], paramPath)
				absoluteParamPath = delsuffix(absoluteParamPath, '.xml', False)

		fileName = ''  # 文件名称
		disPlayPath = ''  # 显示路径
		absolutePath = ''  # 绝对路径
		if not isNoneOrEmpty(testCasePath):
			testCaseDir = settings.TESTCASE['testCaseDir']
			testCasePath = delFirstChar(testCasePath, ['/', '\\'])

			if not testCasePath.startswith(testCaseDir):
				testCasePath = testCaseDir + testCasePath

			absolutePath = pathJoin(settings.SCRIPT_DIR, testCasePath)
			absolutePath = delsuffix(absolutePath, '.py', False)
			fileName = os.path.basename(absolutePath).split('.')[0]
			disPlayPath = absolutePath.split(testCaseDir)[1]
			disPlayPath = delsuffix(disPlayPath, '.py')

		enabled = True if enabled is None or enabled.lower().strip() == 'true' else False

		def testCaseFunc():
			return TestCase(absolutePath, absoluteParamPath)

		model = {'name': fileName,
				 'obj': testCaseFunc,
				 'path': disPlayPath,
				 'paramPath': displayParamPath,
				 'absolutePath': absolutePath,
				 'absoluteParamPath': absoluteParamPath,
				 'enabled': enabled,
				 'unique': randomStr(10, True, True, True)
				 }
		return model

	def addHub(self, browser, enabled, remoteUrl='http://0.0.0.0:5555/wd/hub'):
		if isNoneOrEmpty(browser):
			browser = BROWSER_ID[0]
		enabled = True if enabled is None or enabled.lower().strip() == 'true' else False
		remoteUrl = 'http://0.0.0.0:4444/wd/hub' if remoteUrl is None else remoteUrl
		model = {'browser': browser, 'enabled': enabled, 'remoteUrl': remoteUrl}
		return model

	def removeHub(self, browser):
		for item in self.hub:
			if item['browser'] == browser:
				self.hub.remove(item)

	def readTestPlanXML(self):
		'''
		加载测试方案配置文件
		:return:
		'''
		try:
			tree = ET.parse(self.path)  # 打开xml文档
			root = tree.getroot()  # 获得root节点
			for child in root:
				if child.tag == settings.XML_TAG['testPlan']['connection']:
					for hub in child:
						model = self.addHub(hub.get(settings.XML_TAG['testPlan']['browser']),
											hub.get(settings.XML_TAG['testPlan']['enabled']),
											hub.text)
						self.hub.append(model)
				elif child.tag == settings.XML_TAG['testPlan']['scene']:
					testCaseList = []
					for tc in child:
						testCase = self.addTestCase(tc.text,
													tc.get(settings.XML_TAG['testPlan']['enabled']),
													tc.get(settings.XML_TAG['testPlan']['paramPath']))
						testCaseList.append(testCase)
					self.sceneList.append(testCaseList)

		except Exception as e:
			print("[Error-TestPlan.readTestPlanXML]:读取测试方案错误 %s %s" % (self.path, str(e)))

	def writeTestPlanToXML(self):
		result = True
		try:
			tree = xmlHelper.read_xml(self.path)
			self.updateHub(tree)  # 写入hub数据
			self.updateTestCase(tree)  # 写入TestCase数据

			xmlHelper.indent(tree.getroot())
			xmlHelper.write_xml(tree, self.path)
		except Exception as e:
			print('[Error-TestPlan.writeTestPlanToXML]: %s' % (str(e)))
			result = False
		return result

	def updateHub(self, tree):
		connectionNode = tree.find(settings.XML_TAG['testPlan']['connection'])
		for model in self.hub:
			isUpdate = False
			for node in connectionNode:
				browserName = node.get(settings.XML_TAG['testPlan']['browser'])
				if browserName and browserName.lower().strip() == model['browser'].lower().strip():
					node.set(settings.XML_TAG['testPlan']['enabled'], str(model['enabled']))
					node.text = model['remoteUrl']
					isUpdate = True
					break
			if not isUpdate:
				newNode = xmlHelper.create_node('hub',
												{settings.XML_TAG['testPlan']['browser']: model['browser'],
												 settings.XML_TAG['testPlan']['enabled']: str(model['enabled'])
												 },
												model['remoteUrl'])
				xmlHelper.add_child_node([connectionNode], newNode)

	def updateTestCase(self, tree):
		rootNode = tree.getroot()
		xmlHelper.del_node_by_tagkeyvalue([rootNode], settings.XML_TAG['testPlan']['scene'])  # 删除掉所有scene节点

		# 添加节点
		for testCaseList in self.sceneList:
			newSceneNode = xmlHelper.create_node(settings.XML_TAG['testPlan']['scene'],
												 {'description': '脚本执行顺序为子标签排列顺序'}, '')
			for model in testCaseList:
				newNode = xmlHelper.create_node(settings.XML_TAG['testPlan']['testCase'],
												{settings.XML_TAG['testPlan']['paramPath']: model['paramPath'],
												 settings.XML_TAG['testPlan']['enabled']: str(model['enabled'])
												 },
												model['path'])
				xmlHelper.add_child_node([newSceneNode], newNode)
			xmlHelper.add_child_node([rootNode], newSceneNode)
