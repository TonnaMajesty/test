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
		sleep(3)
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[1]/div/div[1]/a/img').click()  # 点击美国GNC
		# driver.switch_to_window(driver.window_handles[1])
		driver.switch_to.window(1)
		driver.find_element_by_css_selector('.now-order').click()  # 点击立即订购
		# driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[2]/div[1]/span').click()  # 选择收货地址
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[11]/a').click()  # 点击发票后修改
		driver.find_element_by_xpath('//*[@id="InvoiceManage"]/div/div/div[2]/form/div[1]/div/ul/li[1]').click()  # 点普通发票
		driver.find_element_by_xpath('//*[@id="InvoiceManage"]/div/div/div[2]/form/div[1]/div/ul/li[2]').click()  # 点不开发票
		driver.find_element_by_xpath('//*[@id="InvoiceManage"]/div/div/div[3]/button[2]').click()  # 点保存
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[14]/div/button').click()  # 点击提交订单
		driver.close()
		driver.switch_to_window(driver.window_handles[0])

		js = '$(".classify").show()'
		driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		sleep(3)
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[2]/div/div[1]/a/img').click()  # 点击直邮美国ARG
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.find_element_by_css_selector('.now-order').click()  # 点击立即订购
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[11]/a').click()  # 点击发票后修改
		driver.find_element_by_xpath('//*[@id="InvoiceManage"]/div/div/div[2]/form/div[1]/div/ul/li[1]').click()  # 点普通发票
		driver.find_element_by_xpath('//*[@id="InvoiceManage"]/div/div/div[2]/form/div[1]/div/ul/li[2]').click()  # 点不开发票
		driver.find_element_by_xpath('//*[@id="InvoiceManage"]/div/div/div[3]/button[2]').click()  # 点保存
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[14]/div/button').click()  # 点击提交订单
		sleep(3)