# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compras.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Compras(object):
    def setupUi(self, Compras):
        if not Compras.objectName():
            Compras.setObjectName(u"Compras")
        Compras.resize(839, 587)
        Compras.setStyleSheet(u"background-color: rgb(255, 0, 255);")
        self.gridLayout = QGridLayout(Compras)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Compras)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Btn_Clientes = QPushButton(Compras)
        self.Btn_Clientes.setObjectName(u"Btn_Clientes")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Clientes.sizePolicy().hasHeightForWidth())
        self.Btn_Clientes.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.Btn_Clientes.setFont(font1)
        self.Btn_Clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Clientes.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/img/imagens/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Clientes.setIcon(icon)
        self.Btn_Clientes.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.Btn_Clientes)

        self.Btn_Produtos = QPushButton(Compras)
        self.Btn_Produtos.setObjectName(u"Btn_Produtos")
        sizePolicy.setHeightForWidth(self.Btn_Produtos.sizePolicy().hasHeightForWidth())
        self.Btn_Produtos.setSizePolicy(sizePolicy)
        self.Btn_Produtos.setFont(font1)
        self.Btn_Produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Produtos.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/img/imagens/Produtos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Produtos.setIcon(icon1)
        self.Btn_Produtos.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.Btn_Produtos)

        self.Btn_Vendas = QPushButton(Compras)
        self.Btn_Vendas.setObjectName(u"Btn_Vendas")
        sizePolicy.setHeightForWidth(self.Btn_Vendas.sizePolicy().hasHeightForWidth())
        self.Btn_Vendas.setSizePolicy(sizePolicy)
        self.Btn_Vendas.setFont(font1)
        self.Btn_Vendas.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Vendas.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/img/imagens/Cash-register.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Vendas.setIcon(icon2)
        self.Btn_Vendas.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.Btn_Vendas)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.frame_2 = QFrame(Compras)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 3)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)

        self.L_Id = QLineEdit(self.frame_2)
        self.L_Id.setObjectName(u"L_Id")
        font3 = QFont()
        font3.setPointSize(14)
        self.L_Id.setFont(font3)

        self.gridLayout_2.addWidget(self.L_Id, 0, 5, 1, 2)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_2.addWidget(self.label_9, 0, 7, 1, 2)

        self.L_Data = QLineEdit(self.frame_2)
        self.L_Data.setObjectName(u"L_Data")
        self.L_Data.setFont(font3)

        self.gridLayout_2.addWidget(self.L_Data, 0, 9, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.Cbb_Produto = QComboBox(self.frame_2)
        self.Cbb_Produto.setObjectName(u"Cbb_Produto")
        self.Cbb_Produto.setFont(font3)

        self.gridLayout_2.addWidget(self.Cbb_Produto, 1, 1, 1, 2)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 1, 7, 1, 1)

        self.Cbb_Tipo = QComboBox(self.frame_2)
        self.Cbb_Tipo.setObjectName(u"Cbb_Tipo")
        self.Cbb_Tipo.setFont(font3)

        self.gridLayout_2.addWidget(self.Cbb_Tipo, 1, 8, 1, 2)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 2)

        self.L_Quantidade = QLineEdit(self.frame_2)
        self.L_Quantidade.setObjectName(u"L_Quantidade")
        self.L_Quantidade.setFont(font3)

        self.gridLayout_2.addWidget(self.L_Quantidade, 2, 2, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 2, 3, 1, 1)

        self.L_Valor = QLineEdit(self.frame_2)
        self.L_Valor.setObjectName(u"L_Valor")
        self.L_Valor.setFont(font3)

        self.gridLayout_2.addWidget(self.L_Valor, 2, 4, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_Salvar = QPushButton(self.frame_2)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        sizePolicy.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Segoe UI Black")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_Salvar.setFont(font4)
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
"}")
        icon3 = QIcon()
        icon3.addFile(u":/image/imagens/Save.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon3)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Salvar)

        self.btn_Excluir = QPushButton(self.frame_2)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        sizePolicy.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy)
        self.btn_Excluir.setFont(font4)
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
"}")
        icon4 = QIcon()
        icon4.addFile(u":/image/imagens/Delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon4)
        self.btn_Excluir.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Excluir)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 6, 1, 3)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.Tab_Transacoes = QTableWidget(self.frame_2)
        if (self.Tab_Transacoes.columnCount() < 4):
            self.Tab_Transacoes.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.Tab_Transacoes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.Tab_Transacoes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.Tab_Transacoes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.Tab_Transacoes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Tab_Transacoes.setObjectName(u"Tab_Transacoes")
        self.Tab_Transacoes.setFont(font3)

        self.gridLayout_3.addWidget(self.Tab_Transacoes, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)


        self.retranslateUi(Compras)

        QMetaObject.connectSlotsByName(Compras)
    # setupUi

    def retranslateUi(self, Compras):
        Compras.setWindowTitle(QCoreApplication.translate("Compras", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Compras", u"Compras", None))
        self.Btn_Clientes.setText(QCoreApplication.translate("Compras", u"Clientes", None))
        self.Btn_Produtos.setText(QCoreApplication.translate("Compras", u"Produtos", None))
        self.Btn_Vendas.setText(QCoreApplication.translate("Compras", u"Vendas", None))
        self.label_3.setText(QCoreApplication.translate("Compras", u"Registro de Transa\u00e7\u00f5es", None))
        self.label_8.setText(QCoreApplication.translate("Compras", u"ID:", None))
        self.label_9.setText(QCoreApplication.translate("Compras", u"Data:", None))
        self.label_4.setText(QCoreApplication.translate("Compras", u"Produto:", None))
        self.label_6.setText(QCoreApplication.translate("Compras", u"Tipo:", None))
        self.label_5.setText(QCoreApplication.translate("Compras", u"Quantidades:", None))
        self.label_7.setText(QCoreApplication.translate("Compras", u"Valor:", None))
        self.btn_Salvar.setText(QCoreApplication.translate("Compras", u"Salvar", None))
        self.btn_Excluir.setText(QCoreApplication.translate("Compras", u"Excluir", None))
        ___qtablewidgetitem = self.Tab_Transacoes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Compras", u"Produtos", None));
        ___qtablewidgetitem1 = self.Tab_Transacoes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Compras", u"Tipo", None));
        ___qtablewidgetitem2 = self.Tab_Transacoes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Compras", u"Quantidade", None));
        ___qtablewidgetitem3 = self.Tab_Transacoes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Compras", u"Valor", None));
    # retranslateUi

