# coding=utf-8
from time import sleep

from selenium.webdriver import ActionChains

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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark').click()  # 点击订单管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[7]/a').click()  # 点击代客下单
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[3]/button').click()  # 点击创建会员
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div/span[2]/input').send_keys(u'13900139000')  # 输入手机号
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[3]/div/button[2]').click()  # 点击确定
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/div/div[3]/p/a').click()  # 点击跳转到前端
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		js = '$(".classify").show()'
		driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[2]/div/div[1]/a/img').click()  # 点击商品
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.find_element_by_link_text('立即订购').click()  # 点击立即订购
		sleep(3)
		driver.find_element_by_css_selector('body > div > div.row > div.col-xs-12.main > div:nth-child(2) > div > div.osubmit > div > button').click()  # 点击提交订单
		sleep(3)
