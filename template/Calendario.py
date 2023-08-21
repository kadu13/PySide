# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Calendario(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(339, 264)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Calendario = QCalendarWidget(Dialog)
        self.Calendario.setObjectName(u"Calendario")

        self.gridLayout.addWidget(self.Calendario, 0, 0, 1, 1)

        self.data = QLabel(Dialog)
        self.data.setObjectName(u"data")
        self.data.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.data, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.Calendario.selectionChanged.connect(self.Calendario.showSelectedDate)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Calendario", None))
    # retranslateUi

