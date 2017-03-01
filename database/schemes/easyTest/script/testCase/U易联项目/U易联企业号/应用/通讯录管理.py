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
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(4) > p").click()
		time.sleep(3)

		#新增
		driver.find_element_by_css_selector("#toolbar_search > div > div > span").click()
		driver.find_element_by_id("addpsn").click()
		#查询
		driver.find_element_by_id("inputSearch").send_keys("1")
		driver.find_element_by_css_selector("#div_search > div > div.typeahead-result > ul > li:nth-child(2) > a").click()

		

