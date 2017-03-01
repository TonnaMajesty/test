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
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(3) > p").click()
		time.sleep(3)

		# 清楚标签
		driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > input[type="checkbox"]').click()
		driver.find_element_by_id("labelClear").click()
		driver.switch_to_alert().accept()
		time.sleep(2)

		# 导出
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)

		# 同步
		driver.find_element_by_id("fetchAction").click()
		time.sleep(15)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(5)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 高级筛选
		driver.find_element_by_id("labelQuery").click()
		time.sleep(2)

		driver.find_element_by_id("cNickNameQuery").send_keys("exia")
		time.sleep(1)

		xb = driver.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(1) > td:nth-child(4) > span > span")
		xb.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(1) > td:nth-child(4) > span > span > span.k-input").click()
		time.sleep(1)

		zt = driver.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > span")
		zt.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > span > span.k-input").click()
		time.sleep(1)

		qd = driver.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > span")
		qd.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > span > span.k-input").click()
		time.sleep(1)

		driver.find_element_by_id("cRealNameQuery").send_keys("exia")
		time.sleep(1)

		driver.find_element_by_id("cPhoneQuery").send_keys("18500738046")

		gj = driver.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(3) > td:nth-child(2) > span > span")
		gj.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(3) > td:nth-child(2) > span > span > span.k-input").click()
		time.sleep(1)

		sf = driver.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(3) > td:nth-child(4) > span > span")
		sf.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(3) > td:nth-child(4) > span > span > span.k-input").click()
		time.sleep(1)

		bqcl = driver.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(4) > td:nth-child(2) > span > span")
		bqcl.find_element_by_css_selector(
			"#labelQueryWin > table > tbody > tr:nth-child(4) > td:nth-child(2) > span > span > span.k-input").click()
		time.sleep(1)

		driver.find_element_by_id("dSubscribeTimeStartQuery").send_keys("2016-01-01")
		time.sleep(1)

		driver.find_element_by_id("dSubscribeTimeEndQuery").send_keys("2016-02-01")
		time.sleep(1)

		driver.find_element_by_id("query_Button").click()
		time.sleep(1)

		driver.back()
		driver.back()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(3) > p").click()

		# 查询
		driver.find_element_by_id("query_cNickName").send_keys("exia")
		time.sleep(1)

		driver.find_element_by_id("query_cCountry").send_keys(u"中国")
		time.sleep(1)

		driver.find_element_by_id("query_cProvince").send_keys(u"黑龙江")
		time.sleep(1)

		driver.find_element_by_id("query_cCity").send_keys(u"哈尔滨")
		time.sleep(1)

		xb = driver.find_element_by_id("query_iSex")
		xb.find_element_by_css_selector("#query_iSex > option:nth-child(3)").click()
		time.sleep(1)

		zt = driver.find_element_by_id("query_iStatus")
		zt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("query_cChannelName").send_keys("123")
		time.sleep(1)

		hyzc = driver.find_element_by_id("query_iMemberStatus")
		hyzc.find_element_by_css_selector("#query_iMemberStatus > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(3)