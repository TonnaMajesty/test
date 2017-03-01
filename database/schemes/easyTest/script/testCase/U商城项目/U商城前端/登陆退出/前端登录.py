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
		driver.delete_all_cookies()
		driver.get('http://test11.upmall.yonyouup.com')
		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[1]/a[1]').click()
		driver.find_element_by_xpath('//*[@id="uname" and @placeholder="请输入用户名"]').clear()
		driver.find_element_by_xpath('//*[@id="uname" and @placeholder="请输入用户名"]').send_keys("jql001")
		driver.find_element_by_xpath('//*[@id="password"]').clear()
		driver.find_element_by_xpath('//*[@id="password"]').send_keys("111111")
		driver.find_element_by_xpath('//*[@id="iptsingup"]').clear()
		driver.find_element_by_xpath('//*[@id="iptsingup"]').send_keys("8dXjt")
		driver.find_element_by_xpath("//*[@id='mainbody_box']/div/div/div/div/div/div[2]/div[1]/ul/li[4]/div/button").click()

