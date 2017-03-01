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

		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/a").click()  # 点击首页
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark").click()  # 点击订单管理
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[2]/a").click()  # 点击订单列表
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > from > div:nth-child(2) > div > div > a.active").click()  #点击代发货
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div.ng-scope > div > button:nth-child(2)').click()  # 点击配送门店
		driver.find_element_by_css_selector('input[ng-model="inputName"]').send_keys('用友门店')#输入查询条件
		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-body > div:nth-child(1) > div > div:nth-child(3) > button').click()#点击搜门店
		driver.find_element_by_css_selector('#storeSelector > ul > li > div > span.spanTitle.ng-binding > input[type="radio"]').click()  # 选择门店
		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-footer > button:nth-child(2)').click()  # 点击确定
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > from > div:nth-child(2) > div > div > a.active").click()  #点击代发货
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input').click()#选择第一个订单
		driver.find_element_by_xpath('//a[@ng-click="store.openStoreDialog()"]').click()#点击批量指定配送门店
		driver.find_element_by_xpath('//*[@id="storeSelector"]/ul/li[2]/div/span[1]/input').click()#选择门店
		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-footer > button:nth-child(2)').click()  # 点击确定
		sleep(3)