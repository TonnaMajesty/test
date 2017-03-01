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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div.typ > a:nth-child(3) > p").click()
		time.sleep(3)

		# 类型
		lx = driver.find_element_by_id("query_iStatus")
		lx.find_element_by_css_selector("#query_iStatus > option:nth-child(4)").click()
		time.sleep(1)
		# 防伪码
		driver.find_element_by_id("query_cSecurityCode").send_keys("123")
		time.sleep(1)
		# 存货编码
		driver.find_element_by_id("query_cInventoryCode").send_keys("123")
		time.sleep(1)
		# 存货名称
		driver.find_element_by_id("query_cInventoryName").send_keys("123")
		time.sleep(1)
		# 验证时间
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(2) > div:nth-child(4) > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		# 验证次数
		driver.find_element_by_id("query_iInspecCount_from").send_keys("1")
		driver.find_element_by_id("query_iInspecCount_to").send_keys("2")
		time.sleep(1)
		# 保存
		driver.find_element_by_id("query_search").click()
		time.sleep(5)