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
		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[2]/a').click()  # 点击退出
		driver.find_element_by_xpath('//a[@href="/register"]','免费注册').click()#点击免费注册
		driver.find_element_by_xpath('//*[@id="reg_user"]').send_keys('yonyou000')#输入用户名
		driver.find_element_by_xpath('//*[@id="reg_passwd"]').send_keys('111111')#输入密码
		driver.find_element_by_xpath('//*[@id="reg_passwd_r"]').send_keys('111111')#输入确认密码
		driver.find_element_by_xpath('//*[@id="mobile"]').send_keys('13787878787')#输入验证手机
		driver.find_element_by_xpath('//*[@id="messageAuthenticationCode"]').send_keys('123456')#输入短信验证码
		driver.find_element_by_xpath('//*[@id="iptsingup"]').send_keys('654321')#输入验证码
		driver.find_element_by_xpath('//*[@id="submit-btn"]/span/span').click()#点击注册按钮