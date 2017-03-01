# coding=utf-8
from time import sleep, time

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils

class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user


		#driver.find_element_by_link_text(u"超客").click()  # 点击超客
		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户
		sleep(3)
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(2) > h4').click()  # 点击客户明细表
		driver.find_element_by_css_selector("#menuSider > li.col-sider-moren.current > ul > li.menu-three.col-sider-sesecond.current > ul > li:nth-child(1) > a > span").click()  # 点击部门明细表
		driver.implicitly_wait(10)
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(3) > div").click()  # 点击负责的客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(4) > div").click()  # 点击重点客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(5) > div").click()  # 点击关注的客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(6) > div").click()  # 点击冻结客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(2) > div").click()  # 点击全部客户
		driver.find_element_by_css_selector("#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr:nth-child(3) > td.ant-table-row-expand-icon-cell > span").click()  # 点击“+”
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(3) > div").click()  # 点击负责的客户
		driver.find_element_by_css_selector("#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr:nth-child(2) > td.ant-table-row-expand-icon-cell > span").click()  # 点击“+”
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(4) > div").click()  # 点击重点客户
		driver.find_element_by_css_selector("#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr > td.ant-table-row-expand-icon-cell > span").click() #点击“+”
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(5) > div").click()  # 点击关注的客户
		driver.find_element_by_css_selector("#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr > td.ant-table-row-expand-icon-cell > span").click()  # 点击“+”
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(2) > h4').click()  # 点击客户明细表
		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户