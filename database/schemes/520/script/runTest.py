# coding:utf-8
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script import addPathToPython, initSettings, selectModel

addPathToPython()
initSettings()
selectModel()

from SRC.main import Main

Main('管理端-首页.xml').run()
Main('管理端-账号管理.xml').run()
Main('管理端-站点设置.xml').run()
Main('管理端-物流管理.xml').run()
Main('管理端-数据分析.xml').run()
Main('管理端-商城设置.xml').run()
Main('管理端-会员中心.xml').run()
Main('管理端-商品信息.xml').run()
Main('管理端-促销管理.xml').run()
