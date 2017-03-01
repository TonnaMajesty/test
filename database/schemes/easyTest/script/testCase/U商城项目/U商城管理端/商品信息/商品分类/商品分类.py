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

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[1]/upmark").click()  # 点击商品信息
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[2]/li[3]/a").click()  # 点击商品分类
		driver.find_element_by_xpath("//a[@ng-click='classfilyLogic.addItem()']").click()  # 点击新增一级分类
		# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[2]/span[2]/input").click()  # 点击积分兑换分类
		WW=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[4]/span[2]/input').send_keys(WW)  # 分类名称输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[5]/span[2]/input').send_keys(u"222333998312")  # 分类编码输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[6]/span[2]/input').send_keys("100")  # 排序号输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[7]/span[2]/input').send_keys(u"999999")  # 商家编码输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[8]/span[2]/input').send_keys(u"戴着吧")  # 页面标题 title输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[9]/span[2]/input').send_keys(u"帽")  # SEO关键字输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div[10]/span[2]/textarea').send_keys(u"各种帽")  # SEO描述输入“”
		# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[10]/div/div[1]/div/a').click()  # 点击上传图片
		# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[10]/div/div[1]/div/input').send_keys("E:\\tupian\\quyeba4.jpg")  # 上传图片
		# os.system("E:\\pythonScript\\autoit\\guanbi.exe")  # 调用guanbi.exe程序关闭windows窗口
		# jb = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[11]/span[2]/select")
		# jb.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[11]/span[2]/select/option[2]").click()  # 选择输入项
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click(3)  # 点击确定

		QQ=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.firstTd > span.m-l-5.ng-binding').text
		self.assertEqual(QQ,WW,'创建一级分类成功')




		# 新增二级分类
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(1)').click()  # 点击新增子类
		EE=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div[2]/div/div[4]/span[2]/input').send_keys(EE)  # 分类名称输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div[2]/div/div[5]/span[2]/input').send_keys('222456789')  # 分类编码输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div[3]/div/button[2]').click()  # 点击确定按钮
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.firstTd > span.glyphicon.icoStyle.pointer.glyphicon-plus').click()#点击帽子前面“+”


		AA=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.firstTd > span.m-l-5.ng-binding').text
		self.assertEqual(AA,EE,'新增二级分类成功')



		# 新增三级分类
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/table/tbody/tr/td/table[4]/tbody/tr[1]/td[1]/span[1]").click()  # 点击“+”
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(1)').click()  # 点击新增子类按钮
		KK=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//*[@id="ngdialog5"]/div[2]/div[2]/div/div[4]/span[2]/input').send_keys(KK)  # 分类名称输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog5"]/div[2]/div[2]/div/div[5]/span[2]/input').send_keys(u"1239821332123")  # 分类编码输入“”
		driver.find_element_by_xpath('//*[@id="ngdialog5"]/div[2]/div[3]/div/button[2]').click()  # 点击确定按钮
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.firstTd > span.glyphicon.icoStyle.pointer.glyphicon-plus').click()#点击二级分类前面的“+”

		MM=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.firstTd > span.m-l-5.ng-binding').text
		self.assertEqual(KK,MM,'创建三级分类成功')
		sleep(10)


		# 编辑
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(2)').click()  # 点击一级的编辑
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click()  # 点击确定
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(2)').click()  # 点击二级编辑
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click()  # 点击确定
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(1)').click()  # 点击三级编辑
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click()  # 点击确定按钮

		# 查看商品
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(6)').click()  # 点击一级查看商品
		driver.switch_to.window(driver.window_handles[1])

		TT=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(1) > div > ol > li:nth-child(2)').text
		self.assertIn('商品列表',TT,'查看商品成功')
		sleep(3)

		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(6)').click()  # 点击二级查看商品
		driver.switch_to.window(driver.window_handles[1])

		UU = driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(1) > div > ol > li:nth-child(2)').text
		self.assertIn('商品列表',UU, '查看商品成功')
		sleep(3)


		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(5)').click()  # 点击三级查看商品
		driver.switch_to.window(driver.window_handles[1])

		YY = driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(1) > div > ol > li:nth-child(2)').text
		self.assertIn('商品列表',YY, '查看商品成功')
		sleep(3)


		driver.close()
		driver.switch_to.window(driver.window_handles[0])

		# 上移下移
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(3)').click()# 点击上移按钮
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(5) > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(4)').click()#点击下移按钮
		# 删除
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(4)').click()  # 点击三级的删除按钮
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确定
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(5)').click()  # 点击二级删除按钮
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确定
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.lastTd.text-center > a:nth-child(5)').click()  # 点击一级删除按钮
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确定按钮
		sleep(3)

		AA=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(1) > td.firstTd > span.m-l-5.ng-binding','findAssert').text
		self.assertIsNone(AA,'删除成功')

		sleep(5)
