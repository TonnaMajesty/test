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
		sleep(3)
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[2]/div').click();  # 点击HK直邮美国商品
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="skus-select"]/ul/li/div[1]/button[2]').click()  # 点击选择商品数量
		driver.find_element_by_css_selector('.cart').click()  # 点击加入购物车
		driver.back()
		driver.find_element_by_css_selector('.collect').click()  # 点击收藏商品
		driver.switch_to.alert.accept()  # 接受警告框
		driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[1]/a').click()  # 点击商品详情
		driver.find_element_by_xpath('//*[@id="profile1"]/a').click()  # 点击商品评论
		driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[4]/a').click()  # 点击购买咨询
		driver.find_element_by_xpath('//*[@id="consulting"]/div[1]/div/a').click()  # 点击发表咨询
		driver.find_element_by_xpath('//*[@id="consultationContent" and @placeholder="请输入要咨询的内容" ]').send_keys(u'山核桃还是人工种植的核桃')  # 输入咨询内容
		driver.find_element_by_xpath('//*[@id="pointType"]/input[1]').click()  # 选择商品咨询
		driver.find_element_by_xpath('//*[@id="publishedConsulting"]/ul/li[3]/button').click()  # 点击提交
		driver.switch_to.alert.accept()  # 接受警告框
		sleep(3)