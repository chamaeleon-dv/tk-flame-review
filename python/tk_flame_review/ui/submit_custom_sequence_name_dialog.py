# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submit_custom_sequence_name_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_SubmitCustomSequenceNameDialog(object):
    def setupUi(self, SubmitCustomSequenceNameDialog):
        SubmitCustomSequenceNameDialog.setObjectName("SubmitCustomSequenceNameDialog")
        SubmitCustomSequenceNameDialog.resize(487, 419)
        self.verticalLayout = QtGui.QVBoxLayout(SubmitCustomSequenceNameDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(SubmitCustomSequenceNameDialog)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/tk-flame-export/ui_splash.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(SubmitCustomSequenceNameDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.shotgun_sequencename = QtGui.QLineEdit(SubmitCustomSequenceNameDialog)
        self.shotgun_sequencename.setObjectName("shotgun_sequencename")
        self.verticalLayout.addWidget(self.shotgun_sequencename)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(368, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel = QtGui.QPushButton(SubmitCustomSequenceNameDialog)
        self.cancel.setAutoDefault(False)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.submit = QtGui.QPushButton(SubmitCustomSequenceNameDialog)
        self.submit.setCheckable(False)
        self.submit.setDefault(True)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SubmitCustomSequenceNameDialog)
        QtCore.QMetaObject.connectSlotsByName(SubmitCustomSequenceNameDialog)

    def retranslateUi(self, SubmitCustomSequenceNameDialog):
        SubmitCustomSequenceNameDialog.setWindowTitle(QtGui.QApplication.translate("SubmitCustomSequenceNameDialog", "Submit to Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SubmitCustomSequenceNameDialog", "Connect to following Sequence in Shotgun:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("SubmitCustomSequenceNameDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("SubmitCustomSequenceNameDialog", "Submit to Shotgun", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
