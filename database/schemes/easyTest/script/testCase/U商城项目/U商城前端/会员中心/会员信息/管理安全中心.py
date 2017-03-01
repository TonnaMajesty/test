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
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click()  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[7]/ul/li[3]/a/span').click()  # 点击安全中心
		driver.find_element_by_xpath('//span[@id="updatePassword"]').click()  # 点击登录密码后的修改
		driver.back()
		sleep(2)
		driver.find_element_by_xpath('//*[@id="valMail"]').click()  # 点击邮箱绑定后的立即绑定
		driver.back()
		sleep(2)
		driver.find_element_by_xpath('//*[@id="valPhone"]').click()  # 点击手机绑定后的修改
		driver.back()
		sleep(3)