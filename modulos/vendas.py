from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Vendas import Ui_Vendas
import sqlite3
from DataBase.DbUsers import Data_Base

class Vendas(QDialog):
    def __init__(self,*args,**argvs):
        super(Vendas, self).__init__(*args,**argvs)
        self.ui = Ui_Vendas()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/MLogo.png")
        self.setWindowIcon(appIcon)