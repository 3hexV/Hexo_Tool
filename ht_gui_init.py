# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ht_gui_init.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(697, 228)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 681, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.le_save = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_save.setObjectName("le_save")
        self.gridLayout.addWidget(self.le_save, 0, 1, 1, 2)
        self.le_github = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_github.setEnabled(False)
        self.le_github.setObjectName("le_github")
        self.gridLayout.addWidget(self.le_github, 3, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_path.setObjectName("le_path")
        self.gridLayout.addWidget(self.le_path, 1, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.select_init_folder)
        self.radioButton_2.clicked['bool'].connect(self.le_github.setDisabled)
        self.radioButton.clicked['bool'].connect(self.le_github.setEnabled)
        self.pushButton_2.clicked.connect(Dialog.accept)
        self.pushButton_3.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton, self.radioButton_2)
        Dialog.setTabOrder(self.radioButton_2, self.radioButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hexo初始化"))
        self.pushButton.setText(_translate("Dialog", "选择文件夹"))
        self.radioButton_2.setText(_translate("Dialog", "本地直接生成"))
        self.radioButton.setText(_translate("Dialog", "来自github仓库"))
        self.label.setText(_translate("Dialog", "hexo生成的文件夹名"))
        self.label_3.setText(_translate("Dialog", "github 仓库"))
        self.label_2.setText(_translate("Dialog", "hexo生成文件夹保存路径"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.pushButton_2.setText(_translate("Dialog", "确定"))
