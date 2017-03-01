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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li:nth-child(3) > a').click()  # 点击权限分配

		jn = driver.find_element_by_xpath('//select[@ng-model="iRoleId"]')
		jn.find_element_by_xpath('//option[@label="老王"]').click()

		driver.find_element_by_xpath('//*[@id="allClick1"]').click()  # 选择商品管理全选
		driver.find_element_by_xpath('//*[@id="role"]/div/div[2]/a').click()  # 点击保存

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/ul/li[2]/a').click()  # 点击人员权限设置

		jk = driver.find_element_by_xpath('//select[@ng-change="userChange()"]')
		jk.find_element_by_xpath('//option[@label="老张->asdasds@jql"]').click()

		driver.find_element_by_xpath('//*[@id="allClick1"]').click()  # 选择商品管理全选
		driver.find_element_by_xpath('//*[@id="role"]/div[1]/div[2]/a').click()  # 点击保存
		sleep(3)
		driver.find_element_by_xpath('//*[@id="role"]/table/tbody/tr/td[5]/a').click()  # 点击修改
		driver.find_element_by_xpath('//*[@id="allClick2"]').click()  # 选择订单管理全选
		driver.find_element_by_xpath('//*[@id="role"]/div[1]/div[2]/a').click()  # 点击保存
		sleep(3)