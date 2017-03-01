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


		#driver.find_element_by_link_text(u"超客").click()  # 点击超客
		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户
		sleep(3)
		driver.find_element_by_link_text("客户字段自定义").click()  # 点击客户字段自定义
		driver.find_element_by_css_selector("#root > div > div > div > div > div > div.ant-spin-container > div > div > div > span > div.ant-table-body > table > tbody > tr:nth-child(3) > td:nth-child(5) > button").click()  # 点击设置
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-content > div:nth-child(1) > div > div > div.ck-customize-gongn01 > div > ul > li:nth-child(2) > div.ck-gongncnt-second.clearfix > button.cut').click()  # 点击"-"
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-content > div:nth-child(1) > div > div > div.ck-customize-gongn01 > div > ul > li > div.ck-gongncnt-first > input[type="text"]').clear()  #清空输入框"
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-content > div:nth-child(1) > div > div > div.ck-customize-gongn01 > div > ul > li > div.ck-gongncnt-first > input[type="text"]').send_keys(u'客户级别超客营销客户自定义自动化')  # 输入选项信息
		driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-content > div:nth-child(1) > div > div > div.ck-customize-gongn01 > div > ul > li:nth-child(1) > div.ck-gongncnt-second.clearfix > button.add").click()  # 点击‘+’号添加选项
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-content > div:nth-child(1) > div > div > div.ck-customize-gongn01 > div > ul > li:nth-child(2) > div.ck-gongncnt-first > input[type="text"]').send_keys(u'自动化测试超客自定义字段')  # 输入选项信息
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > div > div:nth-child(1) > button > span').click()  # 点击应用
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(3)').click() #点击运行中
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(2)').click()  # 点击编辑字段
		driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > div > div:nth-child(2) > button > span").click()
		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户