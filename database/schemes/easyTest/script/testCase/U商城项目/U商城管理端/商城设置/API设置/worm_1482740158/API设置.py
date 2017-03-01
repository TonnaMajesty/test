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
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[1]/upmark').click();  # 点击商城设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[10]/a').click();  # 点击API设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/div').click();  # 切换启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/div').click();  # 切换启动状态
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr/td[3]/div/p/a').click();  # 点击编辑
		driver.find_element_by_xpath('//*[@id="clientapi"]/div/ul/li[2]/a').click();  # 点击使用说明
		driver.find_element_by_xpath('//*[@id="clientapi"]/div/ul/li[1]/a').click();  # 点击配置脚本
		driver.find_element_by_xpath('//*[@id="clientapi"]/div/div/div[1]/div/div[2]/div/textarea').clear()
		driver.find_element_by_xpath('//*[@id="clientapi"]/div/div/div[1]/div/div[2]/div/textarea').send_keys(
			'''var apiResult=true;

var ids=[];

var i;

for(i=0;i<validateParams.oOrderDetails.length;i++){

      var iProductID=validateParams.oOrderDetails[i].iProductId;

      ids.push(iProductID);

}

var tags=[];

tags.push("跨境商品");    //商品标签的名称：跨境商品

var proxy = cb.rest.DynamicProxy.create({ isContainAnyTag: { url: 'client/Products/isContainsAnyTag', method: 'POST', options: { token: true, async:false} } });

proxy.isContainAnyTag({'productIds' : ids, 'tagNames' : tags }, function (getErr, getResult) {

      var b= JSON.stringify(getResult);

      if(getResult){

           if(b=="true"){

                 var j;

                 var value;

                 for(j=0;j<validateParams.oOrderCustomItems.length;j++){

                                //cDefine6是订单上--->身份证号自定义项的ID

                      if("cDefine6"==validateParams.oOrderCustomItems[j].cDefineName){

                            value = validateParams.oOrderCustomItems[j].cDefaultValue;

                      }

                 }

                 if(value ==undefined || value==""){

                      alert("您提交的订单中有跨境商品，请输入收货人身份证号");

                      apiResult = false;

                 }

           }

      }



});

return apiResult;
			''');  # 输入执行脚本
		driver.find_element_by_xpath('//*[@id="clientapi"]/div/div/div[1]/div/div[3]/div/button').click();  # 点击保存
		# driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click();  # 点击确定
		sleep(3)