# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonScript\PythonWorkspace\easyTest\tool\project\ui_designer\paramEdit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 600)
        Dialog.setMinimumSize(QtCore.QSize(260, 600))
        Dialog.setMaximumSize(QtCore.QSize(260, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/cog.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.tableWidget_param = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_param.setGeometry(QtCore.QRect(0, 0, 261, 571))
        self.tableWidget_param.setAlternatingRowColors(True)
        self.tableWidget_param.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_param.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_param.setObjectName("tableWidget_param")
        self.tableWidget_param.setColumnCount(4)
        self.tableWidget_param.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_param.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_param.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_param.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_param.setHorizontalHeaderItem(3, item)
        self.tableWidget_param.verticalHeader().setVisible(False)
        self.pushButton_reset = QtWidgets.QPushButton(Dialog)
        self.pushButton_reset.setGeometry(QtCore.QRect(140, 570, 60, 30))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(0, 570, 70, 30))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_remove = QtWidgets.QPushButton(Dialog)
        self.pushButton_remove.setGeometry(QtCore.QRect(70, 570, 70, 30))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(200, 570, 60, 30))
        self.pushButton_save.setObjectName("pushButton_save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "编辑参数"))
        item = self.tableWidget_param.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "序号"))
        item = self.tableWidget_param.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget_param.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "VALUE"))
        item = self.tableWidget_param.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "描述"))
        self.pushButton_reset.setText(_translate("Dialog", "重置"))
        self.pushButton_add.setText(_translate("Dialog", "增加一行"))
        self.pushButton_remove.setText(_translate("Dialog", "移除一行"))
        self.pushButton_save.setText(_translate("Dialog", "保存"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

