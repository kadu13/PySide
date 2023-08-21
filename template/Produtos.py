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


class Ui_Produtos(object):
    def setupUi(self, Produtos):
        if not Produtos.objectName():
            Produtos.setObjectName(u"Produtos")
        Produtos.resize(782, 410)
        Produtos.setStyleSheet(u"background-color: rgb(255, 0, 255);")
        self.gridLayout_2 = QGridLayout(Produtos)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Produtos)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 8)

        self.label_2 = QLabel(Produtos)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.L_Produto = QLineEdit(Produtos)
        self.L_Produto.setObjectName(u"L_Produto")
        self.L_Produto.setFont(font1)

        self.gridLayout.addWidget(self.L_Produto, 1, 3, 1, 5)

        self.label_3 = QLabel(Produtos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.L_Custo = QLineEdit(Produtos)
        self.L_Custo.setObjectName(u"L_Custo")
        self.L_Custo.setFont(font1)

        self.gridLayout.addWidget(self.L_Custo, 2, 2, 1, 3)

        self.label_4 = QLabel(Produtos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 5, 1, 2)

        self.L_Preco = QLineEdit(Produtos)
        self.L_Preco.setObjectName(u"L_Preco")
        self.L_Preco.setFont(font1)

        self.gridLayout.addWidget(self.L_Preco, 2, 7, 1, 1)

        self.label_5 = QLabel(Produtos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.L_Id = QLineEdit(Produtos)
        self.L_Id.setObjectName(u"L_Id")
        self.L_Id.setFont(font1)

        self.gridLayout.addWidget(self.L_Id, 3, 1, 1, 3)

        self.btn_Adicionar = QPushButton(Produtos)
        self.btn_Adicionar.setObjectName(u"btn_Adicionar")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_Adicionar.setFont(font2)
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

        self.gridLayout.addWidget(self.btn_Adicionar, 3, 4, 1, 2)

        self.Tab_Produto = QTableWidget(Produtos)
        if (self.Tab_Produto.columnCount() < 4):
            self.Tab_Produto.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.Tab_Produto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.Tab_Produto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.Tab_Produto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.Tab_Produto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Tab_Produto.setObjectName(u"Tab_Produto")
        self.Tab_Produto.setFont(font1)

        self.gridLayout.addWidget(self.Tab_Produto, 4, 0, 1, 8)

        self.btn_Excluir = QPushButton(Produtos)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        self.btn_Excluir.setFont(font2)
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

        self.gridLayout.addWidget(self.btn_Excluir, 3, 6, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Produtos)

        QMetaObject.connectSlotsByName(Produtos)
    # setupUi

    def retranslateUi(self, Produtos):
        Produtos.setWindowTitle(QCoreApplication.translate("Produtos", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Produtos", u"Cadastro de Produtos", None))
        self.label_2.setText(QCoreApplication.translate("Produtos", u"Produtos:", None))
        self.label_3.setText(QCoreApplication.translate("Produtos", u"Custo:", None))
        self.label_4.setText(QCoreApplication.translate("Produtos", u"Pre\u00e7o de Venda:", None))
        self.label_5.setText(QCoreApplication.translate("Produtos", u"ID:", None))
        self.btn_Adicionar.setText(QCoreApplication.translate("Produtos", u"Adicionar", None))
        ___qtablewidgetitem = self.Tab_Produto.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Produtos", u"ID", None));
        ___qtablewidgetitem1 = self.Tab_Produto.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Produtos", u"Produtos", None));
        ___qtablewidgetitem2 = self.Tab_Produto.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Produtos", u"Custo", None));
        ___qtablewidgetitem3 = self.Tab_Produto.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Produtos", u"Pre\u00e7o", None));
        self.btn_Excluir.setText(QCoreApplication.translate("Produtos", u"Excluir", None))
    # retranslateUi

