# coding=utf-8
import sys
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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[1]/upmark').click()  # 点击物流管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[2]/a').click()  # 点击物流公司
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()  # 点击新增
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[1]/div/input').send_keys(u'芬奇物流')  # 输入物流公司名称
		wk = driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[2]/div/select')
		wk.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[2]/div/select/option[1]').click()  # 选择自定义
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[3]/div/input').send_keys(u'fenqi')  # 输入物流公司代码
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[6]/div/div/div/div/span[2]').click()  # 选择是
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[6]/div/div/div/div/span[2]').click()  # 选择否
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[7]/div/input').send_keys(u'1')  # 排序输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[3]/div/button[2]').click()  # 点击确定
		driver.find_element_by_xpath('//a[@ng-click="logic.edit(deliveryCorp)"]').click()  # 点击编辑
		# driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[6]/div/div/div/div/span[2]').click()  # 选择是
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[3]/div/button[2]').click()  # 点击确定
		driver.find_element_by_xpath('//a[@ng-click="logic.deleteDlyCorp($index,deliveryCorp.id)"]').click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)
		
