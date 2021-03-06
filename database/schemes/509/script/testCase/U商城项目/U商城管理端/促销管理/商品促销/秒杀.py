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

		driver.find_element_by_link_text('首页').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()#点击促销管理
		sleep(2)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[3]/a').click()#点击商品促销
		driver.find_element_by_xpath('//a[@href="/promotion/ProductPreferentialController/index?menuid=44"]').click()#点击新增活动
		driver.find_element_by_xpath('//input[@placeholder="请输入活动名称"]').send_keys(tool.randomStr(6,lowerCaseLetter=True))  # 活动名称输入“”
		driver.find_element_by_xpath('//input[@ng-checked="productPreferential.isSpikeMode"]').click()#选择启用秒杀模式
		driver.find_element_by_xpath('//*[@id="getSpikeLabelType"]/input').click()#选择标签图片
		driver.find_element_by_xpath('//input[@placeholder="请输入开始日期"]').send_keys(u"2016-12-30")  # 输入开始日期
		driver.find_element_by_id('quitTimeChange4').click()  # 点击3个月
		driver.find_element_by_xpath('//div[@ng-click="selectProduct()"]').click()  # 点击添加商品
		driver.find_elements_by_xpath('//span[@ng-bind="product.cName"]')[1].click()  # 选择第一个商品
		# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[2]/tr/td[1]/span/input').click()  # 选择第二个商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加

		js = "document.getElementsByClassName('ngdialog ngdialog-theme-default ng-scope')[0].style.display='none';document.documentElement.style.overflowY = 'scroll'"
		driver.execute_script(js)  # 隐藏窗口

		ws=driver.find_element_by_xpath('//select[@ng-change="price.changeAllPtype(productPreferential.allPtype)"]')
		ws.find_element_by_xpath('//*[@id="entialAllPtype"]/option[4]').click()#选择限购一件
		driver.find_element_by_xpath('//input[@id="isDiscountOrFire0"]').send_keys('1')#输入打折金额

		driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div/div[1]/div/div[2]/div[1]/span').click()  # 点击批量修改
		driver.find_element_by_class_name('savebtn').click(1)  # 点击保存
		sleep(3)
		'''
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[8]/li[1]/upmark').click()#点击站点设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[8]/li[2]/a').click()#点击模板管理
		sleep(3)
		driver.find_element_by_xpath('//a[@ng-href="/corp/Template/pagelist?menuid=71&templatelistid=820&Type=L"]').click()#点击页面
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space10 > div > table > tbody > tr:nth-child(2) > td.text-center > a:nth-child(1)').click()#点击布局
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		sleep(3)
		driver.find_element_by_xpath('//*[@id="12"]/div/span').click()#点击商品列表编辑

		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-body > div > div:nth-child(3) > div > div:nth-child(3) > input').click()#选择秒杀活动列表
		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-body > div > div:nth-child(6) > div.selectGroupgood > div > div > div:nth-child(4) > input').click()#点击全部
		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-footer > button').click()#点击保存
		driver.find_element_by_css_selector('#container > nav > div:nth-child(1) > form > button.btn.btn-info.btn-submit').click()#点击保存布局/版本
		sleep(5)
		'''

		# ele=driver.find_element_by_xpath('')
		# ele.ISNULLELEMENT=True
		# ele.ISNULLELEMENT=False
		# self.assertTrue(ele.ISNULLELEMENT,msg='不是空元素')