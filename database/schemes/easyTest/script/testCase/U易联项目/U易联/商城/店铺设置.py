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
		driver.find_element_by_id("cShopName").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cShopName").send_keys(s1)
		time.sleep(1)
		driver.find_element_by_id("cShareTitle").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cShareTitle").send_keys(s2)
		time.sleep(1)
		driver.find_element_by_css_selector(
			"#c-zone > div:nth-child(5) > div.form-slider > div:nth-child(2) > div.slider-content > ul > li:nth-child(2) > label > input").click()
		driver.find_element_by_css_selector(
			"#c-zone > div:nth-child(5) > div.form-slider > div:nth-child(2) > div.slider-content > ul > li:nth-child(2) > input").clear()
		driver.find_element_by_css_selector(
			"#c-zone > div:nth-child(5) > div.form-slider > div:nth-child(2) > div.slider-content > ul > li:nth-child(2) > input").send_keys(
			"123")
		time.sleep(1)
		zsfs = driver.find_element_by_id("iDisplayType")
		zsfs.find_element_by_css_selector("#iDisplayType > option:nth-child(2)").click()
		time.sleep(1)
		driver.find_element_by_id("cServicePhone").clear()
		driver.find_element_by_id("cServicePhone").send_keys("18500738046")
		time.sleep(1)
		driver.find_element_by_id("cServicePhone").send_keys("1")
		driver.find_element_by_id("fDerateFee").send_keys("1")
		driver.find_element_by_id("fUseScore").send_keys("1")
		driver.find_element_by_id("iOrderTimeLimit").send_keys("1")
		qxdd = driver.find_element_by_id("iTimeEffectiveUnit")
		qxdd.find_element_by_css_selector("#iTimeEffectiveUnit > option:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_css_selector("#c-zone > div:nth-child(14) > div > div:nth-child(1) > input").click()
		driver.find_element_by_css_selector("#c-zone > div:nth-child(14) > div > div:nth-child(2) > input").click()
		driver.find_element_by_id("bAllowTicket").click()
		driver.find_element_by_css_selector("#c-zone > div:nth-child(16) > div > div:nth-child(1) > input").click()
		driver.find_element_by_css_selector("#c-zone > div:nth-child(16) > div > div:nth-child(2) > input").click()
		sfz = driver.find_element_by_id("iSupportBuyer")
		sfz.find_element_by_css_selector("#iSupportBuyer > option:nth-child(3)").click()
		time.sleep(1)
		driver.find_element_by_id("bHasInvoice").click()
		time.sleep(3)
		driver.find_element_by_id("saveAction").click()
		time.sleep(5)