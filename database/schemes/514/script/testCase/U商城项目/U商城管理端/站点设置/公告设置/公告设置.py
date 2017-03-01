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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(7) > a').click()   # 点击公告设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/a').click()  # 点击新增
		driver.find_element_by_xpath('//*[@id="txtTitle" and @placeholder="公告标题"]').send_keys(u'重要通知')  # 输入标题

		# js = driver.find_element_by_xpath('//*[@id="selNoticeType"]/div/span');
		# js.find_element_by_xpath('//*[@id="ui-select-choices-row-0-0"]/a/span').click();  # 选择普通公告

		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(2)  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[4]/div/table/tbody/tr/td[5]/a[1]').click()  # 点击编辑
		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(2)  # 点击保存
		driver.find_element_by_xpath('//a[@ng-click="delNotice($index)"]').click()  # 点击删除
		driver.find_element_by_xpath('//button[@class="btn btn-primary btn-lg"]').click()  # 点击确定
		sleep(3)