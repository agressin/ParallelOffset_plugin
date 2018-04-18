# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_paralleloffset.ui'
#
# Created: Tue Jul 23 12:41:12 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



def _fromUtf8(s):
    return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_ParallelOffset(object):
    def setupUi(self, ParallelOffset):
        ParallelOffset.setObjectName(_fromUtf8("ParallelOffset"))
        ParallelOffset.resize(344, 310)
        self.buttonBox = QDialogButtonBox(ParallelOffset)
        self.buttonBox.setGeometry(QRect(-20, 260, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.txtDistance = QLineEdit(ParallelOffset)
        self.txtDistance.setGeometry(QRect(230, 20, 81, 20))
        font = QFont()
        font.setPointSize(10)
        self.txtDistance.setFont(font)
        self.txtDistance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtDistance.setObjectName(_fromUtf8("txtDistance"))
        self.label = QLabel(ParallelOffset)
        self.label.setGeometry(QRect(20, 20, 201, 16))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QLabel(ParallelOffset)
        self.label_2.setGeometry(QRect(20, 70, 141, 16))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gbDirection = QGroupBox(ParallelOffset)
        self.gbDirection.setGeometry(QRect(230, 70, 81, 61))
        self.gbDirection.setTitle(_fromUtf8(""))
        self.gbDirection.setObjectName(_fromUtf8("gbDirection"))
        self.radLeft = QRadioButton(self.gbDirection)
        self.radLeft.setGeometry(QRect(10, 10, 82, 18))
        self.radLeft.setChecked(True)
        self.radLeft.setObjectName(_fromUtf8("radLeft"))
        self.radRight = QRadioButton(self.gbDirection)
        self.radRight.setGeometry(QRect(10, 30, 82, 18))
        self.radRight.setObjectName(_fromUtf8("radRight"))
        self.label_3 = QLabel(ParallelOffset)
        self.label_3.setGeometry(QRect(20, 150, 171, 16))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gbMethod = QGroupBox(ParallelOffset)
        self.gbMethod.setGeometry(QRect(230, 150, 81, 81))
        self.gbMethod.setTitle(_fromUtf8(""))
        self.gbMethod.setObjectName(_fromUtf8("gbMethod"))
        self.radRound = QRadioButton(self.gbMethod)
        self.radRound.setGeometry(QRect(10, 10, 82, 18))
        self.radRound.setChecked(True)
        self.radRound.setObjectName(_fromUtf8("radRound"))
        self.radMitre = QRadioButton(self.gbMethod)
        self.radMitre.setGeometry(QRect(10, 30, 82, 18))
        self.radMitre.setObjectName(_fromUtf8("radMitre"))
        self.radBevel = QRadioButton(self.gbMethod)
        self.radBevel.setGeometry(QRect(10, 50, 82, 18))
        self.radBevel.setObjectName(_fromUtf8("radBevel"))

        self.retranslateUi(ParallelOffset)
        self.buttonBox.accepted.connect(ParallelOffset.accept)
        self.buttonBox.rejected.connect(ParallelOffset.accept)
        #QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("accepted()")), ParallelOffset.accept)
        #QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("rejected()")), ParallelOffset.reject)
        QMetaObject.connectSlotsByName(ParallelOffset)

    def retranslateUi(self, ParallelOffset):
        ParallelOffset.setWindowTitle(_translate("ParallelOffset", "ParallelOffset", None))
        self.txtDistance.setText(_translate("ParallelOffset", "0", None))
        self.label.setText(_translate("ParallelOffset", "Enter the offset distance (meters)", None))
        self.label_2.setText(_translate("ParallelOffset", "Enter the offset side", None))
        self.radLeft.setText(_translate("ParallelOffset", "Left", None))
        self.radRight.setText(_translate("ParallelOffset", "Right", None))
        self.label_3.setText(_translate("ParallelOffset", "Enter the offset line method", None))
        self.radRound.setText(_translate("ParallelOffset", "Round", None))
        self.radMitre.setText(_translate("ParallelOffset", "Mitre", None))
        self.radBevel.setText(_translate("ParallelOffset", "Bevel", None))

