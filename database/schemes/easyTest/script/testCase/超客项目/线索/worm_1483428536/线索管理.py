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
		driver.find_element_by_xpath('#menuSider > li:nth-child(8) > div').click()  # 点击线索
		sleep(3)
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(1) > a').click()  # 点击线索管理
		driver.find_element_by_css_selector("#lead_tab > li:nth-child(2)").click()  # 点击已处理
		driver.find_element_by_css_selector("#lead_tab > li:nth-child(3)").click()  # 点击已转化联系人
		driver.find_element_by_css_selector("#lead_tab > li:nth-child(4)").click()  # 点击已转化客户
		driver.find_element_by_css_selector("#lead_tab > li:nth-child(5)").click()  # 点击已关闭
		driver.find_element_by_css_selector("#lead_tab > li:nth-child(6)").click()  # 点击全部线索
		driver.find_element_by_xpath('//*[@id="lead_tab"]/li[1]').click()  # 点击未处理
		driver.find_element_by_xpath('#menuSider > li:nth-child(8) > div').click()  # 点击线索