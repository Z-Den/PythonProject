# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instruction.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instruction_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 401)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 361, 361))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Инструкция"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Настройки</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">С помощью настроек Вы можете кастомизировать интерфейс программы. Каждая из трёх кнопок отвечает за цвет одного блока отображения продуктов питания главного окна (далее — холодильник): первая кнопка отвечает за </span><span style=\" font-size:8pt; color:#436e43;\">верхний блок</span><span style=\" font-size:8pt;\">, вторая — за </span><span style=\" font-size:8pt; color:#8c8871;\">средний</span><span style=\" font-size:8pt;\">, третья — за </span><span style=\" font-size:8pt; color:#965050;\">нижний</span><span style=\" font-size:8pt;\">. Чтобы выбрать желаемый цвет, нажмите на кнопку выбора цвета. Чтобы вернуть стандартные цвета, нажмите на кнопку «</span><span style=\" font-size:8pt; text-decoration: underline;\">Сбросить цвета</span><span style=\" font-size:8pt;\">».</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Холодильник</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Интерфейс холодильника представляет собой три блока. В первом отображаются продукты питания, срок годности которых в ближайшие дни не истекает, во втором — продукты, чей срок годности истекает через один-два дня, в третьем — с истёкшим сроком годности.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Конвертация в txt</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Кнопки «</span><span style=\" font-size:8pt; text-decoration: underline;\">Холодильник в txt</span><span style=\" font-size:8pt;\">» и «</span><span style=\" font-size:8pt; text-decoration: underline;\">БД в txt</span><span style=\" font-size:8pt;\">» позволяют представить содержимое холодильника и базы данных всех добавенных продуктов в текстовом файле. При успешном конвертировании на кнопке появится галочка (она пропадёт при следующем обновлении холодильника).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Удаление просроченных продуктов</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Кнопка «</span><span style=\" font-size:8pt; text-decoration: underline;\">Удалить просроченные</span><span style=\" font-size:8pt;\">» удаляет все продукты с истёкшим сроком годности из холодильника.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Изменение</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Открытие окон изменения базы данных продуктов и холодильника осуществляется с помощью кнопок «</span><span style=\" font-size:8pt; text-decoration: underline;\">Изменить БД</span><span style=\" font-size:8pt;\">» и «</span><span style=\" font-size:8pt; text-decoration: underline;\">Изменить холодильник</span><span style=\" font-size:8pt;\">» соответственно. К изменению доступны изображение и название продукта (в БД), дата окончания срока годности (в холодильнике). </span><span style=\" font-size:8pt; font-weight:600;\">При удалении из БД продукт удаляется и из холодильника!</span><span style=\" font-size:8pt;\"> Все изменения вступят в силу после сохранения.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Добавление</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Кнопка «</span><span style=\" font-size:8pt; text-decoration: underline;\">Добавить известный</span><span style=\" font-size:8pt;\">» позволяет добавить в холодильник продукт, который уже есть в БД. Кнопка «</span><span style=\" font-size:8pt; text-decoration: underline;\">Добавить новый</span><span style=\" font-size:8pt;\">» добавляет новый продукт в БД и в холодильник.</span></p></body></html>"))
