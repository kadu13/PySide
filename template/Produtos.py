# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Produtos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Produtos(object):
    def setupUi(self, Produtos):
        if not Produtos.objectName():
            Produtos.setObjectName(u"Produtos")
        Produtos.resize(754, 548)
        Produtos.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.gridLayout_4 = QGridLayout(Produtos)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Produtos)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.L_Produto = QLineEdit(Produtos)
        self.L_Produto.setObjectName(u"L_Produto")
        self.L_Produto.setFont(font)

        self.gridLayout.addWidget(self.L_Produto, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(Produtos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.L_Custo = QLineEdit(Produtos)
        self.L_Custo.setObjectName(u"L_Custo")
        self.L_Custo.setFont(font)

        self.gridLayout_2.addWidget(self.L_Custo, 0, 1, 1, 1)

        self.label_4 = QLabel(Produtos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.L_Preco = QLineEdit(Produtos)
        self.L_Preco.setObjectName(u"L_Preco")
        self.L_Preco.setFont(font)

        self.gridLayout_2.addWidget(self.L_Preco, 0, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.Tab_Produto = QTableWidget(Produtos)
        if (self.Tab_Produto.columnCount() < 4):
            self.Tab_Produto.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.Tab_Produto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.Tab_Produto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.Tab_Produto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.Tab_Produto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Tab_Produto.setObjectName(u"Tab_Produto")
        self.Tab_Produto.setFont(font)

        self.gridLayout_4.addWidget(self.Tab_Produto, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_Voltar = QPushButton(Produtos)
        self.btn_Voltar.setObjectName(u"btn_Voltar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Voltar.sizePolicy().hasHeightForWidth())
        self.btn_Voltar.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_Voltar.setFont(font1)
        self.btn_Voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Voltar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 127);\n"
"	color: rgb(255, 255, 255);\n"
"   border-radius: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(206, 206, 206);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/image/imagens/voltar1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Voltar.setIcon(icon)
        self.btn_Voltar.setIconSize(QSize(80, 40))

        self.horizontalLayout.addWidget(self.btn_Voltar)

        self.label = QLabel(Produtos)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(30)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_Editar = QPushButton(Produtos)
        self.btn_Editar.setObjectName(u"btn_Editar")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_Editar.setFont(font3)
        self.btn_Editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Editar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
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
        icon1.addFile(u":/image/imagens/editar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Editar.setIcon(icon1)
        self.btn_Editar.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_Editar, 0, 3, 1, 1)

        self.btn_Excluir = QPushButton(Produtos)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        self.btn_Excluir.setFont(font3)
        self.btn_Excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Excluir.setStyleSheet(u"QPushButton{  \n"
"   background-color: rgb(255, 0, 0);\n"
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
        icon2.addFile(u":/image/imagens/excluir-arquivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon2)
        self.btn_Excluir.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_Excluir, 0, 5, 1, 1)

        self.L_Id = QLineEdit(Produtos)
        self.L_Id.setObjectName(u"L_Id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L_Id.sizePolicy().hasHeightForWidth())
        self.L_Id.setSizePolicy(sizePolicy1)
        self.L_Id.setFont(font)

        self.gridLayout_3.addWidget(self.L_Id, 0, 1, 1, 1)

        self.label_5 = QLabel(Produtos)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.btn_Adicionar = QPushButton(Produtos)
        self.btn_Adicionar.setObjectName(u"btn_Adicionar")
        self.btn_Adicionar.setFont(font3)
        self.btn_Adicionar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Adicionar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 255, 0);\n"
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
        icon3.addFile(u":/image/imagens/mais (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Adicionar.setIcon(icon3)
        self.btn_Adicionar.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_Adicionar, 0, 2, 1, 1)

        self.btn_Limpar = QPushButton(Produtos)
        self.btn_Limpar.setObjectName(u"btn_Limpar")
        self.btn_Limpar.setFont(font3)
        self.btn_Limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Limpar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 0);\n"
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
        icon4.addFile(u":/image/imagens/limpar-limpo (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Limpar.setIcon(icon4)
        self.btn_Limpar.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_Limpar, 0, 4, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.retranslateUi(Produtos)

        QMetaObject.connectSlotsByName(Produtos)
    # setupUi

    def retranslateUi(self, Produtos):
        Produtos.setWindowTitle(QCoreApplication.translate("Produtos", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Produtos", u"Produtos:", None))
        self.label_3.setText(QCoreApplication.translate("Produtos", u"Custo:", None))
        self.label_4.setText(QCoreApplication.translate("Produtos", u"Pre\u00e7o de Venda:", None))
        ___qtablewidgetitem = self.Tab_Produto.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Produtos", u"ID", None));
        ___qtablewidgetitem1 = self.Tab_Produto.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Produtos", u"Produtos", None));
        ___qtablewidgetitem2 = self.Tab_Produto.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Produtos", u"Custo", None));
        ___qtablewidgetitem3 = self.Tab_Produto.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Produtos", u"Pre\u00e7o", None));
        self.btn_Voltar.setText("")
        self.label.setText(QCoreApplication.translate("Produtos", u"Cadastro de Produtos", None))
        self.btn_Editar.setText(QCoreApplication.translate("Produtos", u"Editar", None))
        self.btn_Excluir.setText(QCoreApplication.translate("Produtos", u"Excluir", None))
        self.label_5.setText(QCoreApplication.translate("Produtos", u"ID:", None))
        self.btn_Adicionar.setText(QCoreApplication.translate("Produtos", u"Adicionar", None))
        self.btn_Limpar.setText(QCoreApplication.translate("Produtos", u"Limpar", None))
    # retranslateUi

