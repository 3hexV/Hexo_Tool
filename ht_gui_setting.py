# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ht_gui_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(681, 191)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.le_web = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_web.setObjectName("le_web")
        self.gridLayout.addWidget(self.le_web, 3, 1, 1, 1)
        self.le_note = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_note.setObjectName("le_note")
        self.gridLayout.addWidget(self.le_note, 1, 1, 1, 1)
        self.le_md = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_md.setObjectName("le_md")
        self.gridLayout.addWidget(self.le_md, 2, 1, 1, 1)
        self.btn_canle = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_canle.setObjectName("btn_canle")
        self.gridLayout.addWidget(self.btn_canle, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 4)
        self.btn_note = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_note.setObjectName("btn_note")
        self.gridLayout.addWidget(self.btn_note, 1, 2, 1, 2)
        self.btn_md = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_md.setObjectName("btn_md")
        self.gridLayout.addWidget(self.btn_md, 2, 2, 1, 2)
        self.btn_web = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_web.setObjectName("btn_web")
        self.gridLayout.addWidget(self.btn_web, 3, 2, 1, 2)
        self.btn_def = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_def.setObjectName("btn_def")
        self.gridLayout.addWidget(self.btn_def, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.btn_note.clicked.connect(Dialog.select_note_exe)
        self.btn_md.clicked.connect(Dialog.select_md_exe)
        self.btn_web.clicked.connect(Dialog.select_web_exe)
        self.btn_save.clicked.connect(Dialog.accept)
        self.btn_canle.clicked.connect(Dialog.reject)
        self.btn_def.clicked.connect(Dialog.select_def)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.le_note, self.btn_note)
        Dialog.setTabOrder(self.btn_note, self.le_md)
        Dialog.setTabOrder(self.le_md, self.btn_md)
        Dialog.setTabOrder(self.btn_md, self.le_web)
        Dialog.setTabOrder(self.le_web, self.btn_web)
        Dialog.setTabOrder(self.btn_web, self.btn_save)
        Dialog.setTabOrder(self.btn_save, self.btn_canle)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "配置"))
        self.label.setText(_translate("Dialog", "文本编辑器："))
        self.le_web.setPlaceholderText(_translate("Dialog", "空表示使用默认浏览器"))
        self.btn_canle.setText(_translate("Dialog", "取消"))
        self.label_2.setText(_translate("Dialog", "Markdown编辑器："))
        self.label_3.setText(_translate("Dialog", "浏览器:"))
        self.btn_save.setText(_translate("Dialog", "保存并应用"))
        self.label_4.setText(_translate("Dialog", "请选择可执行文件，或填写命令（例如notepad)"))
        self.btn_note.setText(_translate("Dialog", "选择"))
        self.btn_md.setText(_translate("Dialog", "选择"))
        self.btn_web.setText(_translate("Dialog", "选择"))
        self.btn_def.setText(_translate("Dialog", "恢复默认"))
