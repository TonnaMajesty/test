# coding=utf-8
from time import sleep

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user

		driver.find_element_by_link_text('首页').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark','促销管理').click()  # 点击促销管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[7]/a','包邮活动').click()#点击包邮活动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a','新增活动').click()#点击新增活动
		Q1=tool.randomStr(6,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/form/div[2]/div/input').send_keys(Q1)#输入活动名称
		driver.find_element_by_xpath('//*[@id="pStartDate"]','开始时间').send_keys('2017-08-31 00:00:00')#输入开始时间
		driver.find_element_by_xpath('//*[@id="pEndDate"]','结束时间').send_keys('2017-09-30 00:00:00')#输入结束时间
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/form/div[4]/div/input','消费满多少钱').send_keys('500')#输入消费满多少钱
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/form/div[5]/div/input[2]','选择指定地区').click()#选择指定地区不包邮
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/form/div[5]/div/input[1]').click()#选择所有地区
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/form/div[7]/div/button[2]').click(2)#点击保存按钮

		#断言
		QW = driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space20.ng-scope > div.col-xs-12 > table > tbody > tr:nth-child(5) > td:nth-child(2) > span').text
		self.assertEqual(Q1,QW,'创建包邮活动成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[8]/a[1]').click()#点击编辑按钮
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/form/div[7]/div/button[2]').click(2)#点击保存按钮

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr/td[7]/div').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr/td[7]/div').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr/td[7]/div').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr/td[7]/div').click()# 启动状态

		driver.find_elements_by_xpath('//a[@ng-click="logic.deletePostActivity($index,postActivity.id)"]')[-1].click()#点击删除按钮
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击确定

		#断言
		EW = driver.find_elements_by_xpath('//span[@ng-bind="postActivity.pName"]')[-1].text
		self.assertNotIn(Q1,EW,'删除成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[2]').click()#点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[3]').click()  # 点击进行中
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[4]').click()  # 点击已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[1]').click()  # 点击全部
		sleep(3)
