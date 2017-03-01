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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(12) > a').click()   # 点击关键词设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()  # 点击新增
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(u'关键是什么')  # 输入关键词名称
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/span[2]').click()  # 点击是否默认
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/button[2]').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr/td[7]/a[1]').click()  # 点击修改
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/button[2]').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr/td[6]/a').click()  # 点击进入
		driver.switch_to.window(driver.window_handles[1])
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr/td[7]/a[2]').click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)