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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(3) > p").click()
		time.sleep(10)
		# 储值活动分析（列表显示）
		driver.find_element_by_css_selector("#myTab > li.active").click()
		czhd = driver.find_element_by_id("query_iStorageActivity")
		czhd.find_element_by_css_selector("#query_iStorageActivity > option:nth-child(2)").click()
		driver.find_element_by_id("query_dDateRange").click()
		js1 = '$(".drp-timeline").show()'
		driver.execute_script(js1)
		driver.find_element_by_class_name("ok").click()
		qd = driver.find_element_by_id("query_iChannel")
		qd.find_element_by_css_selector("#query_iChannel > option:nth-child(2)").click()
		driver.find_element_by_id("query_search").click()
		time.sleep(5)
		driver.find_element_by_id("exportAction").click()
		# 储值活动分析（图形显示）
		driver.find_element_by_xpath('//li[@data-target="storeage"]').click()
		czhd = driver.find_element_by_id("query_iStorageActivity")
		czhd.find_element_by_css_selector("#query_iStorageActivity > option:nth-child(2)").click()
		driver.find_element_by_id("query_dDateRange",'123').click()
		js1 = '$(".drp-timeline").show()'
		driver.execute_script(js1)
		driver.find_element_by_class_name("ok").click()
		qd = driver.find_element_by_id("query_iChannel")
		qd.find_element_by_css_selector("#query_iChannel > option:nth-child(2)").click()
		driver.find_element_by_id("query_search").click()
		time.sleep(5)
		driver.find_element_by_id("exportAction").click()