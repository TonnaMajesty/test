# coding=utf-8
from selenium.webdriver import ActionChains

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

		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[1]/upmark').click();  # 点击站点设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[2]/a').click();  # 点击模板管理

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/button').click();  # 点击模板下载
		driver.find_element_by_xpath('//*[@id="callback"]').click();  # 点击返回
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[5]/a[3]').click();  # 点击启用
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click();  # 点击确定
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click();  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[5]/a[2]').click();  # 点击编辑
		driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/button[2]').click();  # 点击确定
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[5]/a[4]').click();  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click();  # 点击确定
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click();  # 点击确定

		# 模板布局设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[2]/td[5]/a[1]').click();  # 点击第二行页面
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]/a[1]').click();  # 点击第一行布局
		driver.switch_to_window(driver.window_handles[1]);
		driver.find_element_by_xpath('//*[@id="container"]/nav/div[1]/form/button[4]').click() # 点击版本
		#driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div[2]/div/div/table/tbody/tr/td[4]/a[3]').click();  # 点击切换
		driver.find_element_by_css_selector("""#ngdialog1 > div.ngdialog-content > div.modal-body > div > div > table > tbody > tr > td.text-center > a:nth-child(3)""").click();  # 点击切换
		driver.find_element_by_xpath('//*[@id="container"]/nav/div[1]/form/button[4]').click()  # 点击版本
		#driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/div/div/table/tbody/tr/td[4]/a[1]').click();  # 点击编辑
		driver.find_element_by_css_selector("""#ngdialog1 > div.ngdialog-content > div.modal-body > div > div > table > tbody > tr > td.text-center > a:nth-child(1)""").click();  # 点击编辑
		# element = driver.find_element_by_xpath('//*[@id="collapseOne"]/div[1]/div[1]/img[2]');
		# target = driver.find_element_by_xpath('//*[@id="container"]/div[2]');
		# ActionChains(driver).drag_and_drop(element, target).perform();  # 拖动布局
		#
		# driver.find_element_by_xpath('//*[@id="panel"]/div[1]').click();  # 点击布局
		# driver.find_element_by_xpath('//*[@id="panel"]/div[3]/h2').click();  # 点击模板挂件
		#
		# element = driver.find_element_by_xpath('//*[@id="collapseTwo"]/div[1]/div[1]/img');
		# target = driver.find_element_by_xpath('//*[@id="12"]');
		# ActionChains(driver).drag_and_drop(element, target).perform();  # 拖动布局
		'''
		driver.find_element_by_xpath('//*[@class="button color-teal btn-saveversion"]').click();  # 点击保存为新版本
		driver.find_element_by_xpath('//input[@class="modal-text-input"]').send_keys(u'版本1.0');  # 输入新版本名称
		driver.find_element_by_xpath('//span[@class="modal-button modal-button-bold"]').click();  # 点击OK
		driver.switch_to_alert().accept()
		'''
		# driver.find_element_by_xpath('//*[@id="12"]/div/div[2]/a/img').click();  # 点击删除
		# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/a/img').click();  # 点击删除
		driver.find_element_by_xpath('//button[@class="btn btn-info btn-submit"]').click(2);  # 点击保存布局/版本
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		# driver.switch_to_alert().accept()
		# driver.find_element_by_xpath('//*[@id="container"]/nav/div[1]/form/button[4]').click();  # 点击版本

		# driver.find_element_by_xpath('//*[@id="ngdialog7"]/div[2]/div[2]/div/div/table/tbody/tr[3]/td[4]/a[2]').click();  # 点击第三行删除
		# driver.find_element_by_xpath('//*[@id="container"]/nav/div[1]/form/button[2]').click();  # 点击预览
		# driver.find_element_by_xpath('//*[@class="button color-teal btn-reset"]').click(3);  # 点击回复默认

		# 设置模板挂件内容
		# driver.find_element_by_xpath('//*[@id="panel"]/div[1]/h2').click();  # 点击布局
		# driver.find_element_by_xpath('//*[@id="panel"]/div[3]/h2').click();  # 点击模板挂件
		#
		# element = driver.find_element_by_xpath('//*[@id="collapseTwo"]/div[7]/div[1]/img');
		# target = driver.find_element_by_xpath('//*[@id="6"]');
		# ActionChains(driver).drag_and_drop(element, target).perform();  # 拖动轮播图


		# driver.find_element_by_xpath('//*[@id="6"]/div[1]/div[2]/span').click();  # 点击编辑
		# driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(u'500');  # 输入高度
		# driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[3]/button').click();  # 点击保存
		#
		# element = driver.find_element_by_xpath('//*[@id="collapseTwo"]/div[9]/div[1]/img');
		# target = driver.find_element_by_xpath('//*[@id="6"]');
		# ActionChains(driver).drag_and_drop(element, target).perform();  # 拖动公告栏
		#
		# driver.find_element_by_xpath('//*[@id="6"]/div[1]/div[2]/span').click();  # 公告栏点击编辑
		# driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/div/div/input').send_keys(u'600');  # 输入高度
		# driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[3]/button').click();  # 点击保存
		#
		# element = driver.find_element_by_xpath('//*[@id="collapseTwo"]/div[5]/div[1]/img');
		# target = driver.find_element_by_xpath('//*[@id="6"]');
		# ActionChains(driver).drag_and_drop(element, target).perform();  # 拖动图文编辑
		#
		# driver.find_element_by_xpath('//*[@id="6"]/div[2]/div[2]/span').click();  # 点击图文编辑的编辑按钮
		# driver.find_element_by_xpath('//*[@id="myEditor0533408149944441"]').send_keys(u'安大达');  # 输入编辑的内容
		# driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[3]/div[2]/div/button').click();  # 点击保存
		#
		# element = driver.find_element_by_xpath('//*[@id="collapseTwo"]/div[6]/div[1]/img');
		# target = driver.find_element_by_xpath('//*[@id="6"]');
		# ActionChains(driver).drag_and_drop(element, target).perform();  # 拖动商品列表
		# driver.find_element_by_xpath('//*[@id="6"]/div[2]/div[2]/span').click();  # 点击商品列表的编辑按钮