# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()

		driver.find_element_by_css_selector(".classify").show()
		#js = '$(".classify").show()'
		#driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		sleep(3)
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[4]/div', '香港直邮美国商品').click()  # 点击香港直邮美国商品
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="product-detail"]/div/div[2]/div/div[3]/div[2]/a[3]/span','收藏商品').click()#点击收藏商品
		driver.switch_to.alert.accept()

		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click() # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[6]/ul/li[1]/a/span').click()  # 点击我的收藏
		js = '$(".classify").show()'
		driver.execute_script(js)
		js1 = '$("#category > ul > li:nth-child(1) > div").show()'
		driver.execute_script(js1)
		driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/div/ul/li[1]/a').click()  # 点击艺术纸
		sleep(3)
		driver.find_element_by_xpath('//*[@id="product_list"]/div[2]/ul/li[1]/div', 'HK直邮 美国GNC 卵磷脂 1200mg180粒').click()  # 点击HK直邮 美国GNC 卵磷脂 1200mg180粒
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		driver.find_element_by_xpath('//*[@id="product-detail"]/div/div[2]/div/div[3]/div[2]/a[3]/span','收藏商品').click()  # 点击收藏商品
		driver.switch_to.alert.accept()
		sleep(3)

		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click()  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[6]/ul/li[1]/a/span').click()  # 点击我的收藏
		# driver.find_element_by_xpath('//*[@id="categoryFilter"]/a[2]').click();  # 点击办公设备（1）
		# driver.find_element_by_xpath('//*[@id="categoryFilter"]/a[3]').click();  # 点击1005001（1）
		# driver.find_element_by_xpath('//*[@id="allProductClassfied"]').click();  # 点击全部
		# driver.find_element_by_xpath('//*[@id="stateFilter"]/a[2]').click();  # 点击进口
		# driver.find_element_by_xpath('//*[@id="allProductTag"]').click();  # 点击全部
		driver.find_element_by_xpath('//*[@id="fav-search-text"]').send_keys(u'香港直邮美国商品')  # 输入商品名称
		driver.find_element_by_xpath('//*[@id="collection_main "]/div[1]/div[2]/div/div/a').click()  # 点击搜索
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[6]/ul/li[1]/a/span').click()  # 点击我的收藏
		driver.find_element_by_xpath('//*[@id="clearAll"]').click()  # 点击取消关注
		driver.switch_to.alert.accept()
		sleep(3)