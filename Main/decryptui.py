# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decrypt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(467, 597)
        self.cipherText = QtWidgets.QTextEdit(Dialog)
        self.cipherText.setGeometry(QtCore.QRect(30, 60, 401, 71))
        self.cipherText.setObjectName("cipherText")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 455, 61, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButtonDe = QtWidgets.QPushButton(Dialog)
        self.pushButtonDe.setGeometry(QtCore.QRect(180, 420, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButtonDe.setFont(font)
        self.pushButtonDe.setObjectName("pushButtonDe")
        self.pushButtonBc = QtWidgets.QPushButton(Dialog)
        self.pushButtonBc.setGeometry(QtCore.QRect(380, 550, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButtonBc.setFont(font)
        self.pushButtonBc.setObjectName("pushButtonBc")
        self.plainTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.plainTextBrowser.setGeometry(QtCore.QRect(30, 480, 401, 71))
        self.plainTextBrowser.setObjectName("plainTextBrowser")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 60, 16))
        self.label_4.setObjectName("label_4")
        self.priN = QtWidgets.QTextEdit(Dialog)
        self.priN.setGeometry(QtCore.QRect(30, 170, 401, 101))
        self.priN.setObjectName("priN")
        self.priP = QtWidgets.QTextEdit(Dialog)
        self.priP.setGeometry(QtCore.QRect(30, 300, 401, 101))
        self.priP.setObjectName("priP")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "解密"))
        self.cipherText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "请在此输入要解密的文字："))
        self.label_2.setText(_translate("Dialog", "明文："))
        self.pushButtonDe.setText(_translate("Dialog", "解密"))
        self.pushButtonBc.setText(_translate("Dialog", "返回主菜单"))
        self.label_3.setText(_translate("Dialog", "p:"))
        self.label_4.setText(_translate("Dialog", "n:"))
