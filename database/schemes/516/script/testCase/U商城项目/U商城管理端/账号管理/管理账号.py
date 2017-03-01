# coding=utf-8
import time

from selenium.webdriver import ActionChains

from SRC.common import utils_user
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
		tool = utils_user


		driver.find_element_by_css_selector('.userMsgDiv').show()
		driver.find_element_by_link_text(u"账号管理").click()
		driver.find_element_by_link_text(u"账号管理").click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/form/div[3]/div/input').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/form/div[3]/div/input').send_keys(u'萧十一郎')#输入姓名“”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/form/div[10]/div[2]/button').click()#点击保存
		driver.find_element_by_xpath('//a[@ng-href="#useravater"]').click()#点击更改头像
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/ul/li[4]/img').click()#选择头像
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button').click()#点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/a').click()#点击账号安全
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[5]/a').click()#点击修改
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[1]/div/input').send_keys(u'111111')#输入原密码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[2]/div/input').send_keys(u'123456')#输入新密码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/div/input').send_keys(u'123456')#输入确认密码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击保存
		driver.find_element_by_name('password').send_keys(123456)#输入密码
		driver.find_element_by_xpath('//button[@class="btn btn-default btn-block "]').click()#点击登录

		driver.find_element_by_css_selector('.userMsgDiv').show()
		driver.find_element_by_link_text(u"账号管理").click()
		driver.find_element_by_link_text(u"账号管理").click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/a').click()  # 点击账号安全
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[5]/a').click()  # 点击修改
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[1]/div/input').send_keys(u'123456')  # 输入原密码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[2]/div/input').send_keys(u'111111')  # 输入新密码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/div/input').send_keys(u'111111')  # 输入确认密码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击保存
		driver.find_element_by_xpath('//*[@id="password"]').send_keys(u'111111')#输入密码
		driver.find_element_by_xpath('//button[@class="btn btn-default btn-block "]').click()  # 点击登录



		'''
		driver.find_element_by_xpath('//a[@href="javascript:void(0);return false;"]').hover(2)
		driver.find_element_by_xpath('//a[@href="/Users/account#userbase"]').click()  # 点击账号管理
		driver.find_element_by_xpath('//a[@ng-href="#usersafe"]').click()  # 点击账号安全
		driver.find_element_by_xpath('//a[@ng-click="checkPhone()"]').click()#点击手机验证后面修改
		driver.find_element_by_xpath('//*[@id="txtCheckCode"]').send_keys('')#输入验证码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/div[2]/button').click()#点击获取校验码
		driver.find_element_by_xpath('//*[@id="txtReviewCode"]').send_keys('')#输入校验码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击保存

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[3]/div[5]/a').click()  # 点击邮箱验证后面的立即验证
		driver.find_element_by_xpath('//*[@id="txtcontactEmail"]').send_keys('')  # 输入邮箱
		driver.find_element_by_xpath('//*[@id="txtCheckCode"]').send_keys('')  # 输入验证码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/div[2]/button').click()  # 点击获取校验码
		driver.find_element_by_xpath('//*[@id="txtReviewCode"]').send_keys('')  # 输入校验码
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击保存

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[4]/div[4]/a').click()#点击找回密码
		driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys('')#输入账号
		driver.find_element_by_xpath('//*[@id="txtCheckCode"]').send_keys('')#输入验证码
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[4]/div/button').click()#点击下一步
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div[2]/button').click()#点击获取校验码
		driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys('')#输入校验码
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[5]/div/button').click()#点击下一步

		driver.find_element_by_xpath('').send_keys('')#输入新密码
		driver.find_element_by_xpath('').send_keys('')  # 输入确认新密码
		driver.find_element_by_xpath('').click()  # 点击保存
		'''





