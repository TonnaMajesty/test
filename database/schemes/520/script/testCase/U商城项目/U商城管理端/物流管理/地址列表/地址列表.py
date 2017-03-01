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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[5]/li[4]/a').click()#点击地址列表
		sleep(5)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td[6]/a[2]').click()#点击禁用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td[6]/a[1]').click()#点击启用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[6]/a[2]').click()#点击重置数据
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击确定
		sleep(5)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td[1]/span[1]').click()#点击北京后“+”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[1]/span[1]').click()#点击北京后“+”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div[1]/table/tbody/tr[1]/td[6]/a[3]').click()#点击东城后新增下一级
		driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div[2]/div/div[2]/span[2]/input').send_keys(u'龙玉区')#输入地址名称
		#driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/div/div[5]/span[2]/div/div/span[3]').click()#点击是
		driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div[3]/div/button[2]').click()#点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div[1]/table/tbody/tr[1]/td[1]/span[1]').click()#点击东城“+”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[6]/a[3]').click()#点击编辑
		driver.find_element_by_xpath('//*[@id="ngdialog4"]/div[2]/div[3]/div/button[2]').click()#点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[6]/a[4]').click()#点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[1]').click()#点击全部展开
		sleep(10)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[2]').click(2)  # 点击全部收缩
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td[1]/input').click()#选择北京
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[2]/table/tbody/tr[1]/td[1]/input').click()  # 选择天津
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[4]').click()#点击批量禁用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[6]/a[1]').click()#点击显示启用
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[6]/a[1]').click()  # 点击显示全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td[1]/input').click()#选择北京
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/div[2]/table/tbody/tr[1]/td[1]/input').click()  # 选择天津
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[3]').click()#点击批量启用
		sleep(3)
		
