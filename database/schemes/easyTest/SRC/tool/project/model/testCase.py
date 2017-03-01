# coding:utf-8
'''
测试用例模型
'''
from SRC.tool.project.model.testParam import TestParam


class TestCase():
	def __init__(self,path='',param=None):
		self.path=path
		self.testParamPath=param
		self.paramObj=None

	def setTestParam(self,paramPath=None):
		if paramPath:
			self.paramObj = TestParam(self.testParamPath)
			self.testParamPath=paramPath
		else:
			self.paramObj=None
			self.testParamPath = None

	def getTestParamObj(self):
		return self.paramObj