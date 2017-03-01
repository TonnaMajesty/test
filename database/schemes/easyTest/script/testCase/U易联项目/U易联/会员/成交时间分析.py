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

		driver.find_element_by_css_selector("#page_module > li:nth-child(2) > a").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.ajax-link").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(5) > p").click()
		time.sleep(10)
		# 渠道销售统计(列表显示)
		driver.find_element_by_css_selector("#myTab > li.active").click()
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(1) > div > div > div").click()
		driver.find_element_by_xpath('//li[@data-offset-index="1"]').click()
		time.sleep(1)
		cxms = driver.find_element_by_id("query_dDateMode")
		cxms.find_element_by_css_selector("#query_dDateMode > option:nth-child(2)").click()
		time.sleep(1)
		js1 = '$(".drp-popup").show()'
		driver.execute_script(js1)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("exportAction").click()
		time.sleep(3)
		driver.find_element_by_id("query_search").click()
		time.sleep(10)
		# 渠道销售统计（图形显示）
		driver.find_element_by_css_selector("#myTab > li:nth-child(2)").click()
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(1) > div > div > div").click()
		driver.find_element_by_xpath('//li[@data-offset-index="1"]').click()
		time.sleep(5)
		cxms1 = driver.find_element_by_id("query_dDateMode")
		cxms1.find_element_by_css_selector("#query_dDateMode > option:nth-child(2)").click()
		js1 = '$(".drp-popup").show()'
		driver.execute_script(js1)
		driver.find_element_by_class_name("ok").click()
		time.sleep(2)
		driver.find_element_by_id("exportAction").click()
		time.sleep(3)
		driver.find_element_by_id("query_search").click()
		time.sleep(5)