# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vendas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Vendas(object):
    def setupUi(self, Vendas):
        if not Vendas.objectName():
            Vendas.setObjectName(u"Vendas")
        Vendas.resize(759, 412)
        Vendas.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.gridLayout_2 = QGridLayout(Vendas)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Vendas)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_CadCliente = QPushButton(Vendas)
        self.btn_CadCliente.setObjectName(u"btn_CadCliente")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_CadCliente.sizePolicy().hasHeightForWidth())
        self.btn_CadCliente.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_CadCliente.setFont(font1)
        self.btn_CadCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_CadCliente.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/image/imagens/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CadCliente.setIcon(icon)
        self.btn_CadCliente.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_CadCliente)

        self.btn_Estoque = QPushButton(Vendas)
        self.btn_Estoque.setObjectName(u"btn_Estoque")
        sizePolicy1.setHeightForWidth(self.btn_Estoque.sizePolicy().hasHeightForWidth())
        self.btn_Estoque.setSizePolicy(sizePolicy1)
        self.btn_Estoque.setFont(font1)
        self.btn_Estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Estoque.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/image/imagens/vendas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Estoque.setIcon(icon1)
        self.btn_Estoque.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Estoque)

        self.btn_Salvar = QPushButton(Vendas)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        sizePolicy1.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy1)
        self.btn_Salvar.setFont(font1)
        self.btn_Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet(u"QPushButton{;\n"
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
        icon2.addFile(u":/image/imagens/Save.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon2)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.btn_Salvar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.RegistrodeVendas = QFrame(Vendas)
        self.RegistrodeVendas.setObjectName(u"RegistrodeVendas")
        self.RegistrodeVendas.setFrameShape(QFrame.StyledPanel)
        self.RegistrodeVendas.setFrameShadow(QFrame.Sunken)
        self.gridLayout = QGridLayout(self.RegistrodeVendas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.RegistrodeVendas)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_3 = QLabel(self.RegistrodeVendas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.Cbb_nome = QComboBox(self.RegistrodeVendas)
        self.Cbb_nome.setObjectName(u"Cbb_nome")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Cbb_nome.sizePolicy().hasHeightForWidth())
        self.Cbb_nome.setSizePolicy(sizePolicy2)
        self.Cbb_nome.setFont(font2)

        self.gridLayout.addWidget(self.Cbb_nome, 1, 1, 1, 2)

        self.label_4 = QLabel(self.RegistrodeVendas)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 1, 6, 1, 2)

        self.Cbb_Pag = QComboBox(self.RegistrodeVendas)
        self.Cbb_Pag.setObjectName(u"Cbb_Pag")
        sizePolicy2.setHeightForWidth(self.Cbb_Pag.sizePolicy().hasHeightForWidth())
        self.Cbb_Pag.setSizePolicy(sizePolicy2)
        self.Cbb_Pag.setFont(font2)

        self.gridLayout.addWidget(self.Cbb_Pag, 1, 9, 1, 1)

        self.label_5 = QLabel(self.RegistrodeVendas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)

        self.Cbb_Produto = QComboBox(self.RegistrodeVendas)
        self.Cbb_Produto.setObjectName(u"Cbb_Produto")
        sizePolicy2.setHeightForWidth(self.Cbb_Produto.sizePolicy().hasHeightForWidth())
        self.Cbb_Produto.setSizePolicy(sizePolicy2)
        self.Cbb_Produto.setFont(font2)

        self.gridLayout.addWidget(self.Cbb_Produto, 2, 2, 1, 1)

        self.label_6 = QLabel(self.RegistrodeVendas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 3)

        self.L_Quat = QLineEdit(self.RegistrodeVendas)
        self.L_Quat.setObjectName(u"L_Quat")
        self.L_Quat.setFont(font2)
        self.L_Quat.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.L_Quat, 2, 6, 1, 3)

        self.label_7 = QLabel(self.RegistrodeVendas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.L_Valor = QLineEdit(self.RegistrodeVendas)
        self.L_Valor.setObjectName(u"L_Valor")
        self.L_Valor.setFont(font2)
        self.L_Valor.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.L_Valor, 3, 1, 1, 3)

        self.label_8 = QLabel(self.RegistrodeVendas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 3, 4, 1, 1)

        self.L_Id = QLineEdit(self.RegistrodeVendas)
        self.L_Id.setObjectName(u"L_Id")
        self.L_Id.setFont(font2)
        self.L_Id.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.L_Id, 3, 5, 1, 2)

        self.label_9 = QLabel(self.RegistrodeVendas)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout.addWidget(self.label_9, 3, 7, 1, 1)

        self.L_Data = QLineEdit(self.RegistrodeVendas)
        self.L_Data.setObjectName(u"L_Data")
        self.L_Data.setFont(font2)
        self.L_Data.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.L_Data, 3, 8, 1, 2)

        self.Tab_Caixa_Vendas = QTableWidget(self.RegistrodeVendas)
        if (self.Tab_Caixa_Vendas.columnCount() < 7):
            self.Tab_Caixa_Vendas.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.Tab_Caixa_Vendas.setObjectName(u"Tab_Caixa_Vendas")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Tab_Caixa_Vendas.sizePolicy().hasHeightForWidth())
        self.Tab_Caixa_Vendas.setSizePolicy(sizePolicy4)
        self.Tab_Caixa_Vendas.setFont(font2)

        self.gridLayout.addWidget(self.Tab_Caixa_Vendas, 4, 0, 1, 10)


        self.gridLayout_2.addWidget(self.RegistrodeVendas, 2, 0, 1, 1)


        self.retranslateUi(Vendas)

        QMetaObject.connectSlotsByName(Vendas)
    # setupUi

    def retranslateUi(self, Vendas):
        Vendas.setWindowTitle(QCoreApplication.translate("Vendas", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Vendas", u"Vendas", None))
        self.btn_CadCliente.setText(QCoreApplication.translate("Vendas", u"Clientes", None))
#if QT_CONFIG(tooltip)
        self.btn_Estoque.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Estoque.setText(QCoreApplication.translate("Vendas", u"Compras", None))
#if QT_CONFIG(tooltip)
        self.btn_Salvar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Salvar.setText(QCoreApplication.translate("Vendas", u"Salvar", None))
        self.label.setText(QCoreApplication.translate("Vendas", u"Registro de Vendas", None))
        self.label_3.setText(QCoreApplication.translate("Vendas", u"Nome:", None))
        self.Cbb_nome.setCurrentText("")
        self.Cbb_nome.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Vendas", u"Pagamento:", None))
        self.Cbb_Pag.setCurrentText("")
        self.Cbb_Pag.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Vendas", u"Produtos:", None))
        self.Cbb_Produto.setCurrentText("")
        self.Cbb_Produto.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("Vendas", u"Quantidades:", None))
        self.label_7.setText(QCoreApplication.translate("Vendas", u"Valor:", None))
        self.label_8.setText(QCoreApplication.translate("Vendas", u"ID:", None))
        self.label_9.setText(QCoreApplication.translate("Vendas", u"Data:", None))
        ___qtablewidgetitem = self.Tab_Caixa_Vendas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Vendas", u"Data", None));
        ___qtablewidgetitem1 = self.Tab_Caixa_Vendas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Vendas", u"Cliente", None));
        ___qtablewidgetitem2 = self.Tab_Caixa_Vendas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Vendas", u"Produtos", None));
        ___qtablewidgetitem3 = self.Tab_Caixa_Vendas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Vendas", u"Quantidades", None));
        ___qtablewidgetitem4 = self.Tab_Caixa_Vendas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Vendas", u"Valor", None));
        ___qtablewidgetitem5 = self.Tab_Caixa_Vendas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Vendas", u"SubTotal", None));
        ___qtablewidgetitem6 = self.Tab_Caixa_Vendas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Vendas", u"Pagamento", None));
    # retranslateUi

