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

		driver.find_element_by_css_selector("#page_module > li:nth-child(5) > a").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div:nth-child(1)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(2) > p").click()

		#查询
		driver.find_element_by_id("query_cCode").send_keys("1")
		driver.find_element_by_id("query_cName").send_keys("1")
		driver.find_element_by_id("query_cRealName").send_keys("1")
		driver.find_element_by_id("query_cPhone").send_keys("1")
		driver.find_element_by_id("query_search").click()
		#导出
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("exportAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()



