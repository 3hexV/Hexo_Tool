# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ht_gui_help.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 631)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 801, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 791, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 791, 561))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_2.addWidget(self.textBrowser_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout_2.addWidget(self.textBrowser_5, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout_2.addWidget(self.textBrowser_6, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "hexo文件结构"))
        self.label_2.setText(_translate("Dialog", "hexo基本命令"))
        self.label.setText(_translate("Dialog", "如何安装hexo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.label_6.setText(_translate("Dialog", "hexo一键部署"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
