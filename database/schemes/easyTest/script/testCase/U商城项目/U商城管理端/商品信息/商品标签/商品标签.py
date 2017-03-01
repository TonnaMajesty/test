# coding=utf-8
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
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[1]/upmark").click()  # 点击商品信息
		driver.find_element_by_link_text("商品标签").click()  # 点击商品标签
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()  # 点击新增
		MC=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//input[@placeholder="请输入标签名称"]').send_keys(MC)  # 标签名称输入“”
		driver.find_element_by_xpath('//input[@placeholder="请输入标签备注"]').send_keys(u'真的么')  # 标签备注输入“”
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/button[2]').click()  # 点击确定

		YZ=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td:nth-child(1)').text
		self.assertEqual(YZ,MC,'创建成功')

		# 编辑
		driver.find_elements_by_xpath('//a[@ng-click="edit(uptag)"]')[-1].click()  # 点击最后一行编辑
		driver.find_element_by_xpath('//input[@placeholder="请输入标签名称"]').send_keys('1')
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/button[2]').click()  # 点击确定

		AA=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td:nth-child(1)').text
		self.assertNotEqual(AA,MC,'编辑成功')

		# 删除
		driver.find_elements_by_xpath('//a[@ng-click="del($index)"]')[-1].click()  # 点击第三行删除
		driver.switch_to.alert.accept()

		BB=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td:nth-child(1)','findAssert').text
		self.assertIsNone(BB,'删除成功')

