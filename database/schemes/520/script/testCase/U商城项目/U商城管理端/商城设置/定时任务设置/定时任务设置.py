# coding=utf-8
from time import sleep

from SRC.common import utils_user
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
		tool  = utils_user

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li.title.pointer').click()  # 点击商城设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li:nth-child(7) > a').click()   # 点击定时任务
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[8]/a').click()#点击第一行配置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[4]/div/label[2]/input').click()#选择未启动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[4]/div/label[1]/input').click()  # 选择启动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[1]/input[1]').click()#选择一次
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[1]/input[4]').click()#选择天
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[1]/input[5]').click()#选择周
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[1]/input[6]').click()#选择月
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[1]/input[2]').click()  # 选择分钟
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[6]/input').clear()
		TM='3'+tool.randomStr(1,number=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[6]/input').send_keys(TM)#输入每隔时间
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/button[2]').click()#点击确定
		sleep(3)

		YZ=driver.find_elements_by_xpath('//span[@ng-bind="job.taskstarttime"]')[0].text
		self.assertIn(TM,YZ,'设置成功')
		sleep(3)
