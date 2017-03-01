# coding=utf-8
import importlib
# import unittest
import os
import xml.etree.ElementTree as ET
from time import time, sleep
from unittest import TestSuite

from SRC import settings
from SRC.common.const import RunModel, RunResult, RunStatus
from SRC.common.exceptions import ReadParamFileException, createDriverException
from SRC.common.fileHelper import isNoneOrEmpty
from SRC.common.loga import putSystemLog, manageLogRecord, getRecordTxt
from SRC.unittest.case import TestCase
from SRC.unittest.runnerExt import TextTestRunner


class Scene():
	'''
	场景类
	'''

	def __init__(self, webDriverFunc, testScene, logger, screenShotDir, index):
		self._driverFunc = webDriverFunc  # 浏览器驱动调用方法
		self.testCaseList = testScene.testCaseList
		self.logger = logger  # 日志对象
		self.logger.scriptId = ''  # 临时脚本id
		self.screenShotDir = screenShotDir  # 截图目录
		self.index = index  # 场景编号
		# self.sceneId = self.index + 1 if testScene.sceneId is None else testScene.sceneId  # 设置场景id
		self.sceneId = self.index + 1

	def run(self):
		logger = self.logger  # 日志对象
		runTime = settings.PARAMETERIZATION['runTime']  # 单个场景运行次数
		runModel = settings.RUNMODEL  # 运行模式

		manageLogRecord(self.sceneId, operator='create')  # 创建统计记录
		self.testClassList = self.importTestCase(self.testCaseList)  # 引入测试用例
		if len(self.testClassList) == 0:
			putSystemLog('[ERROR-1009]:场景%d中不包含任何测试用例' % self.sceneId, logger, False, RunStatus.RUNNING,
						 RunResult.ERROR, True)
			return

		if runModel == RunModel.TESTING:
			putSystemLog('启动测试模式下，不会真正运行测试用例的脚本！', logger)

		sceneDes = '场景<%d>开始.' % (self.sceneId) if runTime == 1 else '场景<%d>开始.该场景共运行%d次' % (self.sceneId, runTime)
		putSystemLog(sceneDes, logger)
		sTime = time()
		driver =None
		for x in range(runTime):
			try:
				if runTime != 1:
					putSystemLog('第%d次运行：' % (x + 1), logger)
				driver = self.getDriverObj()  # 获取一个浏览器驱动
				putSystemLog('%s浏览器启动成功.' % (driver.name), logger)
				putSystemLog('开始加载脚本...', logger)
				suite = self.suiteFactory(x, driver)  # 创建并配置测试单元套件
				putSystemLog('脚本加载完成...', logger)
				if runModel != RunModel.TESTING and len(suite._tests) > 0:
					TextTestRunner().run(suite)
			except createDriverException as e:
				putSystemLog(str(e), logger, True, RunStatus.RUNNING, RunResult.ERROR, True, '异常')
			except Exception as e:
				putSystemLog('[ERROR-1012]:测试套件运行失败引发的异常.%s' % e, logger, True, RunStatus.RUNNING, RunResult.ERROR,
							 True, '异常')
			finally:
				self.quitDriver(driver)
		eTime = time()
		putSystemLog('场景<%d>结束.用时:%.3fs.' % (self.sceneId, eTime - sTime), logger)
		putSystemLog(getRecordTxt(manageLogRecord(self.sceneId, operator='get')), logger)
		putSystemLog('-' * 40, logger)

	def quitDriver(self, driver):
		try:
			driver.quit()
		except:
			pass

	def getDriverObj(self):
		createDriverFailed = settings.DRIVER['createDriverFailed']
		driver = None
		for n in range(createDriverFailed):
			try:
				driver = self._driverFunc()  # 创建浏览器驱动
				driver.logger = self.logger  # 为浏览器驱动配置日志对象
				driver.screenShotDir = self.screenShotDir  # 为浏览器驱动配置截图目录
				driver.sceneId = self.sceneId  # 为浏览器驱动配置场景ID
				if settings.DRIVER['maximizeWindow']:
					driver.maximize_window()
				break
			except Exception as e:
				# putSystemLog('[ERROR-1008]:创建浏览器驱动对象失败引发的异常.%s' % e, self.logger, True, RunStatus.RUNNING, RunResult.ERROR,
				# 			 True, '异常')
				self.quitDriver(driver)
				if n == createDriverFailed - 1:
					raise createDriverException(e)
				else:
					sleep(1)
		return driver

	def suiteFactory(self, x, driver):
		suite = TestSuite()  # 创建测试单元套件
		for index, testCaseClass in enumerate(self.testClassList):
			try:
				paramsList = None  # 参数列表
				paramPath = testCaseClass['paramPath']  # 获取参数文件地址
				if paramPath and os.path.exists(paramPath):
					paramsList = self.readParamXml(paramPath, testCaseClass['className'], x)
			except ReadParamFileException as e:
				putSystemLog(e, self.logger, True, RunStatus.RUNNING, e.runResult, True, '参数文件异常')
			except Exception as e:
				err = '读取参数化文件时发生异常.%s.%s' % (testCaseClass['scriptPath'], e)
				putSystemLog(err, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True, '异常')

			try:
				driver.scriptId = testCaseClass['scriptId'] if testCaseClass['scriptId'] else ''  # 添加临时脚本id
				suite.addTest(testCaseClass['testClass'](driver, paramsList))  # 创建测试用例，并添加到套件中

				scriptName = testCaseClass['scriptPath'].split('/')[-1]
				putSystemLog('脚本<%d>：%s 加载成功.脚本路径：%s' % (index + 1, scriptName, testCaseClass['scriptPath']),
							 self.logger)
				if paramsList is not None:
					putSystemLog('脚本<%d>参数列表：' % (index + 1), self.logger)
					for k, v in paramsList.items():
						putSystemLog("%s:%s" % (k, v), self.logger)

			except Exception as e:
				err = '[ERROR-1011]:向测试单元套件添加测试用例对象时引发的异常.%s.%s' % (testCaseClass['scriptPath'], e)
				putSystemLog(err, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True, '异常')
		return suite

	def importTestCase(self, testCaseList):
		'''
		动态添加测试用例的引用
		:param testCaseList:
		:return:
		'''
		classList = []
		testCaseDir = settings.TESTCASE['testCaseDir']
		for dict in testCaseList:
			try:
				p = dict['testCase']
				p = p[1:] if p[:1] == '/' else p
				if not p.startswith(testCaseDir):
					p = testCaseDir + p
				path = p
				path = path.replace('/', '.')
				path = path[1:] if path[:1] == '.' else path
				model_module = importlib.import_module(path)  # 引入模块
			except Exception as e:
				err = '[ERROR-1004]:引入测试方案模块失败引发的异常.%s.%s' % (dict['testCase'], e)
				putSystemLog(err, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True, '异常')
				continue
			for attr_name in dir(model_module):
				attr = getattr(model_module, attr_name)
				try:
					if issubclass(attr, TestCase) and attr.__name__ != TestCase.__name__:
						classList.append(
							{'paramPath': dict['paramPath'], 'testClass': attr, 'className': attr.__name__,
							 'scriptPath': '%s' % (p), 'scriptId': dict['scriptId']})
				except Exception:
					continue
		return classList

	def readParamXml(self, paramPath, className='EasyCase', time=0):
		# 读取参数xml文件的数据
		params = {}
		try:
			tree = ET.parse(paramPath)  # 打开xml文档
			root = tree.getroot()  # 获得root节点
			count = len(root.findall('testCase'))
			num = time % count  # 读取参数的次数
			testClassElement = root[num].find("testClass[@name='%s']" % (className))
			if testClassElement is not None:
				for param in testClassElement:
					id = param.get(settings.XML_TAG['testParam']['id'])
					if not isNoneOrEmpty(id):
						value = '' if param.text is None else param.text
						params[id] = value
		except ZeroDivisionError as e:
			raise ReadParamFileException(e, '请检查参数化文件是否正确', RunResult.WARNING)
		except Exception as e:
			raise ReadParamFileException(e)
		return params
