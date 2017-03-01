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
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值
		##################################################################
		该方法内进行测试用例的编写
		'''
		driver.find_element_by_link_text('首页').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()  # 点击促销管理

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[3]/a').click()  # 点击商品促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a').click()  # 点击新增活动
		driver.find_element_by_xpath('//*[@id="product"]/div/div[1]/div[2]').click()  # 点击添加商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click()  # 选择第一个商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[2]/tr/td[1]/span/input').click()  # 选择第二个商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加

		js = "document.getElementsByClassName('ngdialog ngdialog-theme-default ng-scope')[0].style.display='none'"
		driver.execute_script(js)  # 隐藏窗口

		driver.find_element_by_xpath('//*[@id="product"]/div/div[1]/div[3]').click()  # 点击清除全部商品


		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[3]/a').click()  # 点击商品促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a').click()  # 点击新增活动
		W2=tool.randomStr(6,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//input[@placeholder="请输入活动名称"]').send_keys(W2)  # 活动名称输入“”
		driver.find_element_by_xpath('//input[@placeholder="请输入开始日期"]').send_keys(u"2016-12-30")  # 输入开始日期
		driver.find_element_by_id('quitTimeChange1').click()  # 点击1天
		driver.find_element_by_id('quitTimeChange2').click()  # 点击7天
		driver.find_element_by_id('quitTimeChange3').click()  # 点击1个月
		driver.find_element_by_id('quitTimeChange4').click()  # 点击3个月
		driver.find_element_by_id('quitTimeChange1').click()  # 点击1天
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[7]/div/div[1]/label/input').click()  # 选择整单促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[7]/div/div[2]/label/input').click()  # 选择包邮活动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[7]/div/div[3]/label/input').click()  # 选择优惠券
		driver.find_element_by_xpath('//*[@id="product"]/div/div[1]/div[2]').click()  # 点击添加商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click() # 选择第一个商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[2]/tr/td[1]/span/input').click() # 选择第二个商品
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加

		js = "document.getElementsByClassName('ngdialog ngdialog-theme-default ng-scope')[0].style.display='none';document.documentElement.style.overflowY = 'scroll'"
		driver.execute_script(js)  # 隐藏窗口

		driver.find_element_by_xpath('//*[@id="isDiscountOrFire0"]').send_keys(u"1")  # 打折输入“”
		driver.find_element_by_xpath('//*[@id="entialAllPtype"]').click()  # 点击限购
		driver.find_element_by_xpath('//*[@id="entialAllPtype"]/option[4]').click()  # 点击限购三件
		driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div/div[1]/div/div[2]/div[1]/span').click()  # 点击批量修改
		driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div/div[1]/div/div[2]/div[2]/span').click()  # 点击抹角
		driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div/div[1]/div/div[2]/div[3]/span').click(1)  # 点击抹分
		driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div/div[1]/div/div[2]/div[1]/span').click()  # 点击批量修改
		driver.find_element_by_class_name('savebtn').click(1)  # 点击保存

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[3]/a').click()  # 点击商品促销
		W1=driver.find_elements_by_xpath('//span[@ng-bind="productPreferential.pName"]')[-1].text
		self.assertEqual(W1,W2,'创建促销活动成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[3]/a').click()  # 点击商品促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[6]/a[1]').click()  # 点击编辑按钮
		driver.find_element_by_class_name('savebtn').click(1)  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[3]/a').click()  # 点击商品促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click()#点击启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click()#点击启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click()#点击启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div').click()#点击启动状态


		driver.find_elements_by_xpath('//a[@ng-click="logic.deleteProductPreferential($index,productPreferential.id)"]')[-1].click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定

		Q1=driver.find_elements_by_xpath('//span[@ng-bind="productPreferential.pName"]')[-1].text
		self.assertNotIn(W2,Q1,'删除成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[2]').click()  # 点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[3]').click()  # 点击进行中
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[4]').click()  # 点击已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[1]').click()  # 点击全部
		sleep(3)
