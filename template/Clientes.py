# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clientes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Clientes(object):
    def setupUi(self, Clientes):
        if not Clientes.objectName():
            Clientes.setObjectName(u"Clientes")
        Clientes.resize(634, 603)
        Clientes.setStyleSheet(u"background-color: rgb(255, 0, 255);")
        self.gridLayout_3 = QGridLayout(Clientes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_Voltar = QPushButton(Clientes)
        self.btn_Voltar.setObjectName(u"btn_Voltar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Voltar.sizePolicy().hasHeightForWidth())
        self.btn_Voltar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Voltar.setFont(font)
        self.btn_Voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Voltar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 127);\n"
" 	border-radius: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 255);\n"
"	color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"")
        self.btn_Voltar.setIconSize(QSize(45, 45))
        self.btn_Voltar.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_Voltar)

        self.label = QLabel(Clientes)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.frame = QFrame(Clientes)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.L_Data = QLineEdit(self.frame)
        self.L_Data.setObjectName(u"L_Data")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.L_Data.setFont(font2)
        self.L_Data.setCursor(QCursor(Qt.ArrowCursor))
        self.L_Data.setCursorPosition(0)

        self.gridLayout_2.addWidget(self.L_Data, 1, 3, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.btn_Excluir = QPushButton(self.frame)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_Excluir.setFont(font3)
        self.btn_Excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Excluir.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/image/imagens/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon)
        self.btn_Excluir.setIconSize(QSize(45, 36))

        self.gridLayout_2.addWidget(self.btn_Excluir, 1, 7, 1, 1)

        self.btn_Salvar = QPushButton(self.frame)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        self.btn_Salvar.setFont(font3)
        self.btn_Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/image/imagens/media-floppy.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon1)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.gridLayout_2.addWidget(self.btn_Salvar, 1, 5, 1, 1)

        self.btn_Calendario = QPushButton(self.frame)
        self.btn_Calendario.setObjectName(u"btn_Calendario")
        self.btn_Calendario.setFont(font3)
        self.btn_Calendario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Calendario.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/image/imagens/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Calendario.setIcon(icon2)
        self.btn_Calendario.setIconSize(QSize(45, 45))

        self.gridLayout_2.addWidget(self.btn_Calendario, 1, 4, 1, 1)

        self.L_Id = QLineEdit(self.frame)
        self.L_Id.setObjectName(u"L_Id")
        self.L_Id.setFont(font2)
        self.L_Id.setCursorPosition(0)

        self.gridLayout_2.addWidget(self.L_Id, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)

        self.btn_Editar = QPushButton(self.frame)
        self.btn_Editar.setObjectName(u"btn_Editar")
        self.btn_Editar.setFont(font3)
        self.btn_Editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Editar.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/image/imagens/editar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Editar.setIcon(icon3)
        self.btn_Editar.setIconSize(QSize(45, 45))

        self.gridLayout_2.addWidget(self.btn_Editar, 1, 6, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(Clientes)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.L_Nome = QLineEdit(self.frame_2)
        self.L_Nome.setObjectName(u"L_Nome")
        self.L_Nome.setFont(font2)
        self.L_Nome.setCursorPosition(0)

        self.gridLayout.addWidget(self.L_Nome, 0, 1, 1, 2)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)

        self.L_Telefone = QLineEdit(self.frame_2)
        self.L_Telefone.setObjectName(u"L_Telefone")
        self.L_Telefone.setFont(font2)
        self.L_Telefone.setCursorPosition(0)

        self.gridLayout.addWidget(self.L_Telefone, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)

        self.L_Endereco = QLineEdit(self.frame_2)
        self.L_Endereco.setObjectName(u"L_Endereco")
        self.L_Endereco.setFont(font2)
        self.L_Endereco.setCursorPosition(0)

        self.gridLayout.addWidget(self.L_Endereco, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 1)

        self.Tab_CadClientes = QTableWidget(Clientes)
        if (self.Tab_CadClientes.columnCount() < 5):
            self.Tab_CadClientes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.Tab_CadClientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.Tab_CadClientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.Tab_CadClientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.Tab_CadClientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.Tab_CadClientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Tab_CadClientes.setObjectName(u"Tab_CadClientes")

        self.gridLayout_3.addWidget(self.Tab_CadClientes, 3, 0, 1, 1)

        QWidget.setTabOrder(self.L_Id, self.L_Data)
        QWidget.setTabOrder(self.L_Data, self.L_Nome)
        QWidget.setTabOrder(self.L_Nome, self.L_Telefone)
        QWidget.setTabOrder(self.L_Telefone, self.L_Endereco)
        QWidget.setTabOrder(self.L_Endereco, self.btn_Salvar)
        QWidget.setTabOrder(self.btn_Salvar, self.btn_Excluir)
        QWidget.setTabOrder(self.btn_Excluir, self.btn_Calendario)
        QWidget.setTabOrder(self.btn_Calendario, self.Tab_CadClientes)

        self.retranslateUi(Clientes)

        self.btn_Voltar.setDefault(False)


        QMetaObject.connectSlotsByName(Clientes)
    # setupUi

    def retranslateUi(self, Clientes):
        Clientes.setWindowTitle(QCoreApplication.translate("Clientes", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.btn_Voltar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Voltar.setText(QCoreApplication.translate("Clientes", u"   <|  Voltar  ", None))
        self.label.setText(QCoreApplication.translate("Clientes", u"Clientes", None))
        self.L_Data.setInputMask("")
        self.L_Data.setPlaceholderText(QCoreApplication.translate("Clientes", u"Data", None))
        self.label_3.setText(QCoreApplication.translate("Clientes", u"ID", None))
#if QT_CONFIG(tooltip)
        self.btn_Excluir.setToolTip(QCoreApplication.translate("Clientes", u"Excluir", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Excluir.setText(QCoreApplication.translate("Clientes", u"Excluir", None))
#if QT_CONFIG(tooltip)
        self.btn_Salvar.setToolTip(QCoreApplication.translate("Clientes", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Salvar.setText(QCoreApplication.translate("Clientes", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.btn_Calendario.setToolTip(QCoreApplication.translate("Clientes", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Calendario.setText("")
        self.label_2.setText(QCoreApplication.translate("Clientes", u"Data", None))
#if QT_CONFIG(tooltip)
        self.btn_Editar.setToolTip(QCoreApplication.translate("Clientes", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Editar.setText(QCoreApplication.translate("Clientes", u"Editar", None))
        self.label_4.setText(QCoreApplication.translate("Clientes", u"Nome:", None))
        self.label_5.setText(QCoreApplication.translate("Clientes", u"Telefone:", None))
        self.L_Telefone.setInputMask("")
        self.label_6.setText(QCoreApplication.translate("Clientes", u"Endere\u00e7o:", None))
        ___qtablewidgetitem = self.Tab_CadClientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Clientes", u"ID", None));
        ___qtablewidgetitem1 = self.Tab_CadClientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Clientes", u"Data", None));
        ___qtablewidgetitem2 = self.Tab_CadClientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Clientes", u"Nome", None));
        ___qtablewidgetitem3 = self.Tab_CadClientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Clientes", u"Telefone", None));
        ___qtablewidgetitem4 = self.Tab_CadClientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Clientes", u"Endere\u00e7o", None));
    # retranslateUi

