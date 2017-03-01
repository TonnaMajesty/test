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

		driver.find_element_by_css_selector("#page_module > li:nth-child(3) > a").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div:nth-child(1)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(4) > p").click()

		# 开始时间
		driver.find_element_by_id("start").clear()
		driver.find_element_by_id("start").send_keys("2015-02-01")
		time.sleep(1)
		# 结束时间
		driver.find_element_by_id("end").clear()
		driver.find_element_by_id("end").send_keys("2017-12-18")
		time.sleep(1)
		# 订单号
		driver.find_element_by_id("orderCode").send_keys("1603161031359841")
		time.sleep(1)
		# 订单状态
		ddzt = driver.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
		ddzt.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > span > span.k-input").click()
		time.sleep(1)
		# 订单完成时间
		driver.find_element_by_id("finishTime").send_keys("2016-03-16")
		time.sleep(1)
		# 分销商
		#driver.find_element_by_id("distributorName").send_keys(u"刘志峰")
		time.sleep(1)
		# 查询
		driver.find_element_by_id("query_Button").click()
		time.sleep(3)
		# 查询验证
		search = driver.find_element_by_css_selector("#orderList > div.k-grid-content > table > tbody > tr:nth-child(1) > td:nth-child(5)","findAssert").text
		self.assertEqual(search, "刘志峰", "查询成功")

		# 导出
		driver.find_element_by_css_selector("#orderList > div.k-header.k-grid-toolbar > a").click()
		time.sleep(3)
