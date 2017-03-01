# coding=utf-8
from time import sleep

from SRC.common import utils_user
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
		tool  = utils_user
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
		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[2]/li[1]/upmark').click()#点击商品信息
		driver.find_element_by_link_text('库存提示规则').click()
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/a").click()#点击增加
		MC=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//input[@placeholder="请输入库存提示规则名称"]').send_keys(MC)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/span[2]/input').send_keys(u'1')#规则排序输入“”
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/span[2]/input[1]').click()#点击是
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/span[2]/input[2]').click()  # 点击否
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[1]/input').send_keys(u'1')#库存区间输入“”
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[2]/input').send_keys(u'100')#库存区间输入“”
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[3]/input').send_keys(u'warming')#库存提示文字输入“”
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/button[2]').click()#点击确定
		sleep(2)

		YZ=driver.find_element_by_xpath('//td[@ng-bind="storePrompt.name"]').text
		self.assertEqual(YZ,MC,'创建成功')

		#编辑
		driver.find_element_by_link_text('编辑').click()#点击编辑
		driver.find_element_by_xpath('//input[@placeholder="请输入库存提示规则名称"]').send_keys('1')
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/button[2]').click()#点击确定
		sleep(3)

		AA=driver.find_element_by_xpath('//td[@ng-bind="storePrompt.name"]').text
		self.assertNotEqual(MC,AA,'编辑成功')

		#删除
		driver.find_element_by_link_text('删除').click()
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()#点击确定
		sleep(3)


		BB=driver.find_element_by_xpath('//td[@ng-bind="storePrompt.name"]','findAssert').text
		self.assertIsNone(BB,'删除成功')
