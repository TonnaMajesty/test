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


		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(4) > li").click()  #点击会员中心
		driver.close()
		driver.switch_to.window(0)
		text = driver.title
		self.assertEqual(text, "会员档案", "跳转成功")
		sleep(3)
		'''
		driver.find_element_by_xpath('//a[@href="/Page/Shop/UpMall"]').click(2)#点击商城
		driver.find_element_by_xpath('//span[@style="background: url('/images/menu/icon-menu-0303.png') no-repeat;"]').click()#点击门店管理
		driver.find_element_by_xpath('//*[@id="page_menu"]/li[2]/div[2]/a[1]/p').click()#点击门店档案
		driver.find_elements_by_xpath('//a[@href="/Page/Store/Store"]')[-1].click()#点击新增
		As=tool.randomStr(6,lowerCaseLetter=True)
		driver.find_element_by_id('cName').send_keys(As)#输入门店名称
		driver.find_element_by_id('cCode').send_keys(tool.randomStr(5,number=True))#输入门店编码
		driver.find_element_by_id('cOutCode').send_keys(tool.randomStr(5,number=True))#输入商家编码
		driver.find_element_by_id('cContactPhone').send_keys('136'+tool.randomStr(8,number=True))

		ws=driver.find_element_by_id('cProvince')
		ws.find_element_by_xpath('//option[@value="北京市"]').click()
		sleep(3)
		wa=driver.find_element_by_id('cCity')
		wa.find_element_by_xpath('//*[@id="cCity"]/option[2]').click()
		wd=driver.find_element_by_id('cArea')
		wd.find_element_by_xpath('//option[@value="海淀区"]').click()

		driver.find_element_by_id('locationAction').click()#点击自动定位
		driver.find_element_by_id('saveAction').click()#点击保存

	# 创建门店职位
		driver.find_element_by_xpath('//*[@id="page_menu"]/li[2]/div[2]/a[3]/p').click()#点击门店职位
		driver.find_element_by_id('exportAction').click()#点击新增
		Q1=tool.randomStr(6,lowerCaseLetter=True)
		driver.find_element_by_id('cName').send_keys(Q1)#输入职位名称
		driver.find_element_by_id('iOrder').send_keys(tool.randomStr(4,number=True))#输入排序
		driver.find_element_by_id('saveAction').click()#点击保存
		driver.find_element_by_xpath('//*[@id="page_menu"]/li[2]/div[2]/a[3]/p').click()  # 点击门店职位

		QW=driver.find_elements_by_xpath('//td[@data-field="cName"]')[-1].text
		self.assertEqual(QW,Q1,'创建职位成功')



	# 新增门店员工
		driver.find_element_by_xpath('//*[@id="page_menu"]/li[2]/div[2]/a[2]/p').click()#点击门店员工
		driver.find_element_by_id('exportAction').click()#点击新增
		Q2=tool.randomStr(6,number=True)
		driver.find_element_by_id('cCode').send_keys(Q2)#输入员工编码
		Q3=tool.randomStr(6,lowerCaseLetter=True)
		driver.find_element_by_id('cName').send_keys(Q3)#输入员工名称
		driver.find_element_by_id('cPhone').send_keys('138'+tool.randomStr(8,number=True))#输入电话号码
		we=driver.find_element_by_id('iPosition')
		we.find_element_by_xpath('//option[@value="119"]','员工').click()#选择职位
		wr=driver.find_element_by_id('iStoreId')
		wr.find_element_by_xpath('//option[@value="1423"]').click()#选择门店
		wq=driver.find_element_by_id('iStatus')
		wq.find_element_by_xpath('//option[@value="1"]','在职').click()#选择在职
		driver.find_element_by_id('saveAction').click()#点击保存
		driver.find_element_by_id('btnDialogBySHFConfirm').click()#点击确定
		driver.find_element_by_id('btnDialogBySHFConfirm').click()  # 点击确定
		driver.find_element_by_xpath('//*[@id="page_menu"]/li[2]/div[2]/a[2]/p').click()  # 点击门店员工

		W1=driver.find_elements_by_xpath('//td[@data-field="cCode"]')[0].text
		self.assertEqual(Q2,W1,'创建员工成功')
		sleep(3)
		'''





