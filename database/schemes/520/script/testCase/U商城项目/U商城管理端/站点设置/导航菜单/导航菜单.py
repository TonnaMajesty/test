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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(3) > a').click() #点击导航菜单
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()#点击新增
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(u'旅游穿衣')#输入菜单名称
		jf=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/select')
		jf.find_element_by_xpath('//option[@label="主页"]').click()#选择主页
		driver.find_element_by_xpath('//input[@name="4"]').click()#选择是
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/button[2]').click()#点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[6]/a[1]').click()#点击修改
		jg=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/select')
		jg.find_element_by_xpath('//option[@label="会员中心"]').click()#选择会员中心
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/button[2]').click()#点击确定
		sleep(3)
		driver.find_elements_by_xpath('//a[@ng-click="enterFront(menu)"]')[-4].click(2)#点击进入
		driver.switch_to_window(driver.window_handles[1])
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		sleep(3)
		driver.find_elements_by_xpath('//a[@ng-click="logic.deleteMenu($index,menu.id)"]')[-4].click()#点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击确定
		sleep(3)