# coding=utf-8
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool  = utils

		driver.get('http://ylb.yonyouup.com/')
		driver.find_element_by_class_name("reg").click()
		title = driver.title
		self.assertEqual(title, 'U易联', '跳转异常')
		driver.find_element_by_id("cUserName").send_keys("testc")
		driver.find_element_by_id("cPassword").send_keys("123456")
		driver.find_element_by_id("cVerify").send_keys("yilian")
		driver.find_element_by_id("login_yes").click()
		title1 = driver.title
		self.assertEqual(title1, '欢迎使用', '跳转异常')

