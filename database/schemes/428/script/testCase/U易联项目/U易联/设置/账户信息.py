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
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(1) > p").click()
		time.sleep(5)

		# 联系电话
		driver.find_element_by_id("cTel").clear()
		driver.find_element_by_id("cTel").send_keys("15244697398")
		time.sleep(1)
		# 公司名称
		driver.find_element_by_id("cCompany").clear()
		driver.find_element_by_id("cCompany").send_keys("15244697398")
		time.sleep(1)

		# driver.find_element_by_id("cAlias").send_keys("killkill")
		# 地区
		s = driver.find_element_by_id("cProvince")
		s.find_element_by_css_selector("#cProvince > option:nth-child(4)").click()
		time.sleep(1)

		s1 = driver.find_element_by_id("cCity")
		s1.find_element_by_css_selector("#cCity > option:nth-child(3)").click()
		time.sleep(1)

		s2 = driver.find_element_by_id("cArea")
		s2.find_element_by_css_selector("#cArea > option:nth-child(4)").click()
		time.sleep(1)

		# 行业
		hy = driver.find_element_by_id("cIndustry")
		hy.find_element_by_css_selector("#cIndustry > option:nth-child(2)").click()
		time.sleep(1)

		# 保存
		driver.find_element_by_id("saveAction").click()
		time.sleep(5)
