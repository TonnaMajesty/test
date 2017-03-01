# coding:utf-8
import os

from SRC import settings
from SRC.common.fileHelper import pathJoin, isAbsolutePath
from SRC.tool.project.model.testPlan import TestPlan

'''
测试方案配置工厂
'''


class ConfigFactory():
	def __init__(self, projectPath, configXmlPath=None):
		self.testPlanList = []  # 测试方案列表
		# self.initSettings(projectPath)#废弃
		self.testCaseDir = pathJoin(projectPath,settings.TESTCASE['testCaseDir'])
		self.templateList = self.getTemplatePathList()

	# 废弃，在__init__中已经初始化
	# def initSettings(self, projectPath):
	# 	'''
	# 	项目配置文件
	# 	'''
	# 	settings.BASE_DIR = projectPath  # 项目目录
	#
	# 	settings.TESTCASE['xmlDir'] = self.getAbsoluteDir(settings.TESTCASE['xmlDir'])
	# 	settings.PARAMETERIZATION['dataDir'] = self.getAbsoluteDir(settings.PARAMETERIZATION['dataDir'])
	# 	settings.REPORT['logDir'] = self.getAbsoluteDir(settings.REPORT['logDir'])

	def getTemplatePathList(self):
		list = []
		for fileName in settings.TEMPLATES['templateDir']:
			list.append(pathJoin(settings.SRC_DIR, settings.TEMPLATES['storeTemplateDir'], fileName))
		return list

	def loadAllTestPlans(self):
		try:
			if os.path.isdir(settings.TESTCASE['xmlDir']):
				self.diguiReadDir(settings.TESTCASE['xmlDir'])
			else:
				print('loadAllTestPlans->目录错误:' + settings.TESTCASE['xmlDir'])
		except Exception as e:
			print('loadAllTestPlans:' + str(e))

	def diguiReadDir(self, dir):
		files = os.listdir(dir)
		for file in files:
			path = pathJoin(dir, file)
			if os.path.isfile(path):
				self.addTestPlan(path, file)
			elif os.path.isdir(path):
				self.diguiReadDir(path)

	def addTestPlan(self, path, file):
		if file.split('.')[-1] == 'xml':
			fileName = file.split('.')[0]

			def func():
				return TestPlan(fileName, path)

			model = {'name': fileName, 'path': path, 'objFunc': func}
			res = [x for x in self.testPlanList if x['path'] == path]
			if res:
				self.removeTestPlan(res)
			self.testPlanList.append(model)

	def removeTestPlan(self, mode):
		if isinstance(mode, list):
			for m in mode:
				self.testPlanList.remove(m)
		else:
			self.testPlanList.remove(mode)

	#废弃
	# def getAbsoluteDir(self, subDir):
	# 	if not isAbsolutePath(subDir):
	# 		subDir = pathJoin(settings.BASE_DIR, subDir)
	# 	return subDir
