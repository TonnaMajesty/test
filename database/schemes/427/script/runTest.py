# coding:utf-8
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script import addPathToPython, initSettings, selectModel

addPathToPython()
initSettings()
selectModel()

from SRC.main import Main

Main('U易联企业号_应用_菜单模板.xml').run()
Main('U易联企业号_应用_服务功能.xml').run()
Main('U易联企业号_应用_打卡记录.xml').run()
Main('U易联企业号_应用_服务源注册.xml').run()
Main('U易联企业号_应用_会议室管理.xml').run()
Main('U易联企业号_应用_应用管理.xml').run()
Main('U易联企业号_微信_企业号绑定.xml').run()
Main('U易联企业号_微信_群发消息.xml').run()
Main('U易联企业号_微信_微信菜单.xml').run()
Main('U易联企业号_素材_单图文消息.xml').run()
Main('U易联企业号_素材_多图文消息.xml').run()
Main('U易联企业号_素材_文本消息.xml').run()
Main('U易联企业号_设置_操作员管理.xml').run()
Main('U易联企业号_设置_短信设置.xml').run()
Main('U易联企业号_设置_站内消息.xml').run()
Main('U易联企业号_设置_账户信息.xml').run()
