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
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[1]/a').click()  # 点击站内消息
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[4]/ul/li[1]/a/span').click()  # 点击我的订单
		driver.find_element_by_xpath('//*[@id="recivedproduct"]').click()  # 点击待收货
		driver.find_element_by_xpath('//*[@id="orderList"]/table/tbody/tr[2]/td[8]/div[1]/a').click()  # 点击确认收货
		driver.find_element_by_xpath('//*[@id="modalSure"]').click()  # 点击确定
		sleep(5)

		# 评价
		driver.find_element_by_xpath('//*[@id="goremark"]').click()  # 点击待评价
		driver.find_element_by_xpath('//*[@id="orderList"]/table/tbody/tr[2]/td[5]/div[2]/a').click()  # 点击立即评论
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_elements_by_xpath('//button[@class="col-md-2 evaluation_btn"]')[0].click()  # 点击评论
		driver.find_elements_by_xpath('//li[@class="five"]')[0].click()  # 点击评星
		driver.find_elements_by_xpath('//textarea[@class="textarea textarea01"]')[0].send_keys(u'还可以很好不错就那样')  # 输入评价内容
		driver.find_elements_by_xpath('//button[@class="col-md-2 evaluationBtn"]')[0].click() # 点击评价并继续
		driver.find_element_by_css_selector('body > div > div.row > div.col-md-10.main.myEvaluation > div.col-md-12.main_tabs > ul > li:nth-child(2)').click()  # 查看评价
		sleep(5)