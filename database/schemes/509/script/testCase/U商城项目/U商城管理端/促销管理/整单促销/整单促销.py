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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[5]/a').click()  # 点击整单促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a').click()  # 点击新增活动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[2]/span[2]/label[2]/input').click()  # 选择减价活动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[2]/span[2]/label[1]/input').click()  # 选择打折活动
		QW=tool.randomStr(6,False,True)
		driver.find_element_by_xpath('//input[@placeholder="请输入活动名称" and @value="pricePreferential.pName"]').send_keys(QW)  # 输入活动名称
		driver.find_element_by_xpath('//input[@placeholder="请输入开始日期"]').send_keys(u'2017-08-31 00:00:00')  # 输入开始时间
		driver.find_element_by_xpath('//input[@placeholder="请输入结束日期"]').send_keys(u'2017-09-30 00:00:00')  # 输入结束时间
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[5]/span[2]/label[2]/input').click()  # 选择部分商品
		driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[1]/div[2]/table/tbody[1]/tr/td[4]/button/span').click()  # 点击第一个商品的“+”
		driver.find_element_by_xpath('//*[@id="productright"]/table/tbody/tr/td[4]/button/span').click()  # 点击右边的叉
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[5]/span[2]/label[1]/input').click()  # 选择全部商品
		driver.find_element_by_xpath('//*[@id="dazhe"]/tbody/tr/td[3]/input').send_keys(u'200')  # 消费满输入“200”
		driver.find_element_by_xpath('//*[@id="dazhe"]/tbody/tr/td[6]/input').send_keys(u'7')  # 打折输入“”
		driver.find_element_by_xpath('//button[@ng-click="specLogic.save(true)"]').click()  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[5]/a').click(2)  # 点击整单促销

		WE=driver.find_elements_by_xpath('//span[@ng-bind="pricePreferential.pName"]')[-3].text
		self.assertEqual(QW,WE,'创建成功')
		sleep(3)


		# 编辑
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[8]/a[1]').click()  # 点击编辑
		driver.find_element_by_xpath('//button[@ng-click="specLogic.save(true)"]').click()  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[5]/a').click()  # 点击整单促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]/div').click()  # 点击启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]/div').click()  # 点击启动状态

		# 删除
		driver.find_elements_by_xpath('//a[@ng-click="logic.deletePricePreferential($index,pricePreferential.id)"]')[0].click()  # 点击删除按钮
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[5]/a').click()  # 点击整单促销

		WE=driver.find_elements_by_xpath('//span[@ng-bind="pricePreferential.pName"]')[0].text
		self.assertNotEqual(WE,QW,'删除成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[2]').click()  # 点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[3]').click()  # 点击进行中
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[4]').click()  # 点击已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[1]').click()  # 点击全部
		sleep(3)