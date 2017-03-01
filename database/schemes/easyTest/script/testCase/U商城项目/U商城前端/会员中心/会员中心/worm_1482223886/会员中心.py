# coding=utf-8
from time import sleep

from PyQt5.QtCore.QByteArray import insert

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值
		##################################################################
		该方法内进行测试用例的编写
		'''
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click()  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="memberPortrait" and @class="member-portrait fl"]').click()  # 点击会员头像
		driver.switch_to.window(driver.window_handles[1])
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@data-status="PAYMONEY"]').click()  # 点击待付款
		driver.find_element_by_xpath('//*[@data-status="DELIVERGOODS"]').click()  # 点击待发货
		driver.find_element_by_xpath('//*[@data-status="TAKEDELIVERY"]').click()  # 点击待收货
		driver.find_element_by_xpath('//*[@id="orderListsHeader"]/li[1]').click()  # 点击全部订单
		driver.find_element_by_xpath('//*[@id="orderstatus"]/li[1]/a/p/span').click()  # 点击待付款后数据
		driver.find_element_by_xpath('//*[@id="orderstatus"]/li[2]/a/p/span').click()  # 点击待发货后数据
		driver.find_element_by_xpath('//*[@id="orderstatus"]/li[3]/a/p/span').click()  # 点击待收货后数据
		driver.find_element_by_xpath('//*[@id="orderstatus"]/li[4]/a/p/span').click()  # 点击待评价后数据
		driver.switch_to.window(driver.window_handles[1])
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="memberassert"]/li[1]/a/div[2]/span[1]').click()  # 点击积分后数据
		driver.switch_to.window(driver.window_handles[1])
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="memberassert"]/li[2]/a/div[2]/span[1]').click()  # 点击优惠券后数据
		driver.switch_to.window(driver.window_handles[1])
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		sleep(3)

