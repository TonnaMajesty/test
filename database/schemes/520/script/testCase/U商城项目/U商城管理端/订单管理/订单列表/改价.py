# coding=utf-8
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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/from/div[1]/div/div/a[2]').click()#点击待付款
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/button[1]").click() # 点击第一行订单的改价
		#driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/input").clear()
		#driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/input").send_keys("1")  # 修改邮费
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/input").clear()
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/input").send_keys("1")  # 修改实付金额
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click()  # 点击确定
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/button[1]").click() # 点击第一行订单的改价
		#driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/input").clear()
		#driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/input").send_keys("0")  # 修改邮费
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/input").clear()
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/input").send_keys("9.8")  # 修改实付金额
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click()  # 点击确定
