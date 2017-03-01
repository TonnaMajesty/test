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

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark').click()  # 点击订单管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[3]/a').click()  # 点击退货列表
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody[1]/tr[1]/td/div[3]/div/button').click()  # 点击完成
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定
		sleep(3)
