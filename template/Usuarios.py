# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        if not Usuarios.objectName():
            Usuarios.setObjectName(u"Usuarios")
        Usuarios.resize(774, 628)
        Usuarios.setStyleSheet(u"background-color: rgb(255, 0, 255);")
        self.gridLayout_3 = QGridLayout(Usuarios)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(Usuarios)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Usuarios)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.L_Id = QLineEdit(self.frame)
        self.L_Id.setObjectName(u"L_Id")
        self.L_Id.setEnabled(False)
        self.L_Id.setFont(font1)

        self.gridLayout_2.addWidget(self.L_Id, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.L_Data = QLineEdit(self.frame)
        self.L_Data.setObjectName(u"L_Data")
        self.L_Data.setFont(font1)

        self.gridLayout_2.addWidget(self.L_Data, 0, 3, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.btn_Salvar = QPushButton(Usuarios)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_Salvar.setFont(font2)
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
        icon = QIcon()
        icon.addFile(u":/image/imagens/Save.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Salvar)

        self.btn_Limpar = QPushButton(Usuarios)
        self.btn_Limpar.setObjectName(u"btn_Limpar")
        self.btn_Limpar.setFont(font2)
        self.btn_Limpar.setStyleSheet(u"QPushButton{\n"
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
"}")
        icon1 = QIcon()
        icon1.addFile(u":/image/imagens/limpar-limpo (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Limpar.setIcon(icon1)
        self.btn_Limpar.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Limpar)

        self.btn_Excluir = QPushButton(Usuarios)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        self.btn_Excluir.setFont(font2)
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
        icon2 = QIcon()
        icon2.addFile(u":/image/imagens/Delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon2)
        self.btn_Excluir.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Excluir)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.frame_2 = QFrame(Usuarios)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.L_Nome = QLineEdit(self.frame_2)
        self.L_Nome.setObjectName(u"L_Nome")
        self.L_Nome.setFont(font1)
        self.L_Nome.setMaxLength(50)

        self.horizontalLayout_2.addWidget(self.L_Nome)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.L_Telefone = QLineEdit(self.frame_2)
        self.L_Telefone.setObjectName(u"L_Telefone")
        self.L_Telefone.setFont(font1)

        self.horizontalLayout_2.addWidget(self.L_Telefone)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.L_Endereco = QLineEdit(self.frame_2)
        self.L_Endereco.setObjectName(u"L_Endereco")
        self.L_Endereco.setFont(font1)
        self.L_Endereco.setMaxLength(80)

        self.horizontalLayout_3.addWidget(self.L_Endereco)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.Cbb_Permicao = QComboBox(self.frame_2)
        self.Cbb_Permicao.addItem("")
        self.Cbb_Permicao.addItem("")
        self.Cbb_Permicao.addItem("")
        self.Cbb_Permicao.setObjectName(u"Cbb_Permicao")
        self.Cbb_Permicao.setFont(font1)

        self.horizontalLayout_3.addWidget(self.Cbb_Permicao)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.L_Usuario = QLineEdit(self.frame_2)
        self.L_Usuario.setObjectName(u"L_Usuario")
        self.L_Usuario.setFont(font1)
        self.L_Usuario.setMaxLength(50)

        self.horizontalLayout_4.addWidget(self.L_Usuario)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.L_Senha = QLineEdit(self.frame_2)
        self.L_Senha.setObjectName(u"L_Senha")
        self.L_Senha.setFont(font1)
        self.L_Senha.setMaxLength(50)

        self.horizontalLayout_4.addWidget(self.L_Senha)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 1)

        self.Tab_Usuarios = QTableWidget(Usuarios)
        if (self.Tab_Usuarios.columnCount() < 8):
            self.Tab_Usuarios.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.Tab_Usuarios.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.Tab_Usuarios.setObjectName(u"Tab_Usuarios")

        self.gridLayout_3.addWidget(self.Tab_Usuarios, 3, 0, 1, 1)

        QWidget.setTabOrder(self.L_Id, self.L_Data)
        QWidget.setTabOrder(self.L_Data, self.L_Nome)
        QWidget.setTabOrder(self.L_Nome, self.L_Telefone)
        QWidget.setTabOrder(self.L_Telefone, self.L_Endereco)
        QWidget.setTabOrder(self.L_Endereco, self.L_Usuario)
        QWidget.setTabOrder(self.L_Usuario, self.L_Senha)
        QWidget.setTabOrder(self.L_Senha, self.Cbb_Permicao)
        QWidget.setTabOrder(self.Cbb_Permicao, self.btn_Salvar)
        QWidget.setTabOrder(self.btn_Salvar, self.btn_Limpar)
        QWidget.setTabOrder(self.btn_Limpar, self.btn_Excluir)
        QWidget.setTabOrder(self.btn_Excluir, self.Tab_Usuarios)

        self.retranslateUi(Usuarios)

        QMetaObject.connectSlotsByName(Usuarios)
    # setupUi

    def retranslateUi(self, Usuarios):
        Usuarios.setWindowTitle(QCoreApplication.translate("Usuarios", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Usuarios", u"Usuarios", None))
        self.label_3.setText(QCoreApplication.translate("Usuarios", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Usuarios", u"Data", None))
        self.L_Data.setInputMask(QCoreApplication.translate("Usuarios", u"00/00/0000", None))
        self.btn_Salvar.setText(QCoreApplication.translate("Usuarios", u"Salvar", None))
        self.btn_Limpar.setText(QCoreApplication.translate("Usuarios", u"Limpar", None))
        self.btn_Excluir.setText(QCoreApplication.translate("Usuarios", u"Excluir", None))
        self.label_4.setText(QCoreApplication.translate("Usuarios", u"Nome:", None))
        self.label_5.setText(QCoreApplication.translate("Usuarios", u"Telefone:", None))
        self.L_Telefone.setInputMask(QCoreApplication.translate("Usuarios", u"(00)00000-0000", None))
        self.label_6.setText(QCoreApplication.translate("Usuarios", u"Endere\u00e7o:", None))
        self.label_9.setText(QCoreApplication.translate("Usuarios", u"Permi\u00e7\u00e3o", None))
        self.Cbb_Permicao.setItemText(0, "")
        self.Cbb_Permicao.setItemText(1, QCoreApplication.translate("Usuarios", u"Administrador", None))
        self.Cbb_Permicao.setItemText(2, QCoreApplication.translate("Usuarios", u"Usu\u00e1rio", None))

        self.label_7.setText(QCoreApplication.translate("Usuarios", u"Usuario", None))
        self.label_8.setText(QCoreApplication.translate("Usuarios", u"Senha", None))
        ___qtablewidgetitem = self.Tab_Usuarios.horizontalHeaderItem(0)  # MUDA A COLUNA
        ___qtablewidgetitem.setText(QCoreApplication.translate("Usuarios", u"ID", None));
        ___qtablewidgetitem1 = self.Tab_Usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Usuarios", u"Data", None));
        ___qtablewidgetitem2 = self.Tab_Usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Usuarios", u"Nome", None));
        ___qtablewidgetitem3 = self.Tab_Usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Usuarios", u"Telefone", None));
        ___qtablewidgetitem4 = self.Tab_Usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Usuarios", u"Endere\u00e7o", None));
        ___qtablewidgetitem5 = self.Tab_Usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Usuarios", u"Usuario", None));
        ___qtablewidgetitem6 = self.Tab_Usuarios.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Usuarios", u"Senha", None));
        ___qtablewidgetitem7 = self.Tab_Usuarios.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Usuarios", u"Permi\u00e7\u00e3o", None));
    # retranslateUi

