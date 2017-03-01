# coding=utf-8
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.common import utils_user


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化：param
		说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值

		工具函数：tool
		说明：
		内置的函数，如tool.randomStr() 获取一个随机的字符串
		##################################################################
		该方法内进行测试用例的编写
		'''
		pass
