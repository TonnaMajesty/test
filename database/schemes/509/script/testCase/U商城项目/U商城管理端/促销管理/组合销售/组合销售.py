# coding=utf-8
from time import sleep

from selenium.webdriver import ActionChains

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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()  # 点击促销管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[4]/a').click()  # 点击组合销售
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a').click()  # 点击新增
		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[1]/div[2]').click()  # 点击添加商品
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click()  # 选择第一个商品
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加

		# driver.find_element_by_xpath('//div[@role="alertdialog"]').hidden(1)#隐藏窗口
		js = "document.getElementsByClassName('ngdialog ngdialog-theme-default ng-scope')[0].style.display='none';document.documentElement.style.overflowY = 'scroll'"
		driver.execute_script(js)  # 隐藏窗口
		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[1]/div[3]').click()  # 点击清除全部商品

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[4]/a').click()  # 点击组合销售
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a').click()  # 点击新增
		QQ=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/span[2]/input').send_keys(QQ)  # 活动名称输入“”
		driver.find_element_by_xpath('//*[@id="startDate"]').send_keys(u'2017-12-31 00:00:00')  # 开始时间输入“”
		driver.find_element_by_xpath('//*[@id="quitTimeChange2"]').click()  # 点击七天
		driver.find_element_by_xpath('//*[@id="quitTimeChange3"]').click()  # 点击一个月
		driver.find_element_by_xpath('//*[@id="quitTimeChange4"]').click()  # 点击三个月
		driver.find_element_by_xpath('//*[@id="quitTimeChange1"]').click()  # 点击一天
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div/div[1]/label/input').click()  # 选择整单促销
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div/div[2]/label/input').click()  # 选择包邮活动
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div/div[3]/label/input').click()  # 选择优惠券
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[8]/div/div[1]/img').click()  # 点击主商品
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click()  # 选择第一个商品
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加
		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[1]/div[2]').click()  # 点击添加商品
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[2]/tr/td[1]/span/input').click()  # 选择第二个商品
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加


		# driver.find_element_by_xpath('//div[@role="alertdialog"]').hidden()  # 隐藏窗口
		js = "document.getElementsByClassName('ngdialog ngdialog-theme-default ng-scope')[0].style.display='none';document.documentElement.style.overflowY = 'scroll'"
		driver.execute_script(js)  # 隐藏窗口


		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[1]/div/div[1]/input[2]').click()  # 选择减价
		driver.find_element_by_xpath('//*[@id="isDiscountOrFire0"]').send_keys(u'0.75')  # 输入减价“”

		WO = driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/select')
		WO.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/select/option[3]').click()  # 选择限购一件

		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[1]/div/div[3]/div/span').click()  # 点击批量修改
		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[1]/div/div[4]/div[2]/span').click()  # 点击抹分
		driver.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[1]/div/div[4]/div[1]/span').click()  # 点击抹角

		js=driver.find_element_by_xpath('//select[@ng-change="price.changePtype(item.type,item.productId)"]')
		js.find_element_by_xpath('//*[@id="product"]/div[1]/div[2]/div/div[2]/table/tbody/tr/th[7]/div/div[1]/select/option[3]').click()#选择限购一件


		driver.find_element_by_xpath('//*[@id="product"]/div[2]/div[2]/button').click()  # 点击保存
		WW = driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space20.ng-scope > div.col-xs-12 > table > tbody > tr:nth-child(1) > td:nth-child(2) > span").text
		#WW = driver.find_elements_by_xpath('//span[@ng-bind="combination.name"]')[0].text
		self.assertEqual(QQ,WW,'创建组合销售成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[6]/a[1]').click()  # 点击编辑按钮
		driver.find_element_by_xpath('//*[@id="product"]/div[2]/div[2]/button').click()  # 点击保存按钮

		sleep(3)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click(1)   #点击启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click(1)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click(1)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click(1)



		driver.find_elements_by_xpath('//a[@ng-click="logic.deleteCombinationSales($index,combination.id)"]')[0].click()  # 点击删除按钮
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定按钮
		sleep(2)
		#EE = driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space20.ng-scope > div.col-xs-12 > table > tbody > tr:nth-child(8) > td:nth-child(2) > span").text
		#EE=driver.find_elements_by_xpath('//span[@ng-bind="combination.name"]')[0].text
		self.assertNotEqual(WW,'删除成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[2]').click()  # 点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[3]').click()  # 点击进行中
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[4]').click()  # 点击已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[1]').click()  # 点击全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()  # 点击促销管理
		sleep(3)