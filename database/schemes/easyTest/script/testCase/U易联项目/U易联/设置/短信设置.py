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

		driver.find_element_by_css_selector("#page_module > li:nth-child(6) > a").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(5) > p").click()
		time.sleep(5)

		# 短信设置
		driver.find_element_by_id("cSmsHeader").send_keys("1")
		driver.find_element_by_id("bRegMemberMsg").click()
		driver.find_element_by_id("bRegMemberMsg").click()
		time.sleep(2)

		# 短信发送记录
		driver.find_element_by_xpath('//a[@href="/Page/User/MsgRecordList"]').click()
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 短信充值记录
		driver.find_element_by_xpath('//a[@href="/Page/User/MsgRechargeRecordList"]').click()
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()
		time.sleep(5)
