# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_db.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_Db_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 231)
        self.title = QtWidgets.QComboBox(Form)
        self.title.setGeometry(QtCore.QRect(20, 20, 301, 22))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(120, 60, 201, 20))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(120, 90, 81, 81))
        self.image.setStyleSheet("")
        self.image.setText("")
        self.image.setObjectName("image")
        self.btnChange = QtWidgets.QPushButton(Form)
        self.btnChange.setGeometry(QtCore.QRect(220, 100, 101, 23))
        self.btnChange.setObjectName("btnChange")
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(20, 190, 141, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setGeometry(QtCore.QRect(180, 190, 141, 23))
        self.btnDelete.setObjectName("btnDelete")
        self.btnDefault = QtWidgets.QPushButton(Form)
        self.btnDefault.setGeometry(QtCore.QRect(220, 140, 101, 23))
        self.btnDefault.setObjectName("btnDefault")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Изменить базу данных"))

        self.label.setText(_translate("Form", "Название:"))
        self.label_3.setText(_translate("Form", "Изображение:"))
        self.btnChange.setText(_translate("Form", "Изменить"))
        self.btnSave.setText(_translate("Form", "Сохранить"))
        self.btnDelete.setText(_translate("Form", "Удалить"))
        self.btnDefault.setText(_translate("Form", "Стандартное"))