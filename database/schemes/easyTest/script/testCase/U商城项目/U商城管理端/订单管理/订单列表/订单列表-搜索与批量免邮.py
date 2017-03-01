# coding=utf-8
import time

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
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化：param
		说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值

		自定义工具模块：tool 文件所在路径script/common/utils.py
		开发人员可根据需要自行添加新的函数
		例如：
		获取一个随机生成的字符串：number=tool.randomStr(6)

		##################################################################
		该方法内进行测试用例的编写
		'''
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark").click()  # 点击订单管理
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[2]/a").click()  # 点击订单列表
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/from/div[1]/div/div/a[1]").click()  # 点击近三个月
		driver.find_element_by_link_text("待付款").click()
		driver.find_element_by_link_text("待发货").click()
		driver.find_element_by_link_text("已发货").click()
		driver.find_element_by_link_text("已完成").click()
		driver.find_element_by_link_text("已关闭").click()
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/from/div[1]/div/div/a[7]").click()  # 点击三个月前
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/from/div[1]/div/div/a[1]").click()  # 点击近三个月
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[1]/input").click()  # 选择第一个订单
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[2]/tr[1]/td[1]/input").click()  # 选择第二个订单
		driver.find_element_by_link_text("批量免邮").click()
		time.sleep(3)
