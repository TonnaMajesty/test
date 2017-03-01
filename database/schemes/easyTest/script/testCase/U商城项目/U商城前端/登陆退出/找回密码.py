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
		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[1]/a[1]').click()  # 点击请登录
		driver.find_element_by_xpath('//*[@id="forget_password"]').click()  # 点击忘记密码
		driver.find_element_by_xpath('//*[@id="username"]').send_keys(u'nan456')  # 输入账户名
		driver.find_element_by_xpath('//*[@id="valAuthCode"]').send_keys(u'uguyz')  # 输入验证码
		driver.find_element_by_xpath('//*[@id="forget_password_btn_step1"]').click()  # 点击提交按钮
		driver.find_element_by_xpath('//*[@id="sendMobileCode"]').click()  # 点击获取短信校验码
		driver.find_element_by_xpath('//*[@id="messageValCode"]').send_keys(u'123455')  # 输入手机校验码
		driver.find_element_by_xpath('//*[@id="forget_password_btn_step2"]').click()  # 点击提交
		driver.find_element_by_xpath('//*[@id="password"]').send_keys(u'333333')  # 输入新密码
		driver.find_element_by_xpath('//*[@id="repassword"]').send_keys(u'333333')  # 输入确认新密码
		driver.find_element_by_xpath('//*[@id="forget_password_btn_step3"]').click()  # 点击提交
