# coding=utf-8
from time import sleep, time

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils

class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user


		# js = '$(".xiaTui").show()'
		# driver.execute_script(js)
		driver.find_element_by_class_name('xiaTui').show()
		driver.find_element_by_css_selector("body > div.col01 > div.col01_header01 > div > div.userHeader > div.xiaTui > ul > li:nth-child(3) > a").click()
		sleep(3)
		#js1 = '$(".js-logout").click()'
		#driver.execute_script(js1)
		i=1

