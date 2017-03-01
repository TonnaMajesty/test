# coding=utf-8
import time

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase



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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.ajax-link").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(1) > p").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(4) > p").click()
		time.sleep(5)
		# 导出
		driver.find_element_by_id("exportAction").click()

		# 储值卡明细
		driver.find_element_by_id("query_cRealName").send_keys("123")

		driver.find_element_by_id("query_cRealName").clear()

		time.sleep(3)
		lylx = driver.find_element_by_id("query_iType")
		lylx.find_element_by_css_selector("#query_iType > option:nth-child(3)").click()

		jyly = driver.find_element_by_id("query_iSource")
		jyly.find_element_by_css_selector("#query_iSource > option:nth-child(6)").click()

		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(2) > div > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_search").click()

		time.sleep(3)

		# 储值卡管理
		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberStorageCard"]').click()

		# 会员卡号
		driver.find_element_by_id("query_cPhone").send_keys("18500738046")
		driver.find_element_by_id("query_search").click()
		driver.find_element_by_id("query_cPhone").clear()
		# 会员姓名
		driver.find_element_by_id("query_cRealName").send_keys("123")
		driver.find_element_by_id("query_search").click()
		driver.find_element_by_id("query_cRealName").clear()
		# 实体卡号
		driver.find_element_by_id("query_cStorageCardNum").send_keys("18500738046")
		driver.find_element_by_id("query_search").click()
		driver.find_element_by_id("query_cStorageCardNum").clear()

		# 时间
		js1 = '$(".drp-popup").show()'
		driver.execute_script(js1)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(2) > div > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_search").click()