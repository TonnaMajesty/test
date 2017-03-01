# coding=utf-8
import time

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



		driver.find_element_by_css_selector("#page_module > li:nth-child(3) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(6) > p").click()
		time.sleep(3)
		driver.find_element_by_xpath('//a[@href="/Page/Shop/DeliveryCompany"]').click()
		driver.find_element_by_css_selector(
			'#companyList > div:nth-child(7) > div > label > input[type="checkbox"]').click()
		time.sleep(3)
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		time.sleep(3)
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		driver.find_element_by_id("query_cCompanyName").send_keys(u"天天快递")
		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		
