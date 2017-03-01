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
		driver.find_element_by_css_selector('#menuSider > li.col-sider-moren.current > ul > li:nth-child(1)').click() #点击设置
		driver.find_element_by_css_selector('body > div.col01 > div.col_mian.clearfix > div.col_right > div.col_cnt > div.col_location > div.col_location_title.clearfix > div.col_location_btn').click()  # 点击添加考勤地点
		driver.find_element_by_css_selector("#tkkqbody > div > div.add_kaoq_box01 > div:nth-child(1) > div.add_kaoq_box01_input > input").send_keys(u'用友软件园考勤点')  # 输入考勤点
		driver.find_element_by_css_selector("#tkkqbody > div > div.add_kaoq_box01 > div:nth-child(2) > div.add_kaoq_dizhi_input > input").send_keys(u'用友软件园北门') # 输入详细地址
		driver.find_element_by_css_selector("div.add_kaoq_dingwei").click() #点击定位
		driver.find_element_by_css_selector("div.BMap_button.BMap_stdMpZoomIn").click()  #放大地图
		driver.find_element_by_css_selector("span.BMap_Marker.BMap_noprint").click()  #选择A
		driver.find_element_by_id("okBtn").click()  #确定
		driver.find_element_by_css_selector(".add_kaoq_fanwei_kuang").clear()  # 考勤范围清空
		driver.find_element_by_css_selector(".add_kaoq_fanwei_kuang").send_keys("1000")  # 输入考勤范围 1000
		driver.find_element_by_css_selector(".add_kaoq_riqila").click()  # 点击考勤下拉框

		driver.find_element_by_css_selector('[rolevalue="1"]').click()  # 周一
		driver.find_element_by_css_selector('[rolevalue="2"]').click()  # 周二
		driver.find_element_by_css_selector('[rolevalue="3"]').click()  # 周三
		driver.find_element_by_css_selector('[rolevalue="4"]').click()  # 周四
		driver.find_element_by_css_selector('[rolevalue="5"]').click()  # 周五
		driver.find_element_by_css_selector(".add_kaoq_fanwei_kuang").click()  #点击空白
		driver.find_element_by_css_selector('.add_kaoq_time_kuang').click()  # 时间框
		driver.find_element_by_xpath('//*[@id="tkkqbody"]/div/div[2]/div[5]/div[2]/div/div[1]/div[2]/ul/li[9]').click()  # 8点
		driver.find_element_by_xpath('//*[@id="tkkqbody"]/div/div[2]/div[5]/div[2]/div/div[2]/div[2]/ul/li[7]').click()  # 30分
		driver.find_element_by_css_selector('.add_kaoq_xtime_kuang').click()  # 下班时间框
		driver.find_element_by_xpath('//*[@id="tkkqbody"]/div/div[2]/div[6]/div[2]/div/div[1]/div[2]/ul/li[18]').click()  # 8点
		driver.find_element_by_xpath('//*[@id="tkkqbody"]/div/div[2]/div[6]/div[2]/div/div[2]/div[2]/ul/li[1]').click()  # 00分
		driver.find_element_by_css_selector('#selectTab > ul > li:nth-child(2)').click()  # 按员工
		driver.find_element_by_css_selector('#check_addPerson').click()  # 添加员工
		driver.find_element_by_css_selector('.node_name').click()  # 点击全公司
		driver.find_element_by_css_selector('[name="郑梓涛"]').click()  # 点击郑梓涛
		driver.find_element_by_css_selector('.layui-layer-btn0').click()  # 点击确定
		driver.find_element_by_css_selector('.add_yuan_btnR').click()  # 点击确定
		sleep(3)
		new = driver.find_element_by_css_selector("#row0setCheck_grid > div:nth-child(2) > div").text
		self.assertEqual(new, "用友软件园考勤点", '新增成功')
		driver.find_element_by_css_selector('.check_delete').click()  # 点击删除
		driver.find_element_by_css_selector('.delete_btn_left').click()  # 点击确定
		driver.find_element_by_css_selector("#menuSider > li:nth-child(1) > div").click()  # 点击考勤