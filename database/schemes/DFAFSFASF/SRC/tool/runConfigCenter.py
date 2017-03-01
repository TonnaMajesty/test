import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/').split('/SRC')[0])

from PyQt5.QtWidgets import QApplication

from SRC.tool.project.ui_designer.configCenter import ConfigCenter

app = QApplication(sys.argv)
dlg = ConfigCenter()
dlg.show()
dlg.windowMove()
sys.exit(app.exec_())
