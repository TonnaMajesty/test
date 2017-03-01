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
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[1]/span[2]").click()  # 点击订单管理
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[4]/a").click()  # 点击收款列表
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/a[2]").click()  # 点击付款成功
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys(u"000001")  # 支付单号输入“”
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/button").click()  # 点击搜索按钮
		driver.find_element_by_link_text("付款失败").click()
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/input").send_keys(u"000002")  # 订单编号输入“”
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/button").click()  # 点击搜索按钮
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[4]/a").click()  # 点击收款列表
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[7]/div/a").click()  # 点击详情