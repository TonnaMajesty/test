# coding=utf-8
import time

from selenium.webdriver import ActionChains

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

		driver.find_element_by_css_selector("#page_module > li:nth-child(4)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(5) > p").click()
		time.sleep(3)

		#新增
		fwy=driver.find_element_by_id("iSSID")
		fwy.find_element_by_css_selector("#iSSID > option:nth-child(2)").click()
		driver.find_element_by_css_selector("#hometemplate > div > img").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()



		

