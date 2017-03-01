# coding=utf-8
from time import sleep, time

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils

class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user
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
		driver.get("http://esn.ren")
		title = driver.title
		self.assertEqual(title, '用友企业空间-社交化移动办公平台-企业级SAAS首选品牌', '跳转异常')
		driver.find_element_by_link_text(u"登录").click()
		driver.find_element_by_id("usernameId").clear()
		driver.find_element_by_id("usernameId").send_keys("18500738046")
		driver.find_element_by_id("passwordId").clear()
		driver.find_element_by_id("passwordId").send_keys("111111")
		driver.find_element_by_id("loginId").click()
		title1 = driver.title
		self.assertEqual(title1, '首页--脚本环境--企业空间', '跳转异常')

		driver.find_element_by_link_text(u"超客").click()  # 点击超客
		driver.find_element_by_css_selector("#menuSider > li:nth-child(1) > div").click()  # 点击考勤