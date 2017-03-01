# coding=utf-8
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
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[1]/upmark').click();  # 点击站点设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[5]/a').click();  # 点击首页广告图片

		driver.find_element_by_xpath('//input[@class="btn btn-info ng-pristine ng-untouched ng-valid"]').click();  # 点击上传图片
		driver.find_element_by_xpath('//*[@id="indexAdImage"]/div[2]/div[2]/input[1]').send_keys('E:\\tupian\\quyeba3.jpg');  # 上传图片
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口

		driver.find_element_by_xpath('//input[@ng-model="adEntity.iOrder"]').send_keys(u'1');  # 输入显示顺序
		driver.find_element_by_xpath('//input[@ng-model="adEntity.cRedirectUrl"]').send_keys('www.baidu.com');
		driver.find_element_by_xpath('//*[@class="form-control ng-pristine ng-untouched ng-valid ng-valid-maxlength"]').send_keys(u'好图');
		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(3);  # 点击保存
		driver.find_element_by_xpath('//*[@id="indexAdImage"]/div[7]/div/table/tbody/tr[1]/td[5]/a[1]').click();  # 点击编辑
		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(3);  # 点击保存
		driver.find_element_by_xpath('//*[@id="indexAdImage"]/div[7]/div/table/tbody/tr[1]/td[5]/a[2]').click();  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(3);  # 点击确定