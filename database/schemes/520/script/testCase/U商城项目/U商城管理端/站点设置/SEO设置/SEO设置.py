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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li.title.pointer').click()  # 点击站点设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(11) > a').click()  # 点击SEO设置
		driver.find_elements_by_xpath('//a[@class="colorblue"]')[0].click()  # 点击编辑
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div/button').click()  # 点击保存
		driver.find_elements_by_xpath('//a[@class="colorblue"]')[1].click()  # 点击回复默认设置
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)