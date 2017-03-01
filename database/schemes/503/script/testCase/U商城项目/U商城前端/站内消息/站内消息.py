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
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[2]/div').click()  # 点击HK直邮美国商品
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="product-detail"]/div/div[2]/div/div[3]/div[2]/a[2]/span').click()  # 点击立即订购
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div/div[14]/div/button').click()  # 点击提交订单

		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[1]/a').click()  # 点击站内消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/a').click()  # 点击设置
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/input').click()  # 点击优惠券到账
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/input').click()  # 点击优惠券过期
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/a').click()  # 点击返回我的消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[2]').click()  # 点击订单消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[3]').click()  # 点击账户消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[4]').click()  # 点击系统消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[1]').click()  # 点击所有消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/ul/li[2]').click()  # 点击已读消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[2]').click()  # 点击订单消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[3]').click()  # 点击账户消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[4]').click()  # 点击系统消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/ul/li[1]').click()  # 点击所有消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/ul/li[1]').click()  # 点击新消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[4]/div[2]/div[2]/span[3]').click()  # 点击下一页
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[4]/div[2]/div[2]/span[1]').click()  # 点击上一页
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[4]/div[1]/div[1]/div[1]/input').click()  # 选择第一个消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[4]/div[2]/div[1]/button[1]').click()  # 点击标记为已读
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/ul/li[1]').click()  # 点击新消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[4]/div[1]/div[1]/div[1]/input').click()  # 选择第一个订单消息
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[4]/div[2]/div[1]/button[2]').click() # 点击删除
		sleep(3)
