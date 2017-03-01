# coding=utf-8
from time import sleep

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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[4]/a').click();  # 点击站点信息
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[1]/div/input').clear();
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[1]/div/input').send_keys(u'家家乐');  # 输入站点名称
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[2]/div/input').clear();
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[2]/div/input').send_keys(u'123445');  # 输入备案号
		driver.find_element_by_xpath('//*[@style="width: 619px; height: 400px; z-index: 999;"]').clear();
		driver.find_element_by_xpath('//*[@style="width: 619px; height: 400px; z-index: 999;"]').send_keys(u'快乐就是简单快速');  # 输入底部信息
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[2]/div/button').click();  # 点击保存

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/ul/li[2]/a').click();  # 点击联系方式
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[2]/span').click();  # 点击笔图案
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[1]/input').clear();
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[1]/input').send_keys(u'10086');
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[2]/span').click();  # 点击‘√’
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[1]/div/a').click();  # 点击上传
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[1]/div/input').send_keys('E:\\tupian\\hhhhhh.jpg');
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[3]/div[1]/input').send_keys(u'黑寡妇');  # 输入文字说明
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[3]/div[2]/button').click();  # 点击保存
		sleep(3)