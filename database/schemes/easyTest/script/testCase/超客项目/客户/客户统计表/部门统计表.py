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
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(3) > h4').click()  # 点击客户统计表
		driver.find_element_by_link_text("部门统计表").click()  # 点击部门统计表
		driver.implicitly_wait(10)
		driver.find_element_by_link_text("全公司").click()  # 点击全公司
		sleep(5)
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(3) > h4').click()  # 点击客户统计表
		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户
