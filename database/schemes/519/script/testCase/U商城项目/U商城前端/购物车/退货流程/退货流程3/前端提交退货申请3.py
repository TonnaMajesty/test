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
		driver.find_element_by_xpath('//*[@id="orderList"]/table/tbody/tr[2]/td[8]/div[1]/a').click()  # 点击确认收货
		driver.find_element_by_xpath('//*[@id="modalSure"]').click()  # 点击确认
		sleep(2)
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[4]/ul/li[1]/a/span').click()  # 点击我的订单
		driver.find_element_by_xpath('//*[@id="orderList"]/table/tbody/tr[2]/td[5]/div[3]/span/a').click()  # 点击退款申请
		sleep(3)
		driver.find_element_by_xpath('//*[@id="return_tabs"]/ul/li[2]').click() #点击我要退款无需退货
		driver.find_element_by_xpath('//*[@id="money"]/div/input').send_keys(u'0.1')  # 输入退货金额
		driver.find_element_by_xpath('//*[@id="returnPost"]/div/button').click()  # 点击提交申请
		sleep(3)
