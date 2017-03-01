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
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click();  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[6]/ul/li[2]/a/span').click();  # 点击我的咨询

		# 查看我的评价
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[4]/ul/li[3]/a/span').click();  # 点击我的评价
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div[1]/div[1]/button[1]').click();  # 点击评论
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div/ul/li[5]').click();  # 点击评分
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div/textarea').send_keys(u'很好很好很嗨很嗨很不错');  # 输入评价心得
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[5]/div[2]/input').click();  # 勾选匿名
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[5]/button').click();  # 点击评价并继续
		sleep(3)