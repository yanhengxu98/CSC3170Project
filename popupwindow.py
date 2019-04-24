# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popupwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 521)
        self.FCode = QtWidgets.QLabel(Form)
        self.FCode.setGeometry(QtCore.QRect(40, 50, 71, 21))
        self.FCode.setObjectName("FCode")
        self.FligtID = QtWidgets.QLabel(Form)
        self.FligtID.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.FligtID.setObjectName("FligtID")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.FCode.setText(_translate("Form", "Flight Code"))
        self.FligtID.setText(_translate("Form", "Flight ID"))

