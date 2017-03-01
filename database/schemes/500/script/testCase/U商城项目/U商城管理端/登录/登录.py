# coding=utf-8
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
		tool = utils
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
		driver.get(param.url)  # http://upmalldemo.yonyouup.com
		driver.find_element_by_class_name("reg").click()
		driver.close()
		# driver.switch_to_window(driver.window_handles[0])
		driver.switch_to.window(0)
		driver.find_element_by_xpath("//input[@name='username']").clear()
		driver.find_element_by_xpath("//input[@name='username']").send_keys(param.username)
		driver.find_element_by_xpath("//input[@name='password']").clear()
		driver.find_element_by_xpath("//input[@name='password']").send_keys(param.password)

		driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/form/div[4]/div/button").click()
		text = driver.title
		self.assertEqual(text, "U商城 企业端首页", "登录成功")
