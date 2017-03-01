# coding=utf-8
from time import sleep

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
		tool  = utils

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li.title.pointer').click()  # 点击商城设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li:nth-child(4) > a').click()  # 点击商城配置
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click()  # 点击确定
		driver.find_element_by_xpath('//*[@id="tablist"]/form/div[1]/div[1]/div[1]/input[1]').click()  # 选择是
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click()  # 点击确定
		driver.find_element_by_xpath('//*[@id="tablist"]/form/div[1]/div[4]/div[1]/input[2]').click()  # 选择储值卡否
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click()  # 点击确定
		driver.find_element_by_xpath('//*[@id="tablist"]/form/div[1]/div[4]/div[1]/input[1]').click() # 选择储值卡是
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click()  # 点击确定
		sleep(3)
