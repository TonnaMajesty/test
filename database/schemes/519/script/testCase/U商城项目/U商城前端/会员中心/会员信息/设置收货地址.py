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
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click()  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[7]/ul/li[2]/a/span').click()  # 点击收货地址
		sleep(3)
		driver.find_element_by_xpath('//a[@class="main_addaddr showModelBtn"]').click()  # 点击添加新地址
		driver.find_element_by_xpath('//input[@id="cReceiver"]').send_keys(u'老王')  # 输入收货人姓名
		driver.find_element_by_xpath('//input[@id="cMobile"]').send_keys('136'+tool.randomStr(8,number=True))  # 输入手机号码

		js = driver.find_element_by_xpath('//select[@id="cProvince"]')
		js.find_element_by_xpath('//option[@value="110000"]').click()  # 选择北京

		ja = driver.find_element_by_xpath('//select[@id="cCity"]')
		ja.find_element_by_xpath('//option[@value="110100"]').click()  # 选择北京市

		jd = driver.find_element_by_xpath('//select[@id="cArea"]')
		jd.find_element_by_xpath('//option[@value="110108"]').click()  # 选择海淀区

		driver.find_element_by_xpath('//textarea[@id="cAddress"]').send_keys(u'用友路1号')  # 输入详细地址
		driver.find_element_by_xpath('//button[@id="newaddressSave"]').click(3)  # 点击保存
		driver.find_elements_by_xpath('//a[@class="edit-btn"]')[-2].click()  # 点击编辑按钮
		driver.find_element_by_xpath('//*[@id="newaddressSave"]').click(3)  # 点击保存
		driver.find_element_by_xpath('//*[@id="addrList"]/div[1]/div/div[3]/div/div/a[2]').click(3)  # 点击设置为常用地址
		driver.find_elements_by_xpath('//a[@class="delete-btn"]')[-2].click()  # 点击删除
		driver.switch_to.alert.accept()
		sleep(3)