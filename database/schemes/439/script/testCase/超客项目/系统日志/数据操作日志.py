# coding=utf-8
from lib2to3.pgen2 import driver
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
		driver.find_element_by_css_selector("div.menu-title1.col-menu-Journal > span").click()  # 点击系统日志
		driver.find_element_by_link_text(u"数据操作日志").click()  # 点击数据操作日志
		sleep(3)
		driver.find_element_by_css_selector(".ant-input").send_keys(u"蒋启龙")
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-title > div > div.ant-col-10 > span > div").click()
		sleep(2)

		driver.find_element_by_css_selector("button.ant-btn.ant-btn-ghost").click()  # 点击导出
		driver.find_element_by_css_selector("div.ant-modal-body > span.ant-calendar-picker > span.ant-calendar-range-picker.ant-input > input.ant-calendar-range-picker-input").click()  # 点击时间
		driver.find_element_by_css_selector("body > div:nth-child(9) > div > div > div > div.ant-calendar-range-part.ant-calendar-range-left > div.ant-calendar-input-wrap > div.ant-calendar-date-input-wrap > input").send_keys(u"2016-10-01")
		driver.find_element_by_css_selector("body > div:nth-child(9) > div > div > div > div.ant-calendar-range-part.ant-calendar-range-right > div.ant-calendar-input-wrap > div.ant-calendar-date-input-wrap > input").send_keys(u"2016-10-31")
		driver.find_element_by_css_selector("body > div:nth-child(9) > div > div > div > div.ant-calendar-range-bottom > a.ant-calendar-ok-btn").click()  # 点击确定
		driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg > span").click()  # 点击导出确定
		sleep(3)
		driver.find_element_by_css_selector("div.menu-title1.col-menu-Journal > span").click()  # 点击系统日志