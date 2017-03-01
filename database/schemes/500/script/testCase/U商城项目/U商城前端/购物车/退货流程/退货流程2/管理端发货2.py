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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[2]/a').click()  # 点击订单列表
		driver.find_elements_by_xpath('//button[@class="btn btn-xs btn-delivery ng-scope"]')[0].click()  # 点击第一个订单发货

		js = driver.find_elements_by_xpath('//select[@ng-options="sub.name for sub in logisticsCorpList"]')[-1]
		js.find_element_by_xpath('//option[@label="申通快递"]').click()  # 选择申通快递

		driver.find_elements_by_xpath('//input[@ng-model="logisticsNo"]')[-1].send_keys(u'1234560')  # 输入快递单号
		driver.find_element_by_xpath('//button[@id="btnDeliver"]').click()  # 点击确定
		sleep(3)
