# coding=utf-8
from time import sleep

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
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark").click()  # 点击订单管理
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[2]/a").click()  # 点击订单列表
		#driver.find_element_by_link_text("待发货").click()
		#driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > nav > ul > li.next > a > span").click() #点击末页
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div.ng-scope > div > button.btn.btn-xs.btn-delivery.ng-scope').click() # 点击发货
		driver.find_element_by_xpath('//*[@class="form-control ng-pristine ng-untouched ng-valid" and @ng-model="deliveryCorp" and @ng-options="sub.name for sub in logisticsCorpList"]').click()#点击快递公司
		driver.find_element_by_xpath("//*[@value='3' and @label='顺丰速运']").click()  # 选择顺丰快递
		driver.find_element_by_xpath("//*[@id='ngdialog1']/div[2]/div[2]/form/div[3]/div/input").send_keys(u"123456")  # 快递单号栏输入123456
		driver.find_element_by_xpath("//*[@id='btnDeliver']").click()  # 点击确定
		sleep(3)
