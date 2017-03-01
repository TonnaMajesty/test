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

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark','订单管理').click()  # 点击订单管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[3]/a','退货列表').click()  # 点击退货列表
		driver.find_element_by_xpath('//button[@ng-click="confirmDialog(saleReturn)"]','驳回').click()  # 点击驳回
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div/textarea').send_keys(u'产品无问题，请确认后再退货')  # 输入驳回原因
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[3]/div/div/button[2]').click()  # 点击驳回
		driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click() # 点击确定
		sleep(3)