# coding=utf-8
from time import sleep

from selenium.webdriver import ActionChains

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()

		js = '$(".classify").show()'
		driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[1]/div/div[1]/a/img').click()  # 点击HK直邮美国商品
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_link_text('立即订购').click()  # 点击立即订购
		# driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[9]/div[2]/div[2]/div/input').send_keys('老王')
		sleep(3)
		driver.find_element_by_css_selector('body > div > div.row > div.col-xs-12.main > div:nth-child(2) > div > div.osubmit > div > button').click()  # 点击提交订单
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[1]/ul/li[4]/div[1]/input').click() # 选择储值卡
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[2]/span/button').click() # 点击确认付款
		sleep(3)