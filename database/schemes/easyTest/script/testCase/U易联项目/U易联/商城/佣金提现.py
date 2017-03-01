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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(6) > p").click()

		# 开始时间
		driver.find_element_by_id("start").clear()
		driver.find_element_by_id("start").send_keys("2016-02-01")
		time.sleep(1)
		# 结束时间
		driver.find_element_by_id("end").clear()
		driver.find_element_by_id("end").send_keys("2016-07-18")
		time.sleep(1)

		# 状态
		jszt = driver.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(1) > td:nth-child(6) > span")
		jszt.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > span > span.k-input").click()
		# 分销商
		driver.find_element_by_id("distributorName").send_keys(u"刘志峰")
		time.sleep(1)
		# 分销商电话
		driver.find_element_by_id("phoneNum").send_keys("18711999797")
		time.sleep(1)
		# 查询
		driver.find_element_by_id("query_Button").click()
		time.sleep(3)
		# 分销员审核
		# fxysh=driver.find_element_by_css_selector("#distributorList > div.k-grid-content > table > tbody > tr.k-state-selected")
		# ActionChains(driver).click(fxysh).perform()
		# time.sleep(1)
		# driver.find_element_by_css_selector("#distributorList > div.k-header.k-grid-toolbar > a.k-button.k-button-icontext.k-grid-doAudit").click()
		# time.sleep(1)
		# driver.switch_to_alert().accept()


		# 全部审核
		# driver.find_element_by_css_selector("#cashsList > div.k-header.k-grid-toolbar > a.k-button.k-button-icontext.k-grid-doCashsAll").click()
		# sh=driver.find_element_by_css_selector("#editWin > table > tbody > tr:nth-child(1) > td:nth-child(2) > span")
		# sh.find_element_by_css_selector("#editWin > table > tbody > tr:nth-child(1) > td:nth-child(2) > span > span > span.k-input").click()
		# driver.find_element_by_id("payPwd").send_keys("123456")
		# driver.find_element_by_id("remark").send_keys("1")
		# driver.find_element_by_id("save_Button").click()


		# driver.switch_to_alert().accept()
		time.sleep(3)

		# 导出
		driver.find_element_by_css_selector(
			"#cashsList > div.k-header.k-grid-toolbar > a.k-button.k-button-icontext.k-grid-excel").click()
		time.sleep(5)