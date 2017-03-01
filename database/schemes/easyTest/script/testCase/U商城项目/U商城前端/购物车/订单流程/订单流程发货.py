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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[2]/a').click()  # 点击待发货订单
		driver.find_elements_by_xpath('//input[@placeholder="昵称/电话"]')[-1].send_keys('老王')  # 输入查询条件
		driver.find_element_by_xpath('//button[@ng-click="searchLogic.searchClick()"]').click(3)  # 点击搜索
		driver.find_elements_by_xpath('//button[@class="btn btn-xs btn-delivery ng-scope"]')[-2].click()  # 点击第一个订单后的发货按钮
		driver.find_elements_by_xpath('//select[@ng-options="sub.name for sub in logisticsCorpList"]')[-1].click()
		driver.find_element_by_xpath('//option[@label="中国邮政EMS"]').click()  # 选择邮政快递
		driver.find_elements_by_xpath('//input[@ng-model="logisticsNo"]')[-1].send_keys('111112222')
		driver.find_element_by_xpath('//*[@id="btnDeliver"]').click()  # 点击确定
		sleep(3)
