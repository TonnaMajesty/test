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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(9) > p").click()
		time.sleep(3)

		# start time
		driver.find_element_by_id("start").clear()
		driver.find_element_by_id("start").send_keys("2016-07-07")
		time.sleep(1)
		# end time
		driver.find_element_by_id("end").clear()
		driver.find_element_by_id("end").send_keys("2016-07-07")
		time.sleep(1)

		# driver.find_element_by_css_selector("#selArea > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > span > span.k-select > span")
		# driver.find_element_by_css_selector("#accountId_listbox > li:nth-child(2)").click()
		# time.sleep(1)
		# 商品分类
		# s=driver.find_element_by_css_selector("#selArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > span > span.k-select > span")
		# s.find_element_by_css_selector("#classification_listbox > li:nth-child(2)").click()
		# time.sleep(1)
		# 商品分组
		# s1=driver.find_element_by_css_selector("#selArea > table > tbody > tr:nth-child(2) > td:nth-child(4) > span > span > span.k-select > span")
		# s1.find_element_by_css_selector("#comgroup_listbox > li:nth-child(3)").click()
		# time.sleep(1)
		# 商品名称
		# s2=driver.find_element_by_css_selector("#selArea > table > tbody > tr:nth-child(2) > td:nth-child(6) > span > span > span.k-select > span")
		# s2.find_element_by_css_selector("#comname_listbox > li:nth-child(2)").click()
		# time.sleep(1)
		driver.find_element_by_id("sel_Button").click()

		driver.find_element_by_css_selector("#content > div > div > a:nth-child(2)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#content > div > div > a:nth-child(3)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#content > div > div > a:nth-child(4)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#content > div > div > a:nth-child(5)").click()

		driver.find_element_by_css_selector("#content > div > div > a:nth-child(8)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#content > div > div > a:nth-child(9)").click()