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

		driver.find_element_by_css_selector("#page_module > li:nth-child(4) > a").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div:nth-child(1)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div.typ > a:nth-child(3) > p").click()
		time.sleep(3)

		# 用户分析
		driver.find_element_by_id("start").clear()
		driver.find_element_by_id("start").send_keys("2016-06-31")
		time.sleep(1)

		driver.find_element_by_id("end").clear()
		driver.find_element_by_id("end").send_keys("2016-07-31")
		time.sleep(1)

		# gzh=driver.find_element_by_css_selector("#selArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
		# gzh.find_element_by_css_selector("#accountId_listbox > li:nth-child(5)").click()
		time.sleep(1)

		gjzb = driver.find_element_by_css_selector(
			"#selArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
		gjzb.find_element_by_css_selector(
			"#selArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > span > span.k-input").click()
		time.sleep(1)

		zzly = driver.find_element_by_css_selector(
			"#selArea > table > tbody > tr:nth-child(2) > td:nth-child(4) > span")
		zzly.find_element_by_css_selector(
			"#selArea > table > tbody > tr:nth-child(2) > td:nth-child(4) > span > span > span").click()
		time.sleep(2)

		driver.find_element_by_id("sel_Button").click()
		time.sleep(2)

		driver.find_element_by_css_selector("#userAnalysisGrid > div.k-header.k-grid-toolbar > a").click()
		time.sleep(3)
		# 用户属性
		driver.find_element_by_xpath('//a[@href="/Page/UPLogger/UserAnalysisTwoBQ"]').click()
		time.sleep(1)

		gzh2 = driver.find_element_by_css_selector("#selArea > table > tbody > tr > td:nth-child(2) > span")
		gzh2.find_element_by_css_selector(
			"#selArea > table > tbody > tr > td:nth-child(2) > span > span > span.k-input").click()
		time.sleep(1)

		gjzb2 = driver.find_element_by_css_selector("#selArea > table > tbody > tr > td:nth-child(4) > span")
		gjzb2.find_element_by_css_selector(
			"#selArea > table > tbody > tr > td:nth-child(4) > span > span > span.k-input").click()
		time.sleep(1)

		driver.find_element_by_id("sel_Button").click()
		time.sleep(2)