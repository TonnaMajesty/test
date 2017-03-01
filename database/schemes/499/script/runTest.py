# coding:utf-8
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script import addPathToPython, initSettings, selectModel

addPathToPython()
initSettings()
selectModel()

from SRC.main import Main

Main('退货流程1.xml').run()
