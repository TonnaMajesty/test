version = '1.0.7'
author = 'Walt'
date = '2016-10-26'
description = '''
version='1.0.7'
author ='Walt'
date ='2016-10-26'
更新说明：
1.目录分离
settings中配置的目录按照SRC（源码），script（脚本）分开
1）目的是script可以出现在任何地方
2）源码支持安装到python下
3）原runTest中的说明备份
4）如果将目录分离需要修改script.__init__.py文件中的src_dir = None，例如：
src_dir = 'D:/迅雷下载/test/bbb' 若使用'\\' 请转义

5）启动方式说明：
1>，Main().run()或Main('').run()：
程序运行后，控制台会有提示，根据选择的编号运行对应的测试方案
2>，Main('测试方案.xml').run()：
'测试方案.xml'配置文件放在script/xml/目录下，程序会自动运行该测试方案
3>，外部传参数的启动：
启动命令后跟参数（xml文件相对路径或绝对路径）
命令行:python runTest.py c:\demo.xml
4>,调出配置测试方案工具：
命令行:python runTest.py CCTT

2.优化日志统计功能，添加百分比

3.webelment的别名去掉了

4.webelement添加对text的装饰器
------------------------------------
version='1.0.6'
author ='Walt'
date ='2016-10-19'
更新说明：
1.修复bug：
查找元素返回空元素对象的时候，该元素对象无法使用test()

2.添加run.py为程序主入口

3.从新定义脚本结果Fail和Error的区别，单纯的找元素如果没找到是失败，进行操作时候失败就是ERROR

4.上传文件：
selenium的send_key方法是支持上传文件的，使用该方法，并且针对本框架进行优化
1）上传文件首先从files目录下的脚本id对应目录下查找，如果没有，判断脚本中提供的上传文件路径是否为
绝对路径，如果不是绝对路径，拼接files目录下的路径，如果最终找不到上传文件，会报出异常
2）解决关闭打开窗口的问题（未实现）

5.重新定义运行模式RUNMODEL
当前含有以下几种模式，根据不同模式，会对setting进行不同的设置
NORMAL:普通模式，参数使用setting中设置的参数
ONLINE:线上模式，针对本公司线上平台而进行的优化
TESTING：测试模式

6.修改BUG ，元素的text属性报错的问题

7.修改报告，多层查找元素，返回空元素继续查找元素报出错误的问题

8.提供了一个查找元素失败，也会返回PASS结果的参数
使用方法：在代码中添加参数’findAssert‘
driver.findElement('定位元素代码','findAssert')

汇总异常错误，程序中可能会出现的异常如下
[ERROR-1001]:读取测试方案配置文件引发的异常.代码位置(SRC.main.Main.loadTestPlanXML)
[ERROR-1002]:解析外部传入的JSON字符串引发的异常.代码位置(SRC.main.Main.setRunType)
[ERROR-1003]:配置场景引发的异常.代码位置(SRC.main.Main.start)
[ERROR-1004]:引入测试方案模块失败引发的异常.代码位置(SRC.unittest.scene.Scene.importTestCase)
[ERROR-1005]:向主机发送JSON字符串引发的异常.代码位置(SRC.common.loga.sendLogToHTTP)
[ERROR-1006]:测试用例管理运行结果统计模块引发的异常.代码位置(SRC.common.loga.manageLogRecord)
[ERROR-1007]:测试用例汇总运行结果统计模块引发的异常.代码位置(SRC.common.loga.getRecordTxt)
[ERROR-1008]:创建浏览器驱动对象失败引发的异常.代码位置(SRC.unittest.scene.Scene.getDriverObj)
[ERROR-1009]:场景中不包含任何测试用例.代码位置(SRC.unittest.scene.Scene.run)
[ERROR-1010]:读取参数化配置文件引发的异常.代码位置(SRC.unittest.scene.Scene.readParamXml)
[ERROR-1011]:向测试单元套件添加测试用例对象时引发的异常.代码位置(SRC.unittest.scene.Scene.suiteFactory)
[ERROR-1012]:测试套件运行失败引发的异常.代码位置(SRC.unittest.scene.run)
[ERROR-1013]:上传文件不存在引发的异常.代码位置(SRC.webdriver.webelement.getUploadFiles)




------------------------------------------
version='1.0.2'
author ='Walt'
date ='2016-10-10'
更新说明：
1.移除源码目录下的config.XML全局配置文件，而使用settings代替
现在全局配置文件的数据以常量的形式保存在settings中

2.优化了源码

3.修改了图片路径：
本地图片路径：相对路径，日期/图片名
服务器数据中图片路径：相对路径,项目名称/script/report/image/日期/图片名

4.测试方案配置文件中scene节点添加sceneid属性,scriptId属性

5.发送服务器数据添加新字段：
状态字段：标记开始，运行中，结束
场景id
脚本id
唯一识别码字段
代码顺序号

6.添加统计结果的功能
按照PASS,FAIL,ERROR,TRUE,FALSE分别统计出累计的次数，输出到日志中

7.完善整套程序的异常处理，程序在运行过程中，会记录到日志中，或者发送给远程服务器

8.添加新功能：友好的测试方案选择方式
runTest.py文件中，如果Main()函数不传入测试方案文件名称或者传入空值，举例如下：
Main().run()
Main('').run()
控制台会调出友好界面，供用户选择当前测试方案目录下现有的配置文件，根据提示选择即可运行

未解决问题：
1.代码中条件调用脚本的问题
2.程序发生错误时候，发送给服务器的日志还没实现（解决）
3.alert后弹出窗口自动处理
4.断言的自动化
5.根据传递参数选择运行方式（本地或远程），并且向服务器发送唯一码(完成)

脚本发送的CODE
{\"jobId\":0,\"payload\":{\"taskId\":\"0\",\"execTaskId\":0,\"tiTaskId\":0,\"timer\":[]},\"browsers\":{\"browserId\":0,\"machineId\":0,\"Chrome\":\"http:\/\/10.10.12.103:4444\/wd\/hub\"},\"requestURL\":\"http:\/\/10.1.214.154:8088\/ext\/log?token=q8E89zRdp\",\"reportId\":0}


你传回来的需要增加
scriptId和schemeId
格式与发送的一致

------------------------------------------------------
version='1.0.1'
author ='Walt'
date ='2016-09-15'
更新说明：
1.将模版放到单独的模版文件夹(/script/template)中
测试方案模版:xml模版.xml
参数化模版：data参数化模版.xml
测试用例模版:testCase模版.py

2.测试方案模版（xml模版.xml）中hub节点和testCase节点添加enabled属性
enabled='True'时 该条目启用；
enabled='False'时，该条目不启用；
向下兼容：如果hub节点和testCase节点不包含enabled属性，则该条目启用

3.修复警告框弹出截图报错的问题
现在接受警告框不会被截图，
如果页面不存在警告框，执行接受警告框代码也不会报异常，会在日志中体现
另外，webdriver的行为操作都不会进行截图

4.重新定义源码中webDriver和webElement的继承规则
自定义的方法放在webdriver_ext和webelement_ext模块的相对应类中
重写后的方法放在webDriver和webElement类中
继承顺序:
selenium中的webdriver>webdriver_ext>webDriver
selenium中的webElement>webelement_ext>webElement

5.在webdriver_ext.WebDriverExt中添加滚屏的方法
driver.windowScrollTo(x,y)

6.修复查找元素失败，后续程序崩溃的问题
在SRC.webdriver.webelement模块中添加WebElementNull类，
在SRC.webdriver.webelement.WebElement类中添加属性‘ISNULLELEMENT’ 该属性的值为布尔型，
当查找元素成功的时候，返回WebElement对象，ISNULLELEMENT的值为False
当查找元素失败的时候，返回WebElementNull对象，ISNULLELEMENT的值为True
代码使用举例：
element=findElementByXX('xxx')
if not element.ISNULLELEMENT:
	定位到元素，执行的后续代码
else:
	没能定位到元素，执行的后续代码

7.暂时屏蔽了验证码识别功能
该功能识别的验证码不准确

8.重新优化了装饰器的代码
优化查找元素的装饰器

9.添加新功能：界面化工具
1）文件对比
2）目录对比
3）配置中心

10.优化测试方案配置文件和测试用例配置文件的配置
详细见本文档最后的三大配置文件配置说明

11.优化了SRC/main.py和SRC/unittest/scene的代码

12.重新设计了webdriver中的切换窗口的方法：
现在不建议使用driver.switch_to_window；
而是用driver.switch_to.window替换；
用法如下：
1）driver.switch_to.window(index)
2）driver.switch_to.window(driver.window_handles[index])
index为窗口索引号，从打开的第一个窗口记录为0号，第二个窗口记录为1号，以此类推
建议使用第一种方法调用

13.优化main类中的代码，抽取公共函数，移动到SRC/common/fileHelper中

14.添加新功能：测试方案下包含多个场景，场景顺序运行
现在的结构：测试方案->场景（场景1，场景2...）->每个场景包含测试用例
在测试方案配置文件中(xml模板.xml)可以配置多个<scene>节点，例如：
<scene description="脚本执行顺序为子标签排列顺序">
	<testCase paramPath="/参数化1.xml">登录</testCase>
	<testCase paramPath="/参数化11.xml">退出</testCase>
</scene>
<scene description="脚本执行顺序为子标签排列顺序">
	<testCase paramPath="/参数化2">登录</testCase>
</scene>
程序会按照scene的先后顺序运行

15.为了配合自动化测试平台，启动方式进行了优化，
CMD运行:python runTest.py 参数1 参数2
无参数：加载config.xml，启动runTest.py中传递的测试方案
有一个参数：参数1是测试方案的绝对路径
有两个参数：参数1是测试方案的绝对路径，参数2是唯一识别码。加载config_remote.xml
唯一识别码为json字符串，解析后包含唯一码，浏览器参数等（未实现）

未解决问题：
1.找不到元素，后面程序崩溃的问题（解决）
2.代码中条件调用脚本的问题
3.程序发生错误时候，发送给服务器的日志还没实现(解决)
4.alert后弹出窗口自动处理
5.gbk中@ 商标符号报错，影响别名，需要修改日志的编码为utf-8 （解决）
6.别名长度控制一下(解决)
7.控制下截图画红框的数量（解决）
8.断言的自动化
'''

configDescription='''
三大配置文件填写说明：
1.测试方案配置文件（xml模版.xml）
1）浏览器配置：
目前支持火狐,谷歌,IE浏览器，配置如下
<hub browser="FF" enabled="False">http://0.0.0.0:5555/wd/hub</hub>
<hub browser="Chrome" enabled="False">http://0.0.0.0:5556/wd/hub</hub>
<hub browser="IE" enabled="False">http://0.0.0.0:5557/wd/hub</hub>
browser属性：浏览器名称。包含火狐(FF),谷歌(Chrome),IE
enableds属性：是否启用。启用(True),不启用(False)
标签内容：remote远程主机地址，本地启动浏览器不起作用，默认即可

2）测试用例配置：
每一个标签表示一个测试用例，配置如下
<testCase paramPath="/项目/登录" enabled="True">/项目/公共/登录</testCase>
paramPath属性：参数化文件路径，支持绝对路径或相对路径。相对路径的默认根目录为'../easyTest/script/data',文件扩展名'.xml',可省略
enableds属性：是否启用。启用(True),不启用(False)
标签内容：测试用例脚本文件相对路径，该文件必须放在项目中script/testCase目录下，文件扩展名'.py',可省略,'/script/testCase/'可省略

2.参数化配置文件(data参数化模板.xml)
每个参数化配置文件对应一个测试用例(testCase模版.py)，配置如下：
<testClass name="EasyCase" description='测试用例类的类名需要对应本标签的name属性'>
	<param id="url" description="">http://umalltest.yonyouup.com/</param>
</testClass>
name属性：对应测试用例脚本中的类名，只有与之对应才能实现参数化,默认测试用例脚本类名都为'EasyCase'
id属性：对应测试用例脚本中的参数化变量名
param标签内容：对应测试用例脚本中，参数化变量是实际值


'''
