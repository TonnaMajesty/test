# coding:utf-8
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script import addPathToPython, initSettings, selectModel

addPathToPython()
initSettings()
selectModel()

from SRC.main import Main

Main('线索.xml').run()
Main('系统日志.xml').run()
Main('联系人.xml').run()
Main('客户汇总表.xml').run()
Main('客户自定义字段.xml').run()
Main('客户列表.xml').run()
Main('客户统计表.xml').run()
Main('考勤.xml').run()
