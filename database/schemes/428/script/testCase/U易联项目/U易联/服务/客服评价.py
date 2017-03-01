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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(4) > p").click()
		time.sleep(5)

		# 查询
		kfgh = driver.find_element_by_id("query_cKfAccount")
		kfgh.find_element_by_css_selector("#query_cKfAccount > option:nth-child(2)").click()
		driver.find_element_by_id("query_cKfNick").send_keys("zzt")
		time.sleep(1)
		driver.find_element_by_id("query_search").click()
		time.sleep(5)
		# 查询验证
		#search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		#self.assertEqual(search, "zzt", "查询成功")