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
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[1]/upmark').click()  # 点击站点设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[8]/a').click()  # 点击文章分类
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/table[1]/tbody/tr[1]/td[4]/a[1]').click()  # 点击新增子类
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[2]/span[2]/input').send_keys(u'笑傲江湖')
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[3]/span[2]/input').send_keys(u'大话江湖')
		driver.find_element_by_xpath('//button[@ng-click="ok()" and @class="btn btn-save btn-warning"]').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/table[1]/tbody/tr[1]/td[4]/a[2]').click()  # 点击编辑
		driver.find_element_by_xpath('//button[@ng-click="ok()" and @class="btn btn-save btn-warning"]').click()  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/table[2]/tbody/tr[1]/td[4]/a[3]').click()  # 点击上移
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/table[1]/tbody/tr[1]/td[4]/a[4]').click()  # 点击下移
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[2]').click()  # 点击全部展开
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[3]').click()  # 点击全部收缩
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/thead/tr/th[1]/a[1]').click()  # 点击新增一级分类
		driver.find_element_by_xpath('//input[@ng-model="editClassData.tName" and @placeholder="分类名称"]').send_keys(u'小鼠')  # 输入分类名称
		driver.find_element_by_xpath('//input[@ng-model="editClassData.tPagename" and @placeholder="页面名称"]').send_keys(u'老鼠')  # 输入页面名称
		driver.find_element_by_xpath('//button[@class="btn btn-save btn-warning" and @ng-click="ok()"]').click(2)  # 点击确定
		driver.find_elements_by_xpath('//a[@ng-click="classfilyLogic.deleteItem(item,array)"]')[-1].click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		# driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/span[1]').click()  # 点击帮助中心“+”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/a[5]').click()  # 点击笑傲后删除按钮
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(3)