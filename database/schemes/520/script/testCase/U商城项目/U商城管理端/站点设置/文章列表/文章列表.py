# coding=utf-8
from time import sleep

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

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li.title.pointer').click()  # 点击站点设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(9) > a').click()  # 点击文章列表
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/a').click()  # 点击新增
		driver.find_element_by_xpath('//input[@ng-model="articleBody.articleIndex.title"]').send_keys(u'猴子爱偷桃')  # 输入文章标题

		driver.find_element_by_xpath('//input[@ng-model="model[setting.namekey]"]').click(2) #点击文章节点
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/div/div/ul/li[1]/div/span[2]').click(2)#选择帮助中心
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/div/div/ul/li[1]/ul/li/div/span[1]').click(2)
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/div/div/ul/li[1]/ul/li/ul/li/div/span[2]').click(2)#点击张倩

		driver.find_element_by_xpath('//button[@class="btn btn-default btn-lg"]').click(3)  # 点击保存
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div.row.space10 > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)').click()#点击编辑
		# driver.find_elements_by_xpath('''//a[@ng-click="checkAuth('070803','/corp/Articles/edit?menuid=78&id=' + articleindex.id)"]''')[-3].click();  # 点击编辑
		driver.find_element_by_xpath('//input[@ng-model="articleBody.articleIndex.title"]').send_keys(u'猴子爱偷桃zi')  # 输入文章标题
		driver.find_element_by_xpath('//button[@class="btn btn-default btn-lg"]').click(5)  # 点击保存
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div.row.space10 > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(2)').click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)