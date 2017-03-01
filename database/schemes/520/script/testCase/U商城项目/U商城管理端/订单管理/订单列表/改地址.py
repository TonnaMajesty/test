# coding=utf-8
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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/from/div[1]/div/div/a[2]').click()  # 点击待付款
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/button[2]").click()  # 点击改地址按钮
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/form/div[1]/div/input").clear()
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/form/div[1]/div/input").send_keys(U"王二小")
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/form/div[3]/div/textarea").clear()
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/form/div[3]/div/textarea").send_keys(u"用友软件园西区")
		driver.find_element_by_xpath("//button[@ng-click='ok()']").click()  # 点击保存按钮

