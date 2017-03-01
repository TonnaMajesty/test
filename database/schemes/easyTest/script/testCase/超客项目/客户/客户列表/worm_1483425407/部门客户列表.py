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

		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户
		sleep(3)
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(4) > h4').click()  # 点击客户列表
		driver.find_element_by_link_text("部门客户列表").click()  # 点击部门客户表
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(3) > div").click()  # 点击负责的客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(4) > div").click()  # 点击重点客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(5) > div").click()  # 点击关注的客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(6) > div").click()  # 点击冻结客户
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(2) > div").click()  # 点击全部客户
		driver.find_element_by_css_selector("#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr:nth-child(3) > td.ant-table-selection-column > span > label > span > input").click() #选择客户
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-title > div > div.ant-col-14.ant-col-offset-2 > div.cklist-PersonChange > button > span").click()  # 变更负责人
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > ul > li:nth-child(2)').click() #选择郑梓涛
		driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > div > button.ant-btn.ant-btn-primary > span").click() #点击确定

		sleep(3)
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(3) > div").click()  # 点击负责的客户
		driver.find_element_by_css_selector('#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr:nth-child(3) > td.ant-table-selection-column > span > label > span > input').click() #勾选客户
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-title > div > div.ant-col-14.ant-col-offset-2 > div.cklist-PersonChange > button > span").click()  # 变更负责人
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > ul > li:nth-child(1) > a > img').click() #选择蒋启龙
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > div > button.ant-btn.ant-btn-primary > span').click()  #点击确定

		sleep(3)
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(4) > div").click() # 点击重点客户
		driver.find_element_by_css_selector('#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr > td.ant-table-selection-column > span > label > span > input').click() #勾选郑梓涛
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-title > div > div.ant-col-14.ant-col-offset-2 > div.cklist-PersonChange > button > span").click()  # 变更负责人
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > ul > li:nth-child(1) > a > img').click() #选择蒋启龙
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > div > button.ant-btn.ant-btn-primary > span').click()  # 点击确定

		sleep(3)
		driver.find_element_by_css_selector("#root > div > div > div.ant-tabs.ant-tabs-top.ant-tabs-card > div.ant-tabs-bar > div > div > div > div > div:nth-child(5) > div").click()  # 点击关注的客户
		driver.find_element_by_css_selector('#root > div > div > div.QueryDataTable > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div > span > div > table > tbody > tr > td.ant-table-selection-column > span > label > span > input').click()  # 勾选蒋启龙
		driver.find_element_by_css_selector("#root > div > div > div.ck-root-title > div > div.ant-col-14.ant-col-offset-2 > div.cklist-PersonChange > button > span").click()  # 变更负责人
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > ul > li:nth-child(2) > a > img').click()  # 选择郑梓涛
		driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > div > button.ant-btn.ant-btn-primary > span').click()  # 点击确定
		sleep(5)
		driver.find_element_by_css_selector("#menuSider > li:nth-child(5) > div").click()  # 点击客户