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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div.typ > a:nth-child(2) > p").click()
		time.sleep(3)

		# 下载模板
		# driver.find_element_by_id("download").click()
		# time.sleep(3)
		# 删除
		driver.find_element_by_class_name("icon-delete").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		# 查询
		driver.find_element_by_id("query_cSecurityCode").send_keys("0000000000000001")
		time.sleep(1)
		driver.find_element_by_id("query_cInventoryName").send_keys("001")
		time.sleep(1)
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(5) > span","findAssert").text
		self.assertEqual(search, "0000000000000001", "查询成功")