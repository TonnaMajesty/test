# coding=utf-8
from time import sleep

from selenium.webdriver import ActionChains

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
		js = '$(".classify").show()'
		driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[1]/div/div[1]/a/img').click()  # 点击HK直邮美国商品
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="skus-select"]/ul/li/div[1]/button[2]').click()  # 点击‘+’
		driver.find_element_by_link_text('加入购物车').click()  # 点击加入购物车
		driver.find_element_by_xpath('//*[@id="GotoShoppingCart"]').click()  # 点击去购物车结算
		driver.find_elements_by_xpath('//input[@class="single_jdcheckbox"]')[-1].click()  # 选择订单
		driver.find_element_by_xpath('//span[@class="submit-btn "]').click()  # 点击去结算
		sleep(3)
		driver.find_element_by_css_selector('body > div > div.row > div.col-xs-12.main > div:nth-child(2) > div > div.osubmit > div > button').click()  # 点击提交订单
		#driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[14]/div/button').click()  # 点击提交订单
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[1]/ul/li[2]/div[1]/input').click()  # 选择微信支付
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[1]/ul/li[1]/div[1]/input').click()  # 选择畅捷支付
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[2]/span/button').click()  # 点击确认支付
		driver.back()
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[1]/ul/li[2]/div[1]/input').click()  # 点击支付宝
		driver.find_element_by_xpath('//*[@id="body1"]/dl/dd[2]/span/button').click()  # 点击确认支付
		driver.back()
		sleep(5)
