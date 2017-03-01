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

		#编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1)").click()
		driver.find_element_by_id("btnKeyAuto").click()
		driver.find_element_by_id("cServerName").clear()
		driver.find_element_by_id("cServerName").send_keys("uuu")
		fwlylx=driver.find_element_by_id("cServerSourceType")
		fwlylx.find_element_by_css_selector("#cServerSourceType > option:nth-child(4)").click()
		#driver.find_element_by_id("cAccount").clear()
		#driver.find_element_by_id("cAccount").send_keys("001")
		#scms=driver.find_element_by_id("cAccountType")
		#scms.find_element_by_css_selector("#cAccountType > option:nth-child(2)").click()
		driver.find_element_by_id("cServerUrl").clear()
		driver.find_element_by_id("cServerUrl").send_keys("http://10.10.10.1/WXQYH")
		driver.find_element_by_id("cDes").send_keys("123")
		driver.find_element_by_id("saveAction").click()
		#返回
		driver.find_element_by_xpath('//a[@href="/Page/MP/QyServiceSourceList"]').click()

		#删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		#新增
		driver.find_element_by_id("exportAction").click()

		driver.find_element_by_id("btnKeyAuto").click()
		driver.find_element_by_id("cServerName").send_keys("uu123u")
		fwlylx = driver.find_element_by_id("cServerSourceType")
		fwlylx.find_element_by_css_selector("#cServerSourceType > option:nth-child(2)").click()
		driver.find_element_by_id("cAccount").send_keys("001")
		scms = driver.find_element_by_id("cAccountType")
		scms.find_element_by_css_selector("#cAccountType > option:nth-child(2)").click()
		driver.find_element_by_id("cServerUrl").send_keys("http://10.10.10.1/WXQYH")
		driver.find_element_by_id("cDes").send_keys("41244")
		driver.find_element_by_id("saveAction").click()
		time.sleep(5)


