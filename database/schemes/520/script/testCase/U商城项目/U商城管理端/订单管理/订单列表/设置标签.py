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
		sleep(3)
		driver.find_element_by_link_text('标签设置').click()  # 点击标签设置
		# js1 = '$("#laydate_box").show()'
		# driver.execute_script(js1)
		# driver.find_element_by_xpath('//li[@ng-click="setTaginfo()"]')[1].click()  # 点击标签设置
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/a').click()  # 点击增加按钮
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[2]/input").send_keys(u"团购")  # 输入团购
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[3]/input").send_keys(u"123")  # 输入123
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/a/span").click()  # 点击增加按钮
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/table/tbody/tr[2]/td[2]/input").send_keys(u"促销")  # 输入促销
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/table/tbody/tr[2]/td[3]/input").send_keys(u"123")  # 输入123
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[4]/button[2]").click()  # 点击保存
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[1]/input").click()  # 选择第一个订单
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[2]/tr[1]/td[1]/input").click()  # 选择第二个订单
		driver.find_element_by_link_text('批量标签').click()  # 点击批量标签
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/input").click()  # 选择团购
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/button[1]").click()  # 点击保存
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/from/div[2]/div[3]/input").send_keys(u"团购")  # 点击标签名称
		driver.find_element_by_xpath("//button[@ng-click='searchLogic.searchClick()']").click()  # 点击搜索按钮

		driver.find_element_by_link_text('标签设置').click()  # 点击标签设置
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/input").click()  # 选择团购
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/table/tbody/tr[2]/td[1]/div/input").click()  # 选择促销
		driver.find_element_by_xpath("//button[@ng-click='deletelist()']").click()  # 点击删除按钮
		driver.switch_to.alert.accept()
		sleep(3)
