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

		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[2]/a').click() # 点击退出
		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[1]/a[2]').click()  # 点击免费注册
		driver.find_element_by_xpath('//*[@id="terms_error_sym"]').click()  # 点击用户注册协议
		driver.switch_to_window(driver.window_handles[1])
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.back()
		sleep(3)
