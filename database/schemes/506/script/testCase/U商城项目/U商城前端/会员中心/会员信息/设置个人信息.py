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
		driver.find_element_by_xpath('//*[@id="memberPortrait"]').click()  # 点击会员头像
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="myPortrait"]').click()  # 点击会员头像
		driver.find_element_by_xpath('//input[@class="webuploader-element-invisible"]').send_keys('E:\\tupian\\about2.jpg')  # 点击上传选择图片
		driver.find_element_by_xpath('//a[@class="diyStart"]').click()  # 点击开始上传
		driver.back()
		driver.find_element_by_xpath('//*[@id="cQQ"]').clear()
		driver.find_element_by_xpath('//*[@id="cQQ"]').send_keys(u'888888')  # 输入QQ号
		driver.find_element_by_xpath('//*[@id="save_btn"]').click()  # 点击保存
		driver.switch_to.alert.accept()
		sleep(3)