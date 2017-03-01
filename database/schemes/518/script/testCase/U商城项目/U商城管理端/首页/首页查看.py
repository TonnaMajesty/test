# coding=utf-8
import time

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
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/a").click()  # 点击待付款订单后面的数字
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/a").click()  # 点击详情
		# driver.back()
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/button[1]").click()  # 点击改价
		# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[1]").click()  # 点击取消
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/button[2]").click()  # 点击改地址
		# driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()  # 点击取消
		driver.find_element_by_link_text("首页").click()
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[1]/a[2]").click()  # 点击本月
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[1]/a[3]").click()  # 点击本年
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[1]/a[1]").click()  # 点击本周
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/a[2]").click()  # 点击本季
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/a[3]").click()  # 点击本年
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/a[1]").click()  # 点击本月
		time.sleep(3)
