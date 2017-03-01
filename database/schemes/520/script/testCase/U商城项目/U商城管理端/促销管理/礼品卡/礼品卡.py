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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[8]/a').click()  # 点击礼品卡
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/a').click()  # 点击新增
		driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/div[1]/div[1]/div/input').send_keys(u'溜溜的它')  # 输入礼品卡名称
		QQ=tool.randomStr(4,number=True,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/input').send_keys(QQ)  # 输入礼品卡号码
		driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/div[1]/div[3]/div/input').click()
		driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/div[1]/div[3]/div/input').send_keys(u'1000')  # 面值输入1
		driver.find_element_by_xpath('//input[@ng-model="giftcard.salePrice"]').clear()
		driver.find_element_by_xpath('//input[@ng-model="giftcard.salePrice"]').send_keys(u'1')  # 售价输入1
		driver.find_element_by_xpath('//*[@id="startDate"]').send_keys('2016-12-31')  # 输入有效时间
		driver.find_element_by_xpath('//*[@id="endDate"]').send_keys('2018-08-20')  # 输入有效时间
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div/textarea').send_keys(u'通用卡')  # 使用说明输入“”

		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[4]/div/a').click()  # 点击上传图片
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[4]/div/input').send_keys('E:\\tupian\\hhhhhh.jpg')
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口

		jj = driver.find_element_by_xpath('//*[@id="styleId"]')
		jj.find_element_by_xpath('//*[@id="styleId"]/option[2]').click()  # 选择样式2
		driver.find_element_by_class_name('savebtn').click(2)  # 点击保存
		sleep(3)
		WQ=driver.find_elements_by_xpath('//td[@ng-bind="giftcard.giftCardCode"]')[0].text
		self.assertEqual(QQ,WQ,'创建成功')
		sleep(2)


		# 编辑，删除
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input').send_keys(u'1')  # 礼品号输入“”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[3]/div[3]/button').click()  # 点击搜索
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()  # 点击促销管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[8]/a').click()  # 点击礼品卡
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[2]').click()  # 未生效
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[3]').click()  # 已生效
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[4]').click()  # 已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/a[1]').click()  # 全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[7]/div/p/a[1]').click()  # 点击编辑
		driver.find_element_by_class_name('savebtn').click(2)  # 点击保存
		sleep(3)
		driver.find_elements_by_xpath('//a[@ng-click="end(giftcard.id)"]')[-2].click()  # 点击结束
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(2)  # 点击确定
		sleep(3)
		driver.find_elements_by_xpath('//a[@ng-click="del(giftcard.id)"]')[-3].click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(2)  # 点击确定

		WE=driver.find_elements_by_xpath('//td[@ng-bind="giftcard.giftCardCode"]')[0].text
		self.assertNotEqual(QQ,WE,'删除成功')
		sleep(3)
