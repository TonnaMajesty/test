# coding=utf-8
import time

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
		driver.find_element_by_class_name("icon-help").click()
		time.sleep(3)
		title = driver.title
		self.assertEqual(title, 'U易联-帮助中心', '跳转异常')
		driver.switch_to_window(driver.window_handles[0])
		time.sleep(3)
		title = driver.title
		self.assertEqual(title, '欢迎使用', '跳转异常')
		driver.find_element_by_class_name("icon-social").click()
		time.sleep(3)
		title = driver.title
		self.assertEqual(title, 'U易联 -  优普论坛 -  Powered by Discuz!', '跳转异常')
		driver.switch_to_window(driver.window_handles[0])
		time.sleep(3)
		title = driver.title
		self.assertEqual(title, '欢迎使用', '跳转异常')
		driver.find_element_by_class_name("icon-contact").click()
		time.sleep(3)
		title = driver.title
		self.assertEqual(title, '联系我们', '跳转异常')
		driver.switch_to_window(driver.window_handles[0])
		time.sleep(3)
		title = driver.title
		self.assertEqual(title, '欢迎使用', '跳转异常')
		#基本统计
		#js1='$(.drp-popup).show()'
		#driver.execute_script(js1)
		#driver.find_element_by_class_name("ok").click()
		time.sleep(1)
		driver.find_element_by_css_selector("#basicStat > ul > li.active > a").click()#七天
		driver.find_element_by_css_selector("#basicStat > ul > li:nth-child(2) > a").click()#30天
		driver.find_element_by_css_selector("#basicStat > ul > li:nth-child(3) > a").click()#三个月
		driver.find_element_by_css_selector("#basicStat > ul > li:nth-child(4) > a").click()#一年
		#会员增长趋势分析
		#新增会员
		driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div.right-title > ul.title-tab > li.active > a").click()
		#交易会员
		driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div.right-title > ul.title-tab > li:nth-child(2) > a").click()
		#储值会员
		driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div.right-title > ul.title-tab > li:nth-child(2) > a").click()
		driver.find_element_by_css_selector("#memberGrowStat > ul > li.active > a").click()#七天
		driver.find_element_by_css_selector("#memberGrowStat > ul > li:nth-child(2) > a").click()#30天
		driver.find_element_by_css_selector("#memberGrowStat > ul > li:nth-child(3) > a").click()#三个月
		driver.find_element_by_css_selector("#memberGrowStat > ul > li:nth-child(4) > a").click()#一年
		#会员等级分布
		driver.find_element_by_css_selector("#memberTradeStat > ul > li.active > a").click()#七天
		driver.find_element_by_css_selector("#memberTradeStat > ul > li:nth-child(2) > a").click()#30天
		driver.find_element_by_css_selector("#memberTradeStat > ul > li:nth-child(3) > a").click()#三个月
		driver.find_element_by_css_selector("#memberTradeStat > ul > li:nth-child(4) > a").click()#一年
		#滚动条至顶部
		#js="var q=document.documentElement.scrollTop=0"
		#driver.execute_async_script(js)
		#time.sleep(3)
		#显示隐藏ul列表，防止获取元素失败
		js1='$(".header-list").show()'
		driver.execute_script(js1)
		#会员体系切换
		h=driver.find_element_by_css_selector("#page_userinfo > a.header-username")
		h.find_element_by_css_selector("#page_userinfo > a.header-username > ul > li:nth-child(2)").click()
