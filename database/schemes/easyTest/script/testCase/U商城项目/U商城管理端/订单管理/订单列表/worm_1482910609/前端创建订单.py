# coding=utf-8
from time import sleep

from selenium.webdriver import ActionChains

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
		tool  = utils
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化：param
		说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值

		自定义工具模块：tool 文件所在路径script/common/utils.py
		开发人员可根据需要自行添加新的函数
		例如：
		获取一个随机生成的字符串：number=tool.randomStr(6)

		##################################################################
		该方法内进行测试用例的编写
		'''
		right_click = driver.find_element_by_xpath('//*[@id="category"]/div');
		ActionChains(driver).move_to_element(right_click).perform();  # 悬停于商品分类
		sleep(2)
		right_click = driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/a')
		ActionChains(driver).move_to_element(right_click).perform()  # 悬停于办公用纸
		sleep(2)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[2]/div').click();  # 点击HK直邮美国商品
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="product-detail"]/div/div[2]/div/div[2]/div[2]/a[2]/span').click();  # 点击立即订购
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[14]/div/button').click();  # 点击提交订单
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[14]/div/button').click();  # 点击提交订单
		sleep(3)