# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_fridge.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_Fridge_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 141)
        self.title = QtWidgets.QComboBox(Form)
        self.title.setGeometry(QtCore.QRect(20, 20, 301, 22))
        self.title.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.title.setObjectName("title")
        self.date = QtWidgets.QDateEdit(Form)
        self.date.setGeometry(QtCore.QRect(120, 60, 110, 22))
        self.date.setObjectName("date")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(20, 100, 141, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setGeometry(QtCore.QRect(180, 100, 141, 23))
        self.btnDelete.setObjectName("btnDelete")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Изменить холодильник"))

        self.label_2.setText(_translate("Form", "Срок годности:"))
        self.btnSave.setText(_translate("Form", "Сохранить"))
        self.btnDelete.setText(_translate("Form", "Удалить"))
