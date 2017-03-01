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

		driver.find_element_by_css_selector("#page_module > li:nth-child(5)").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(3) > p").click()
		time.sleep(5)

		# 查询
		xxzt = driver.find_element_by_id("query_iMsgStatus")
		xxzt.find_element_by_css_selector("#query_iMsgStatus > option:nth-child(2)").click()
		driver.find_element_by_id("query_search").click()
		time.sleep(2)

		xxzt1 = driver.find_element_by_id("query_iMsgStatus")
		xxzt1.find_element_by_css_selector("#query_iMsgStatus > option:nth-child(3)").click()
		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a > i").click()

		driver.find_element_by_xpath('//a[@href="/Page/User/MessageList"]').click()
		time.sleep(5)