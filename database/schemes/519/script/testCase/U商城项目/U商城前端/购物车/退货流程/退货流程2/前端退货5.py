# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()

		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click()  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[4]/ul/li[1]/a/span').click()  # 点击我的订单
		driver.find_element_by_xpath('//*[@id="orderList"]/table/tbody/tr[2]/td[5]/div[3]/a').click()  # 点击请退货

		jg = driver.find_element_by_xpath('//select[@id="expresscompany"]')
		jg.find_element_by_xpath('//option[@data-id="4"]').click()  # 选择顺丰快递

		driver.find_element_by_xpath('//input[@id="expressnum"]').send_keys(u'123456789')  # 输入快递单号
		driver.find_element_by_xpath('//*[@id="modalSure"]').click()  # 点击确定
		sleep(3)
