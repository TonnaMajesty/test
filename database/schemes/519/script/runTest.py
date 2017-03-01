# coding:utf-8
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script import addPathToPython, initSettings, selectModel

addPathToPython()
initSettings()
selectModel()

from SRC.main import Main

Main('前端2.xml').run()
Main('前端.xml').run()
Main('退货流程4.xml').run()
Main('退货流程3.xml').run()
Main('退货流程2.xml').run()
Main('退货流程1.xml').run()
Main('前端-订单流程.xml').run()
