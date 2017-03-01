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
		driver.find_element_by_xpath('//*[@id="search"]/div/div[1]/input').clear()
		driver.find_element_by_xpath('//*[@id="search"]/div/div[1]/input').send_keys(u'广博（GuangBo）PA18353V 35页粘胶型相册影集/相簿');  # 在搜索栏输入“广博（GuangBo）PA18353V 35页粘胶型相册影集/相簿”
		driver.find_element_by_xpath('//*[@id="search"]/div/div[1]/button').click();  # 点击搜索
		sleep(3)