# coding=utf-8
import sys
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
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[1]/upmark').click()  # 点击物流管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[3]/a').click()  # 点击配送方式
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()  # 点击新增
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[3]/div/input').send_keys(u'空运')  # 配送方式名称输入
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[5]/div/input[1]').click()  # 选择全场包邮
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[15]/div/button[2]').click()  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[5]/div/input[2]').click()  # 选择统一计价
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[5]/div/div/input').send_keys(u'10')  # 输入价格
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[15]/div/button[2]').click()  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[5]/div/input[3]').click()  # 选择按重量计算
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[9]/div/input[1]').send_keys(u'10')  # 首重费用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[9]/div/input[2]').send_keys(u'15')  # 续重费用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[15]/div/button[2]').click()  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[3]/a').click()  # 点击配送方式
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[4]/div[2]/nav/div/input').send_keys(u'2')  # 输入第二页
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[4]/div[2]/nav/div/button').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[5]/td[8]/a[1]').click()  # 点击编辑
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[15]/div/button[2]').click()  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[3]/a').click()  # 点击配送方式
		sleep(3)
		driver.find_elements_by_xpath('//input[@ng-change="checkboxClick(deliveryType.isChecked)"]')[-2].click()
		driver.find_elements_by_xpath('//input[@ng-change="checkboxClick(deliveryType.isChecked)"]')[-3].click()
		driver.find_elements_by_xpath('//input[@ng-change="checkboxClick(deliveryType.isChecked)"]')[-4].click()
		#driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[2]/td[1]/span/input').click()
		#driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[3]/td[1]/span/input').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[4]/div[1]/div[2]/a').click()  # 点击批量删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)
		
		
