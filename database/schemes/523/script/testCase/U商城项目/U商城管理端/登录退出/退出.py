# coding=utf-8
import time

from selenium.webdriver import ActionChains

from SRC.common import utils_user
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
		tool = utils_user

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_css_selector('.userMsgDiv').show()
		driver.find_element_by_link_text(u"退出").click()
		driver.find_element_by_link_text(u"退出").click()





