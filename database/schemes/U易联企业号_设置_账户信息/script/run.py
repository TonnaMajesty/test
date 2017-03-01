import os
import sys
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script import getStartProjectCMD

subprocess.Popen(getStartProjectCMD(), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
