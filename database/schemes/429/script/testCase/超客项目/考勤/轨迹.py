# coding=utf-8
from time import sleep, time

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils

class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user

		driver.find_element_by_css_selector("#menuSider > li:nth-child(1) > div").click()  # 点击考勤
		driver.find_element_by_link_text(u'轨迹').click()  # 点击轨迹
		sleep(4)
		# 选择客户
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-main > div.check-trails-col01 > div:nth-child(3) > div.check-trails-btn01 > button").click() #点击选择客户
		driver.find_element_by_xpath('//input[@placeholder="请输入客户名称"]').send_keys(u"新客户") #输入新客户
		driver.find_element_by_xpath('//div[@class="ant-input-group-wrap"]').click() #点击搜索
		driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.select-owner > div > div.ant-col-11 > label > span.ant-checkbox").click()
		#driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.account-list > div > ul > li:nth-child(3) > div.check-trails-pop-gs > label > span.ant-checkbox > input[type="checkbox"]').click() #勾选
		driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button:nth-child(2)").click() #确定

		# 人员范围
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-main > div.check-trails-col01 > div:nth-child(1) > div.check-trails-btn01 > button").click() #点击选择人选
		driver.find_element_by_css_selector('body > div:nth-child(9) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div.searchContent > span:nth-child(2) > span > input[type="text"]').send_keys(u"郑梓涛") #输入搜索
		driver.find_element_by_css_selector("body > div:nth-child(9) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div.searchContent > span:nth-child(2) > button").click() #点击搜索
		driver.find_element_by_css_selector('body > div:nth-child(9) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div.PopBox_OperateCnt > div.PopBox_selectResult > div.PopBox_selectPerson > ul > li > label > span > input[type="checkbox"]').click() #勾选
		driver.find_element_by_css_selector('body > div:nth-child(9) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button:nth-child(2)').click()  #确定
		#选择日期
		driver.find_element_by_css_selector('#root > div > div > div.ck-root-main > div.check-trails-col01 > div:nth-child(2) > div.check-trails-time01 > div > span:nth-child(1) > span > input').click()  #开始日期
		driver.find_element_by_css_selector(".ant-calendar-input").send_keys(u"2016-10-01")
		driver.find_element_by_css_selector('#root > div > div > div.ck-root-main > div.check-trails-col01 > div:nth-child(2) > div.check-trails-time01 > div > span:nth-child(3) > span > input').click()  # 结束日期
		driver.find_element_by_css_selector(".ant-calendar-input").send_keys(u"2016-10-30")
		#勾选
		driver.find_element_by_css_selector('#root > div > div > div.ck-root-main > div.check-trails-col01 > div:nth-child(4) > div.check-trails-types > div > label > span.ant-checkbox > input').click()  # 勾选
		driver.find_element_by_css_selector('[data-reactid=".0.0.0.0.4.0.1:$/=10"]').click()  # 点确定
		driver.find_element_by_css_selector('#root > div > div > div.ck-root-main > div.check-trails-col02 > div.check-trail-tit01.clearfix > div:nth-child(5) > button > span').click()  # 点导出
		sleep(4)
		driver.find_element_by_css_selector("#menuSider > li:nth-child(1) > div").click()  # 点击考勤