from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Compras import Ui_Compras
import sqlite3
from DataBase.DbUsers import Data_Base

class Comp(QDialog):
    def __init__(self,*args,**argvs):
        super(Comp, self).__init__(*args,**argvs)
        self.ui = Ui_Compras()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)