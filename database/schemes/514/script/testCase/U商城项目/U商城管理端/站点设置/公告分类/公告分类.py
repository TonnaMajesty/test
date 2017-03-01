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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(6) > a').click()  # 点击公告分类
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()  # 点击新增
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[2]/input').send_keys(u'无字天书')  # 输入名称
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[3]/button[2]').click(2)  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr/td[2]/a[1]').click()  # 点击编辑
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/div/div[2]/input').clear()
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/div/div[2]/input').send_keys(u'无量天尊')
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[3]/button[2]').click(2)  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr/td[2]/a[2]').click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)
		# driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()

