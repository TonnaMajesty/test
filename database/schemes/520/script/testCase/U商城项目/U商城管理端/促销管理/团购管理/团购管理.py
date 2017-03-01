# coding=utf-8
from time import sleep

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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[6]/a').click()  # 点击团购管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/a').click()  # 点击新增
		MC=tool.randomStr(6,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div/input').send_keys(MC)  # 输入活动名称
		driver.find_element_by_xpath('//*[@id="startTime"]').send_keys(u'2016-12-29 00:00:00')  # 输入开始日期
		driver.find_element_by_xpath('//*[@id="quitTimeChange1"]').click()  # 点击一天
		driver.find_element_by_xpath('//*[@id="quitTimeChange2"]').click()  # 点击七天
		driver.find_element_by_xpath('//*[@id="quitTimeChange3"]').click()  # 点击一个月
		driver.find_element_by_xpath('//*[@id="quitTimeChange4"]').click()  # 点击三个月
		driver.find_element_by_xpath('//*[@id="memberPayType1"]/input').click()  # 选择可使用会员积分抵扣
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[10]/div/div[3]/div[2]/input').send_keys(u'3')  # 输入成团条件
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[10]/div/div[3]/div[4]/input').send_keys(u'2')  # 输入初始已购
		driver.find_element_by_xpath('//*[@id="product"]/div/div[1]/div[2]').click()  # 点击添加商品
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click()  # 选择第一个商品
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click(3)  # 点击添加
		driver.find_element_by_xpath('//*[@id="product"]/div/div[1]/div[3]').click()  # 点击清除全部商品

		driver.find_element_by_xpath('//*[@id="product"]/div/div[1]/div[2]').click()  # 点击添加商品
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click()  # 选择格力
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click(3)  # 点击添加
		driver.find_element_by_xpath('//*[@ng-model="item.groupNumbers"]').send_keys(u'1')#输入成团条件‘1’
		sleep(2)
		driver.find_element_by_xpath('//*[@ng-model="item.totalLimitQuantity"]').send_keys(u'2')  # 输入总限购量
		driver.find_element_by_xpath('//*[@ng-model="item.singleLimitQuantity"]').send_keys(u'3')  # 输入每客户限购量
		sleep(2)
		driver.find_element_by_xpath('//*[@ng-model="item.initialSales"]').send_keys(u'1')#输入初始已购
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[12]/div[2]/button').click()  # 点击保存

		CX=driver.find_elements_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space20.ng-scope > div.col-xs-12 > table > tbody > tr:nth-child(1) > td:nth-child(2)',"findAssert")[0].text
		self.assertEqual(CX,MC,'创建成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[1]').click()  # 点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[2]').click()  # 点击组团中
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[3]').click()  # 点击已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[4]').click()  # 点击未启用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[5]').click()  # 点击全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[1]').click()  # 点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input').send_keys(MC)  # 输入名称
		# driver.find_element_by_xpath('//*[@id="startTime"]').send_keys(u'2016-11-03 00:00:00')  # 输入开始时间
		# driver.find_element_by_xpath('//*[@id="endTime"]').send_keys(u'2016-12-31 00:00:00')  # 输入结束日期
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[4]/button').click(1)  # 点击搜索

		self.assertEqual(CX,MC,'精确查询成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()  # 点击促销管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[6]/a').click()  # 点击团购管理
		driver.find_element_by_xpath('//a[@ng-click="del(groupbuying.id)"]').click()#点击删除
		driver.find_element_by_xpath('//button[@class="btn btn-primary btn-lg" and @ng-click="ok()"]').click()#点击确定
		sleep(2)

		QD=driver.find_elements_by_xpath('//td[@ng-bind="groupbuying.name"]')[0].text
		self.assertNotIn(MC,QD,'删除成功')
		sleep(3)
