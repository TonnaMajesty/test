# coding=utf-8
# from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver import ActionChains

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
		tool  = utils

		'''
		driver.get('http://test11.upmall.yonyouup.com')
		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[1]/a[1]').click()
		driver.find_element_by_xpath('//*[@id="uname" and @placeholder="请输入用户名"]').clear()
		driver.find_element_by_xpath('//*[@id="uname" and @placeholder="请输入用户名"]').send_keys("jql001")
		driver.find_element_by_xpath('//*[@id="password"]').clear()
		driver.find_element_by_xpath('//*[@id="password"]').send_keys("111111")
		driver.find_element_by_xpath('//*[@id="iptsingup"]').clear()
		driver.find_element_by_xpath('//*[@id="iptsingup"]').send_keys("8dXjt")
		driver.find_element_by_xpath("//*[@id='mainbody_box']/div/div/div/div/div/div[2]/div[1]/ul/li[4]/div/button").click()

		# right_click = driver.find_element_by_xpath('//*[@id="category"]/div')
		# ActionChains(driver).move_to_element(right_click).perform()  # 悬停于商品分类
		right_click = driver.find_element_by_xpath('//*[@id="category"]/div');
		ActionChains(driver).move_to_element(right_click).perform();  # 悬停于商品分类
		sleep(2)
		right_click = driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/a')
		ActionChains(driver).move_to_element(right_click).perform()  # 悬停于办公用纸
		sleep(2)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[2]/div/div[1]/a/img').click()  # 点击商品
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[4]').click()  # 点击购买咨询
		driver.find_element_by_xpath('//*[@id="pointType"]/input[1]').click()  # 选择商品咨询
		driver.find_element_by_xpath('//*[@id="consultationContent"]').send_keys(u'这个商品如果团购可以打几折？')  # 输入咨询内容
		driver.find_element_by_xpath('//*[@id="publishedConsulting"]/ul/li[3]/button').click()  # 点击提交按钮
		driver.switch_to_alert().accept()  # 接受警告框
		driver.find_element_by_xpath('//*[@id="pointType"]/input[1]').click()  # 选择商品咨询
		driver.find_element_by_xpath('//*[@id="consultationContent" and @placeholder="请输入要咨询的内容"]').send_keys(u'这个商品如果团购可以打几折？')  # 输入咨询内容
		driver.find_element_by_xpath('//*[@id="publishedConsulting"]/ul/li[3]/button').click()  # 点击提交按钮
		driver.switch_to_alert().accept()  # 接受警告框
		driver.get('http://upmalldemo.yonyouup.com')
		driver.find_element_by_class_name("reg").click()
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark').click()  # 点击订单管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[6]/a').click()  # 点击咨询列表
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[2]').click()  # 点击商品咨询
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[3]').click()  # 点击配送咨询
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[4]').click()  # 点击售后咨询
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[1]').click()  # 点击全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/a[2]').click()  # 点击未回复
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/a[3]').click()  # 点击已回复
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/a[1]').click()  # 点击全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/a[1]').click()  # 点击详情

		element = driver.find_element_by_xpath('//*[@id="ngdialog1"]')
		driver.execute_script('$(arguments[0]).hide()', element)
		'''
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/a").click()  # 点击首页
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark').click()  # 点击订单管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[6]/a').click()  # 点击咨询列表
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/a[3]').click()  # 点击回复
		# driver.find_element_by_css_selector('#ngdialog2 > div.ngdialog-content > div:nth-child(1) > div.modal-body > div:nth-child(6) > textarea').send_keys('满意么？有需要的随时联系我们，生活愉快！')##输入卖家回复内容
		# driver.find_element_by_xpath('//*[@id="ngdialog4"]/div[2]/div[1]/div[2]/div[7]/div/a').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/a[2]').click()  # 点击删除按钮
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/span/input').click()  # 选择第一个咨询
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/a').click()  # 点击批量删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		#driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/nav/ul/li[4]/a/span').click()  # 点击下一页
		#driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/nav/ul/li[1]/a/span').click()  # 点击上一页
