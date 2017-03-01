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
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(2) > p").click()
		time.sleep(3)

		#编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1)").click()
		driver.find_element_by_id("btnKeyAuto").click()
		fwy=driver.find_element_by_id("iSSID")
		fwy.find_element_by_css_selector("#iSSID > option:nth-child(2)").click()
		driver.find_element_by_id("cFunctionName").clear()
		driver.find_element_by_id("cFunctionName").send_keys("统计表")
		gnlx=driver.find_element_by_id("iFunctionType")
		gnlx.find_element_by_css_selector("#iFunctionType > option:nth-child(2)").click()
		driver.find_element_by_id("saveAction").click()
		#返回
		driver.find_element_by_xpath('//a[@href="/Page/MP/ServiceFunctionList"]').click()

		#删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		#新增
		driver.find_element_by_id("exportAction").click()
		driver.find_element_by_id("btnKeyAuto").click()
		fwy = driver.find_element_by_id("iSSID")
		fwy.find_element_by_css_selector("#iSSID > option:nth-child(2)").click()
		driver.find_element_by_id("cFunctionName").clear()
		driver.find_element_by_id("cFunctionName").send_keys("利润统计表")
		gnlx = driver.find_element_by_id("iFunctionType")
		gnlx.find_element_by_css_selector("#iFunctionType > option:nth-child(2)").click()
		driver.find_element_by_id("cFunctionAddress").send_keys("www.baidu.com")
		driver.find_element_by_id("saveAction").click()
		# 返回
		driver.find_element_by_xpath('//a[@href="/Page/MP/ServiceFunctionList"]').click()
		#查询
		fwlx1=driver.find_element_by_id("query_iSSID")
		fwlx1.find_element_by_css_selector("#query_iSSID > option:nth-child(2)").click()
		driver.find_element_by_id("query_cFunctionName").send_keys("利润统计表")
		gnlx1 = driver.find_element_by_id("query_iFunctionType")
		gnlx1.find_element_by_css_selector("#query_iFunctionType > option:nth-child(2)").click()
		driver.find_element_by_id("query_search").click()



