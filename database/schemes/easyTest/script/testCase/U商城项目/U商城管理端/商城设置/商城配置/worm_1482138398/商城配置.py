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
		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[1]/upmark').click();  # 点击商城设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[4]/a').click();  # 点击商城配置
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click();  # 点击确定
		driver.find_element_by_xpath('//*[@id="tablist"]/form/div[1]/div[1]/div[1]/input[1]').click();  # 选择是
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click();  # 点击确定
		driver.find_element_by_xpath('//*[@id="tablist"]/form/div[1]/div[4]/div[1]/input[2]').click();  # 选择储值卡否
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click();  # 点击确定
		driver.find_element_by_xpath('//*[@id="tablist"]/form/div[1]/div[4]/div[1]/input[1]').click();  # 选择储值卡是
		driver.find_element_by_xpath('//*[@id="sub_btn"]').click();  # 点击确定
		sleep(3)
		