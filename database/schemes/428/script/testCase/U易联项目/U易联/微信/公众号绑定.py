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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)

		# 切换账号
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(6) > a").click()
		time.sleep(3)
		# 编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(7) > a > i").click()
		time.sleep(1)

		# 基本设置
		driver.find_element_by_id("cWXAccountName").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cWXAccountName").send_keys(s1)
		time.sleep(1)
		driver.find_element_by_id("cCompany").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cCompany").send_keys(s2)
		time.sleep(1)
		driver.find_element_by_id("cDescription").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cDescription").send_keys(s3)
		time.sleep(1)

		# 地区
		s = driver.find_element_by_id("cProvince")
		s.find_element_by_css_selector("#cProvince > option:nth-child(3)").click()
		time.sleep(1)

		s1 = driver.find_element_by_id("cCity")
		s1.find_element_by_css_selector("#cCity > option:nth-child(2)").click()
		time.sleep(1)

		s2 = driver.find_element_by_id("cArea")
		s2.find_element_by_css_selector("#cArea > option:nth-child(2)").click()
		time.sleep(1)

		# 地址
		driver.find_element_by_id("cAddress").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cAddress").send_keys(s4)
		time.sleep(1)

		# 行业
		hy = driver.find_element_by_id("cIndustry")
		hy.find_element_by_css_selector("#cIndustry > option:nth-child(2)").click()
		time.sleep(1)

		# 联系方式
		driver.find_element_by_id("cRealName").clear()
		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRealName").send_keys(s5)
		time.sleep(1)

		driver.find_element_by_id("cPhone").clear()
		driver.find_element_by_id("cPhone").send_keys("18611232192")
		time.sleep(1)
		driver.find_element_by_id("cTel").clear()
		driver.find_element_by_id("cTel").send_keys("13256551677")
		time.sleep(1)

		driver.find_element_by_id("cEmail").clear()
		driver.find_element_by_id("cEmail").send_keys("123123@qq.com")
		time.sleep(1)

		# save
		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		# back
		driver.find_element_by_xpath('//a[@href="/Page/User/WXAccountList"]').click()
		time.sleep(1)

		# 绑定
		driver.find_element_by_xpath('//a[@href="/Page/User/OpenPlatFormBinding"]').click()
		time.sleep(1)

		driver.find_element_by_id("iAgree").click()
		time.sleep(1)

		driver.find_element_by_id("binding_Button").click()
		time.sleep(1)
		driver.back()
