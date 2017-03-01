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
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(7) > p").click()
		time.sleep(3)

		#导出
		driver.find_element_by_id("exportAction").click()
		driver.switch_to_alert().accept()
		#查询
		js='$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_class_name("ok").click()
		driver.find_element_by_id("query_search").click()






		

