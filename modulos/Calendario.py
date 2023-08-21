#from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtPrintSupport import *
import os,sys
from template.Calendario import Calendario

class Data(QDialog):
    def __init__(self,*args,**argvs):
        super(Data, self).__init__(*args,**argvs)
        self.ui = Calendario()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)
        
        self.ui.Calendario.selectionChanged.connect(self.Funcao)
        
        
    def Funcao(self):

        self.dia = str(self.ui.Calendario.selectedDate())
        self.diaFormat = self.dia[21:32]
        #self.ui.Calendario.selectionChanged.connect(self.diaFormat)
        self.ui.data.setText(self.diaFormat) 
