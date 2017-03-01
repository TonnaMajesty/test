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
		param=self.param
		tool=utils_user

		driver.find_element_by_link_text('首页').click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[1]/upmark').click()  # 点击促销管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[4]/li[2]/a').click()  # 点击赠品促销
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[2]/a').click()  # 点击新增活动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[3]/span[2]/label[2]/input').click()  # 选择满件送
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[3]/span[2]/label[3]/input').click()  # 选择买就送
		driver.find_element_by_xpath('//*[@id="aAnda"]/input').click()  # 选择买A送A
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[3]/span[2]/label[1]/input').click()  # 选择满额送
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/label/input').click()#选择是否使用
		# sleep(2)
		RR=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div/input').send_keys(RR)  # 输入活动名称
		driver.find_element_by_xpath('//*[@id="dStartDate"]').send_keys(u'2017-12-30 00:00:00')  # 输入开始时间
		driver.find_element_by_xpath('//*[@id="quitTimeChange2"]').click()  # 点击七天
		driver.find_element_by_xpath('//*[@id="quitTimeChange3"]').click()  # 点击一个月
		driver.find_element_by_xpath('//*[@id="quitTimeChange4"]').click()  # 点击三个月
		driver.find_element_by_xpath('//*[@id="quitTimeChange1"]').click()  # 点击一天
		driver.find_element_by_xpath('//*[@id="subProduct"]/input').click()  # 选择部分商品
		driver.find_element_by_xpath('//*[@id="allProduct"]/span[2]/label[1]/input').click()  # 选择全部商品
		#driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[7]/div/div[2]/label/input').click()  # 选择金卡
		#driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[7]/div/div[1]/label/input').click()  # 选择所有会员适用
		#driver.find_element_by_xpath('//*[@id="mutexType1"]/input').click()  # 选择整单促销
		#driver.find_element_by_xpath('//*[@id="mutexType2"]/input').click()  # 选择包邮活动
		#driver.find_element_by_xpath('//*[@id="mutexType4"]/input').click()  # 选择优惠券
		driver.find_element_by_xpath('//*[@id="iGiftType1"]/tbody/tr/td[2]/input').send_keys(u'500')  # 消费输入“”

		wk = driver.find_element_by_xpath('//*[@id="iGiftItemType"]')
		wk.find_element_by_xpath('//*[@id="iGiftItemType"]/option[3]').click()  # 选择N倍积分

		driver.find_element_by_xpath('//*[@id="iGiftType1iGiftNum0"]').send_keys(u'2')

		# driver.find_element_by_xpath('//*[@id="iGiftType10"]').click()  # 点击选择赠品
		# driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[1]/span/input').click()  # 选择第一个优惠券

		# driver.find_element_by_xpath('//*[@id="ngdialog5"]/div[2]/div[1]/div[2]/div/div[2]/table/tbody[2]/tr/td[1]/span/input').click()#选择第二个赠品
		# driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button').click()  # 点击添加
		# sleep(3)

		# js = "document.getElementsByClassName('ngdialog ngdialog-theme-default ng-scope')[0].style.display='none'document.documentElement.style.overflowY = 'scroll'"
		# driver.execute_script(js)  # 隐藏窗口

		driver.find_element_by_xpath('//*[@id="iGiftType1"]/tbody/tr/td[8]/a[1]/span').click()  # 点击“+”
		driver.find_element_by_xpath('//*[@id="iGiftType1"]/tbody/tr[2]/td[8]/a[2]/span').click()  # 点击“-”
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[12]/div[2]/button').click()  # 点击保存
		sleep(2)

		WW=driver.find_elements_by_xpath('//span[@ng-bind="giftPreferential.sName"]')[0].text
		self.assertEqual(RR,WW,'创建赠品促销成功')


		# 编辑，删除
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]/a[1]').click()  # 点击编辑
		driver.find_elements_by_link_text('编辑')[-1].click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[12]/div[2]/button').click(2)  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[6]/div').click()  # 点击启动
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]/a[2]').click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(2)

		TT=driver.find_elements_by_xpath('//span[@ng-bind="giftPreferential.sName"]')[0].text
		self.assertNotEqual(TT,RR,'删除赠品促销成功')

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[2]').click()  # 点击未开始
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[3]').click()  # 点击进行中
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[4]').click()  # 点击已结束
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div/div[1]/a[1]').click()  # 点击全部
		sleep(3)