# coding=utf-8
import time

from selenium.webdriver import ActionChains

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
		tool = utils_user

		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[2]/li[1]").click()  # 点击商品信息
		#driver.find_elements_by_xpath('//upmark[@ng-bind="menu.name"]')[1].click()
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[2]/li[2]").click()  # 点击商品列表

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/a[1]").click()  # 点击新增
		driver.find_element_by_xpath("//input[@name='5']").click()# 点击虚拟商品
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input').click()  # 选择礼品卡
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[2]/div/div[3]/input').click()  # 选择储值卡
		driver.find_element_by_xpath('//input[@ng-value="4"]').click()  # 选择其他
		# driver.find_element_by_xpath("//input[@name='7']").click()  # 选择积分换购
		# driver.find_element_by_xpath("//input[@name='6']").click()  # 选择现金购买
		driver.find_element_by_xpath('//input[@name="4"]').click()  # 选择普通商品
		driver.find_element_by_xpath('//input[@placeholder="必填"]').send_keys(tool.randomStr(6,False,True))  # 输入商品编码“”
		SS=tool.randomStr(6,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//input[@placeholder="最多可输入100个字符"]').send_keys(SS)  # 商品名称输入‘’

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div/div/div/input').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div/div/div/ul/li[3]/div/span[1]').click()
		# driver.find_element_by_css_selector('.dropContent>li:nth-child(5)>div').click()  # 商品分类选择
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div/div/div/ul/li[3]/ul/li[1]/div').click()#选择办公设备下的传真机

		#driver.find_element_by_xpath('//*[@id="dws"]').click()
		driver.find_element_by_xpath('//*[@id="dws"]/option[3]').click()  # 选择计量单位
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[9]/div/button[1]').click(2)  # 点击保存
		time.sleep(2)

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/a[1]").click()  # 点击新增
		# driver.find_element_by_xpath("//input[@name='5']").click()  # 点击虚拟商品
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input').click()  # 选择礼品卡
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[2]/div/div[3]/input').click()  # 选择储值卡
		# driver.find_element_by_xpath('//input[@ng-value="4"]').click()  # 选择其他
		# driver.find_element_by_xpath("//input[@name='7']").click()  # 选择积分换购
		# driver.find_element_by_xpath("//input[@name='6']").click()  # 选择现金购买
		driver.find_element_by_xpath('//input[@name="4"]').click()  # 选择普通商品
		driver.find_element_by_xpath('//input[@placeholder="必填"]').send_keys(tool.randomStr(6, False, True))  # 输入商品编码“”
		DD=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//input[@placeholder="最多可输入100个字符"]').send_keys(DD)  # 商品名称输入‘’

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div/div/div/input').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div/div/div/ul/li[3]/div/span[1]').click()
		# driver.find_element_by_css_selector('.dropContent>li:nth-child(5)>div').click()  # 商品分类选择
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div/div/div/ul/li[3]/ul/li[1]/div').click()  # 选择办公设备下的传真机

		#driver.find_element_by_xpath('//*[@id="dws"]').click()
		driver.find_element_by_xpath('//*[@id="dws"]/option[3]').click()  # 选择计量单位
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[9]/div/button[1]').click(2)  # 点击保存
		time.sleep(2)

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[7]/p[1]/a").click()  # 点击第一行的编辑按钮
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div[9]/div/button[1]').click()#点击保存
		time.sleep(3)

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/input").send_keys(SS)  # 商品名称输入“”
		driver.find_element_by_xpath("//a[@ng-click='search()' and @class='btn btn-warning m-r-5']").click()  # 点击查询按钮
		time.sleep(5)
		ff=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(5) > div > table > tbody > tr > td:nth-child(2) > div.proNamediv > p:nth-child(2)','findAssert').text
		self.assertEqual(ff,SS,'创建商品成功')


		driver.find_element_by_xpath('//a[@ng-click="del(product)"]').click()  # 点击第一行的删除按钮
		driver.find_element_by_xpath("//button[@class='btn btn-primary btn-lg' and @ng-click='ok()']").click(3)  # 点击确定

		driver.find_element_by_xpath("//input[@placeholder='商品名称']").send_keys(SS)  # 商品名称输入“”
		driver.find_element_by_xpath("//a[@ng-click='search()' and @class='btn btn-warning m-r-5']").click()  # 点击查询按钮
		time.sleep(5)
		HH=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(5) > div > table > tbody > tr > td:nth-child(2) > div.proNamediv > p.space5.colorgray.font-size-12.ng-binding','findAssert').text
		self.assertIsNone(HH,'删除成功')
		time.sleep(5)
		driver.find_element_by_xpath("//input[@placeholder='商品名称']").clear()
		driver.find_element_by_xpath("//input[@placeholder='商品名称']").send_keys(DD)  # 商品名称输入“”
		driver.find_element_by_xpath("//a[@ng-click='search()' and @class='btn btn-warning m-r-5']").click()  # 点击查询按钮
		time.sleep(5)
		GG=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(5) > div > table > tbody > tr > td:nth-child(2) > div.proNamediv > p.space5.colorgray.font-size-12.ng-binding','findAssert').text
		self.assertEqual(GG,DD,'创建成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[1]/div/input').click()  # 选择第一行商品
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[6]/div/div/label/input').click()  # 选全选
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[3]').click()  # 点击批量删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(3)  # 点击确定

		driver.find_element_by_xpath("//input[@placeholder='商品名称']").send_keys(DD)  # 商品名称输入“”
		driver.find_element_by_xpath("//a[@ng-click='search()' and @class='btn btn-warning m-r-5']").click()  # 点击查询按钮
		time.sleep(5)

		KK=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(5) > div > table > tbody > tr > td:nth-child(2) > div.proNamediv > p.space5.colorgray.font-size-12.ng-binding','findAssert').text
		self.assertIsNone(KK,'删除成功')

		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[2]/li[2]/a").click()  # 点击商品列表


		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[1]/div/input').click()  # 选择第一行商品
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[2]/td[1]/div/input').click()  # 选择第二行商品
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[1]/span/span[1]').click()  # 点击批量操作
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[1]/div/ul/li[2]').click()  # 点击商品下架
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		time.sleep(5)

		ZZ=driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td:nth-child(6) > div > p:nth-child(1)","findAssert").text
		self.assertEqual(ZZ,'未上架','下架成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[1]/div/input').click()  # 选择第一行商品
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[2]/td[1]/div/input').click()  # 选择第二行商品
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[1]/span/span[1]').click()  # 点击批量操作
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[1]/div/ul/li[1]').click()  # 点击商品上架
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(3)  # 点击确定

		#XX=driver.find_elements_by_xpath('''//p[@ng-bind=" '上架：'+product.iUpCount"]''')[0].text
		#self.assertEqual(XX,'上架：1','商品上架成功')


		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[1]/div/input").click()  # 选择第一行
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[2]/td[1]/div/input").click()  # 选择第二行
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[1]/span/span[1]').click()  # 点击批量操作
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[1]/div/ul/li[2]").click()  # 点击下架

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[1]/div/input").click()  # 选择第一行
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[2]/td[1]/div/input").click()  # 选择第二行
		driver.find_element_by_xpath('//a[@class="btn btn-info" and @ng-mouseleave="setTagHidden()"]').click()  # 点击设置标签
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[2]/div/ul/li').click()  # 点击批量标签
		driver.find_element_by_xpath('//input[@ng-model="taginfo.isChecked" and @class="ng-pristine ng-untouched ng-valid"]').click()  # 选择第一项
		driver.find_element_by_xpath('//button[@class="btn btn-primary"and @ng-click="ok()"]').click(3)  # 点击保存
		time.sleep(5)
		VV = driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div.proNamediv > p.p-t-10 > span > label > span',"findAssert").text
		self.assertEqual(VV, '限购', '批量设置标签成功')

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[5]/div/table/tbody/tr[1]/td[1]/div/input").click()  # 选择第一行
		driver.find_element_by_xpath('//a[@class="btn btn-info" and @ng-mouseleave="setTagHidden()"]').click()  # 点击设置标签
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[1]/a[2]/div/ul/li').click()  # 点击批量标签
		driver.find_element_by_xpath('//input[@ng-model="taginfo.isChecked" and @class="ng-pristine ng-untouched ng-valid"]').click()  # 选择第一项
		driver.find_element_by_xpath('//button[@class="btn btn-primary"and @ng-click="ok()"]').click(3)  # 点击保存





		# 导入，导入模板下载
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/a[2]').click()  # 点击导入
		# os.system("E:\\pythonScript\\autoit\\guanbi.exe")  # 调用guanbi.exe程序关闭windows窗口
		# driver.find_element_by_xpath('//a[@class="btn btn-info" and @href="/public/template/product.zip" and @ng-show="true"]').click()  # 点击商品模板下载


