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
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[1]/upmark").click()  # 点击商品信息
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[8]/a").click()  # 点击商品品牌

		driver.find_element_by_xpath("//a[@href='/corp/productBrand/toAdd?menuid=27']").click()  # 点击新增
		MC=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/input").send_keys(MC)  # 品牌名称输入“”
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/div[1]/input").send_keys("1")  # 排序输入“1”
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[3]/div/input").send_keys(U"户外风衣")  # 品牌别名输入“”
		#driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[5]/div/div/div[1]/div/a').click()  # 上传图片
		#driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[5]/div/div/div[1]/div/input').send_keys("E:\\tupian\\huwaifengyi.jpg")  # 上传图片
		#os.system("E:\\pythonScript\\autoit\\guanbi.exe")  # 调用guanbi.exe程序关闭windows窗口
		# driver.find_element_by_xpath("//input[@ng-model='brand.isSelected']").click()  # 点击选择户外
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div/div/div[2]/div").send_keys(u"适合户外旅游")  # 品牌描述输入
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[3]/div/button").click()  # 点击保存按钮
		sleep(3)

		YZ=driver.find_elements_by_xpath('//div[@ng-bind="product.brand_name"]')[-1].text
		self.assertEqual(YZ,MC,'创建品牌成功')
		sleep(3)


		# text = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div").text
		# if text == u"名称重复继续保存吗?":
		# 	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click(3)

		driver.find_element_by_xpath("//a[@href='/corp/productBrand/toAdd?menuid=27']").click()  # 点击新增
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/input").send_keys(tool.randomStr(6,False,True))  # 品牌名称
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/div[1]/input").send_keys("1")  # 排序输入“1”
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[3]/div/button").click()  # 点击保存按钮
		sleep(3)


		driver.find_elements_by_link_text('编辑')[-2].click()  #点击第三行的编辑按钮
		driver.find_element_by_xpath('//input[@ng-model="product.brand_name"]').send_keys('1')
		driver.find_element_by_xpath("//button[@type='submit']").click()  #点击保存按钮
		sleep(3)

		AA=driver.find_elements_by_xpath('//div[@ng-bind="product.brand_name"]')[-2].text
		self.assertNotEqual(AA,MC,'编辑成功')


		driver.find_element_by_xpath("//input[@ng-model='query.brand_name']").send_keys(AA)  # 在品牌名称输入NORTHFACE
		driver.find_element_by_xpath("//a[@ng-click='search()']").click()  # 点击查询
		sleep(2)

		BB=driver.find_element_by_xpath('//div[@ng-bind="product.brand_name"]').text
		self.assertEqual(BB,AA,'查询成功')

		# driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[8]/a").click()  # 点击商品品牌
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[6]/div/nav/ul/li[8]/a/span').click()  # 点击末页
		driver.find_element_by_xpath("//a[@ng-click='del(product.id)']").click()  # 点击第一行的删除按钮
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确定按钮
		sleep(3)
		driver.find_element_by_xpath("//input[@ng-model='query.brand_name']").send_keys(AA)  # 在品牌名称输入NORTHFACE
		driver.find_element_by_xpath("//a[@ng-click='search()']").click()  # 点击查询

		CC=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(4) > div > table > tbody > tr > td:nth-child(2) > div','findAssert').text
		self.assertIsNone(CC,'删除成功')


		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[8]/a").click()  # 点击商品品牌

		driver.find_elements_by_xpath('//input[@ng-model="product.isChecked"]')[-1].click()  # 选定第三个订单
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div/table/tbody/tr[4]/td[1]/div/input").click()  # 选定第四个订单
		driver.find_element_by_xpath("//a[@ng-click='delAll()']").click()  # 点击批量删除
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确认按钮
		sleep(3)

		DD=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(4) > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div','findAssert').text
		self.assertIsNone(DD,'删除成功')

