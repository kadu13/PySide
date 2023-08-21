import os,sys
from PySide2 import QtCore
from PySide2.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QPushButton, QWidget,QMainWindow
from modulos.clientes import Clients
from modulos.compras import Comp
from modulos.estoque import Estoq
from modulos.produtos import Prod
from modulos.usuarios import Users
from modulos.vendas import Vendas
#from modulos.Calendario import Data
from template.Menu import Ui_Menu

class Start(QMainWindow):
    def __init__(self,user,autenticado,*args,**argvs):
        super(Start, self).__init__(*args,**argvs)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/MLogo.png")
        self.setWindowIcon(appIcon)
        
#----------------------   NOME DE USUÁRIO  ----------------------------------------------

        usuario = user
        self.ui.L_Logado.setEnabled(False)
        self.ui.L_Logado.setText(usuario)

#--------------------   PERMISSAO DE ACESSO AO FORMULARIO DE USUARIOS   ------------------

        permissao = autenticado
        if permissao == "user":
            self.ui.Btn_Usuarios.setVisible(False)
            self.ui.actionUsuarios.setVisible(False)

        elif permissao == "administrador":
            self.ui.Btn_Usuarios.setVisible(True)
            self.ui.actionUsuarios.setVisible(True)

#---------------------------  TOGGLE BUTTON  ------------------------------
        self.ui.BtnToggle.clicked.connect(self.Left_Menu)
        
# ----------------------------   MENU   -----------------------------------
        self.ui.actionFechar.triggered.connect(quit)
        self.ui.actionClientes.triggered.connect(self.AbrirCad)
        self.ui.actionCompras.triggered.connect(self.AbrirComp)
        #self.ui.actionContatos.triggered.connect()
        self.ui.actionEstoque.triggered.connect(self.AbrirEstoque)
        self.ui.actionProdutos.triggered.connect(self.AbrirProdutos)
        #self.ui.actionSobre.triggered.connect()
        self.ui.actionUsuarios.triggered.connect(self.AbrirUsuarios)
        self.ui.actionVendas.triggered.connect(self.AbrirVendas)
        
# -----------------------------  BUTTONS   --------------------------------

        self.ui.Btn_Clientes.clicked.connect(self.AbrirCad)
        self.ui.Btn_Compras.clicked.connect(self.AbrirComp)
        self.ui.Btn_Estoque.clicked.connect(self.AbrirEstoque)
        self.ui.Btn_Produtos.clicked.connect(self.AbrirProdutos)
        self.ui.Btn_Usuarios.clicked.connect(self.AbrirUsuarios)
        self.ui.Btn_Vendas.clicked.connect(self.AbrirVendas)

#---------------------------   ABRI O PAINEL COM BOTOES    ----------------

    def Left_Menu(self):

        width = self.ui.LeftMenu.width()

        if width == 0:
            newWidth = 201
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.ui.LeftMenu, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

# ------------------------- METHOR ABRIR FORMULARIOS -------------------

    def AbrirCad(self):
        self.Tela = Clients()
        self.Tela.show()
        

    def AbrirComp(self):
        self.Tela = Comp()
        self.Tela.show()

    def AbrirEstoque(self):
        self.Tela = Estoq()
        self.Tela.show()

    def AbrirProdutos(self):
        self.Tela = Prod()
        self.Tela.show()

    def AbrirUsuarios(self):
        self.Tela = Users()
        self.Tela.show()    

    def AbrirVendas(self):
        self.Tela = Vendas()
        self.Tela.show()
