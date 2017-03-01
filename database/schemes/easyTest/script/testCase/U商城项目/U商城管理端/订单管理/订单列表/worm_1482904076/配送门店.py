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
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化：param
		说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值

		自定义工具模块：tool 文件所在路径script/common/utils.py
		开发人员可根据需要自行添加新的函数
		例如：
		获取一个随机生成的字符串：number=tool.randomStr(6)

		##################################################################
		该方法内进行测试用例的编写
		'''
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/a").click()  # 点击首页
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark").click()  # 点击订单管理
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[2]/a").click()  # 点击订单列表
		driver.find_elements_by_xpath('//button[@ng-click="store.openStoreDialog(order)"]')[0].click()  # 点击配送门店
		# driver.find_element_by_xpath('//input[@placeholder="店名"').send_keys('用友门店')#输入查询条件
		# driver.find_element_by_xpath('//*[@id="ngdialog8"]/div[2]/div[2]/div[1]/div/div[3]/button').click()#点击搜门店
		driver.find_element_by_xpath('//*[@id="storeSelector"]/ul/li[1]/div/span[1]/input').click()  # 选择门店
		driver.find_elements_by_xpath('//button[@ng-click="store.submit(order)"]')[-1].click()  # 点击确定
		driver.find_elements_by_xpath('//input[@class="cCheckBox ng-pristine ng-untouched ng-valid"]')[0].click()#选择第一个订单
		driver.find_element_by_xpath('//a[@ng-click="store.openStoreDialog()"]').click()#点击批量指定配送门店
		driver.find_element_by_xpath('//*[@id="storeSelector"]/ul/li[2]/div/span[1]/input').click()#选择门店
		driver.find_elements_by_xpath('//button[@ng-click="store.submit()"]')[-1].click()#点击确定
		sleep(3)