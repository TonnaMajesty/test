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
		driver.find_element_by_css_selector('.cart').click()  # 点击加入购物车
		sleep(2)
		js = '$(".classify").show()'
		driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[4]/div/div[1]/a/img').click()  # 点击香港直邮美国
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.find_element_by_css_selector('.cart').click()  # 点击加入购物车
		driver.find_element_by_xpath('//*[@id="cart_box"]/div/div/div[1]/span[2]').click()  # 点击购物车
		driver.find_element_by_xpath('//*[@id="cart-list"]/div/div/div[2]/div[1]/div/div/div/div[7]/span[1]').click()  # 点击删除
		driver.switch_to_alert().accept()  # 接受警告框

		# right_click = driver.find_element_by_xpath("//div[@id='cart_box']//ul[1]")
		# ActionChains(driver).move_to_element(right_click).click_and_hold().perform()  # 悬停于购物车
		# driver.execute_script("arguments[0].style.display='block'", right_click)
		driver.find_element_by_xpath("//div[@id='cart_box']//ul[1]").show()
		sleep(2)
		# driver.find_element_by_xpath('//*[@id="cart_box"]/div/ul/li[2]/div/span[1]').click()  # 点击清空
		driver.find_element_by_class_name('clear_cart').click()  # 点击清空
		driver.switch_to_alert().accept()  # 接受警告框
		sleep(3)
