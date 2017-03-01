# coding:utf-8
import json
import os
import sys
from collections import namedtuple
from selenium.webdriver import DesiredCapabilities
import xml.etree.ElementTree as ET
from threading import Thread
from SRC import settings
from SRC.common.const import Agent, RunType, RunModel, BROWSER_ID, RunStatus, RunResult
from SRC.common.fileHelper import delFirstChar, pathJoin, isAbsolutePath, delsuffix, isNoneOrEmpty, astrcmp
from SRC.common.loga import createLog, putSystemLog, getRecordTxt, manageLogRecord
from SRC.common.loggernull import LoggerNull
from SRC.common.utils import createDir, getLogName
from SRC.unittest.scene import Scene
from SRC.webdriver.browser import Browser
from collections import OrderedDict

TestScene = namedtuple('testScene', ['sceneId', 'testCaseList'])


class Main():
	'''
	该类为easyTest项目的管理类
	'''

	def __init__(self, xml=None, model='NORMAL'):
		self.xmlPath = xml.replace('\\', '/').strip() if xml else None  # 接收的测试方案路径
		self.model = model  # 运行模式，分为normal正常 test 测试 注：测试模式下 不运行用例，只执行流程
		self.hubDict = {}  # 远程主机的集合
		self.testPlan = []  # 测试方案列表
		self.sceneList = []  # 场景列表

		self.uniqueCode = settings.UNIQUECODE  # 唯一标识

	def run(self):
		if isNoneOrEmpty(self.xmlPath):  # 当没有传入测试方案的时候，从控制台获取
			self.setTestPlanPathFromUser()
		testPlanName = self.xmlPath #测试方案文件名称
		putSystemLog('程序启动.%s' % testPlanName, None, False, '', '', True)
		try:
			self.setRunModel()  # 设置运行模式
			self.updateSettings(self.model)  # 根据运行模式更新settings设置
			self.loadTestPlanXML()  # 加载测试方案配置文件
			self.start()  # 启动
		except Exception as e:
			pass
		finally:
			putSystemLog('程序结束.%s\n' % testPlanName, None, False, '', '', True)

	def setTestPlanPathFromUser(self):
		'''
		控制台根据用户输入设置测试方案路径
		:return:
		'''
		filesList = []
		index = 0
		try:
			for dirPath, dirNames, fileNames in os.walk(settings.TESTCASE['xmlDir']):
				for filename in fileNames:
					if filename[-4:] == '.xml':
						filesList.append(
							(index + 1, filename, dirPath.replace('\\', '/').split(settings.SCRIPT_DIR)[1]))
						index += 1
			if len(filesList) == 0:
				print('%s目录下没有测试方案' % (settings.TESTCASE['xmlDir']))
				return
			print('%-3s %s' % ('编号', '测试方案'))
			for file in filesList:
				print('%-5s %s' % (file[0], pathJoin(file[2], file[1])))
			while True:
				result = input('请选择测试方案编号:')
				if result.isdigit():
					result = int(result) - 1
					if result >= 0 and result < len(filesList):
						self.xmlPath = filesList[int(result)][1]
						print('即将运行测试方案：%s' % (self.xmlPath))
						break
					else:
						print('输入错误')
				else:
					print('输入错误')
		except Exception as e:
			print(e)
			raise

	def setRunModel(self):
		if self.uniqueCode:  # 如果有传参，那么是实行线上模式
			self.model = RunModel.ONLINE

	def updateSettings(self, model):
		if model == RunModel.TESTING:  # 测试模式
			settings.RUNMODEL = model
			settings.TESTCASE['runType'] = RunType.BROWSER

		if model == RunModel.ONLINE:  # 在线模式
			settings.RUNMODEL = model
			try:
				decodeJson = json.loads(self.uniqueCode.replace("'", "\""))
				hubDict = {}
				for browser in decodeJson['browsers'].keys():
					br = browser.lower()[:2]
					if br in BROWSER_ID:
						hubDict[br] = decodeJson['browsers'][browser]
						break
				self.hubDict = hubDict
				settings.SERVER['requestURL'] = decodeJson['requestURL']
			except Exception as e:
				putSystemLog('[ERROR-1002]:解析外部传入的JSON字符串引发的异常.%s' % e, None, False, '', '', True)
				raise

			settings.TESTCASE['runType'] = RunType.REMOTE
			settings.REPORT['isWriteLog'] = False

		if model == RunModel.NORMAL:  # 正常模式
			settings.RUNMODEL = model

		# 修正
		if isNoneOrEmpty(settings.SERVER['requestURL']):  # 如果服务器url不正确，就不发送数据
			settings.SERVER['isRequest'] = False

	def loadTestPlanXML(self):
		'''
		加载测试用例配置文件
		:return:
		'''
		try:
			if not isAbsolutePath(self.xmlPath):
				self.xmlPath = pathJoin(settings.TESTCASE['xmlDir'], self.xmlPath)

			tree = ET.parse(self.xmlPath)  # 打开xml文档
			root = tree.getroot()  # 获得root节点
			for child in root:
				if child.tag == settings.XML_TAG['testPlan']['connection']:
					if len(self.hubDict) == 0:
						self.hubDict = self.getHubDict(child)
				elif child.tag == settings.XML_TAG['testPlan']['scene']:
					sceneId = child.get(settings.XML_TAG['testPlan']['sceneid'])  # sceneId
					settings.SCENEID = sceneId
					testCaseList = self.getTestList(child)  # 读取一个场景中的所有测试用例
					testScene = TestScene(sceneId, testCaseList)
					self.testPlan.append(testScene)  # 将测试用例列表添加到测试方案中
		except Exception as e:
			putSystemLog('[ERROR-1001]:读取测试方案配置文件引发的异常.%s' % (e), None, True, RunStatus.END, RunResult.ERROR, True,
						 '异常')
			raise

	def start(self):
		# 配置场景
		try:
			runType = settings.TESTCASE['runType']
			if astrcmp(runType, RunType.REMOTE):
				self.__onLine()
			elif astrcmp(runType, RunType.BROWSER):
				self.__offLine()
		except Exception as e:
			putSystemLog('[ERROR-1003]:配置场景引发的异常.%s' % (e), None, True, RunStatus.END, RunResult.ERROR, True, '异常')
			raise

	def getHubDict(self, child):
		hubDict = {}
		for hub in child:
			if hub.tag == settings.XML_TAG['testPlan']['hub']:
				enabled = hub.get(settings.XML_TAG['testPlan']['enabled'])
				if enabled is None or enabled.lower().strip() == 'true':
					browser = hub.get(settings.XML_TAG['testPlan']['browser'])
					if not isNoneOrEmpty(browser):
						remotePath = hub.text.strip() if hub.text is not None else ''
						hubDict[browser.lower().strip()] = remotePath
		return hubDict

	def getTestList(self, child):
		testCaseList = []
		for tc in child:
			if tc.tag == settings.XML_TAG['testPlan']['testCase']:
				enabled = tc.get(settings.XML_TAG['testPlan']['enabled'])
				if enabled is None or enabled.lower().strip() == 'true':
					testCasePath = tc.text  # 测试用例路径
					if not isNoneOrEmpty(testCasePath):
						testCasePath = testCasePath.strip()
						testCasePath = delsuffix(testCasePath, '.py')  # 去掉后缀

						paramPath = tc.get(settings.XML_TAG['testPlan']['paramPath'])
						if not isNoneOrEmpty(paramPath):
							paramPath = paramPath.strip()
							paramPath = delsuffix(paramPath, '.xml', False)  # 增加后缀
							if not isAbsolutePath(paramPath):
								paramPath = delFirstChar(paramPath, ['/', '\\'])
								paramPath = os.path.join(settings.PARAMETERIZATION['dataDir'], paramPath).replace('\\',
																												  '/')
						else:
							paramPath = None

						scriptId = tc.get(settings.XML_TAG['testPlan']['scriptId'])  # 脚本id
						testCaseList.append({'paramPath': paramPath, 'testCase': testCasePath, 'scriptId': scriptId})
		return testCaseList

	def __offLine(self):
		# 线下模式
		for br, host in self.hubDict.items():
			br = self.__switchBrowser(br)
			driver = Browser(br).driver()
			self.__runTestPlan(driver)

	def __onLine(self):
		# 线上模式
		threads = []
		files = range(len(self.hubDict))
		# 创建线程
		for browser, host in self.hubDict.items():
			browser = self.__switchBrowser(browser)
			t = Thread(target=self.__threadStart, args=(browser, host))
			threads.append(t)

		# 启动线程
		for i in files:
			threads[i].start()
		for i in files:
			threads[i].join()

	def __threadStart(self, browser, host):
		desiredCapabilities = self.__setDesiredCapabilities(browser)
		driver = Browser(Agent.REMOTE, command_executor=host,
						 desired_capabilities=desiredCapabilities).driver()
		self.__runTestPlan(driver)

	def __runTestPlan(self, driver):
		logger = self.createLoggerObj()  # 创建该场景日志对象
		screenShotDir = self.createScreenShotDir()  # 创建截图目录
		result = RunResult.PASS
		err = ''
		putSystemLog('Start.', logger, True, RunStatus.START, result, True, '开始')
		try:
			for index, sc in enumerate(self.testPlan):
				Scene(driver, sc, logger, screenShotDir, index).run()
		except Exception as e:
			result = RunResult.ERROR
			err = e
		finally:
			putSystemLog('End.%s' % (err), logger, True, RunStatus.END, result, True, '结束')
			putSystemLog(getRecordTxt(manageLogRecord(operator='get'), type='all'), logger)  # 写入统计结果

	def __switchBrowser(self, key):
		browser = Agent.FIREFOX
		try:
			if key[:2] == BROWSER_ID[0]:
				browser = Agent.FIREFOX
			elif key[:2] == BROWSER_ID[1]:
				browser = Agent.CHROME
			elif key[:2] == BROWSER_ID[2]:
				browser = Agent.IE
		except:
			pass
		return browser

	def __setDesiredCapabilities(self, browser):
		if browser == Agent.CHROME:
			desiredCapabilities = DesiredCapabilities.CHROME.copy()
			chrome_options = {}
			chrome_options['args'] = ['--disable-popup-blocking']
			chrome_options['excludeSwitches'] = ['ignore-certificate-errors']
			desiredCapabilities['chromeOptions'] = chrome_options
		elif browser == Agent.IE:
			desiredCapabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
		else:
			desiredCapabilities = DesiredCapabilities.FIREFOX.copy()

		return desiredCapabilities

	def createLoggerObj(self):
		if settings.REPORT['isWriteLog']:
			# 创建日志对象
			logDir = createDir(settings.REPORT['logDir'])  # 创建日志目录
			logPath = os.path.join(logDir, getLogName())  # 日志绝对路径
			logger = createLog(logPath)  # 日志对象
		else:
			logger = LoggerNull()  # 定义一个空日志对象
		return logger

	def createScreenShotDir(self):
		screenShotDir = None
		if settings.REPORT['isScreenShot']:
			screenShotDir = createDir(settings.REPORT['screenShotDir'])  # 创建截图目录
		return screenShotDir
