from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow, QDateEdit
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Usuarios import Ui_Usuarios
#from modulos.Calendario import Data
from DataBase.DbUsers import Data_Base


class Users(QDialog):
    def __init__(self,*args,**argvs):
        super(Users, self).__init__(*args,**argvs)
        self.ui = Ui_Usuarios()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)

        # self.ui.Tab_Usuarios.setColumnWidth(1, 218)
        self.Table_users()
       
        #Data.selectionChanged.connect(self.Datas)
       
        self.ui.btn_Salvar.clicked.connect(self.cad_Users)
        self.ui.btn_Excluir.clicked.connect(self.Deletar_Users)
        self.ui.btn_Limpar.clicked.connect(self.limpar)


    """ def AbrirData(self):
        self.Da = Data()
        self.Da.show() """
        
    def limpar(self):

        self.ui.L_Id.setText("")
        self.ui.L_Data.setText("")
        self.ui.L_Nome.setText("")
        self.ui.L_Telefone.setText("") 
        self.ui.L_Endereco.setText("")
        self.ui.L_Usuario.setText("")
        self.ui.L_Senha.setText("") 
        self.ui.Cbb_Permicao.setCurrentText("") 

    def cad_Users(self):
    
        data = self.ui.L_Data.text()
        nome = self.ui.L_Nome.text()
        fone = self.ui.L_Telefone.text()
        endereco = self.ui.L_Endereco.text()       
        user = self.ui.L_Usuario.text()
        password = self.ui.L_Senha.text()
        access = self.ui.Cbb_Permicao.currentText() 

        if data == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif nome == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif fone == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif endereco == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif user == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif password == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif access == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        else:

            db = Data_Base()
            db.connect()
            db.insert_user(data, nome, fone, endereco, user, password, access)                        
            self.Table_users()
            self.limpar()
            QMessageBox.information(QMessageBox(),"Cadastro Realizado", "Cadastro Realizado com Sucesso!")
            db.close_connect()



    def Deletar_Users(self):
        db = Data_Base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setText("Este registro sera Excluído.")
        msg.setInformativeText(f"Você tem certeza que deseja excluir? \n \n {self.ui.L_Nome}")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.Tab_Usuarios.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_users(id)           

            self.Table_users()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUIR")
            msg.setText(result)
            msg.exec()

            db.close_connect()
       
        
    def Table_users(self):
        self.ui.Tab_Usuarios.setColumnWidth(0, 70)
        self.ui.Tab_Usuarios.setColumnWidth(1, 70)
        self.ui.Tab_Usuarios.setColumnWidth(2, 170)
        self.ui.Tab_Usuarios.setColumnWidth(3, 100)
        self.ui.Tab_Usuarios.setColumnWidth(4, 100)
        self.ui.Tab_Usuarios.setColumnWidth(5, 100)
        self.ui.Tab_Usuarios.setColumnWidth(6, 100)
        self.ui.Tab_Usuarios.setColumnWidth(7, 100)

        db = Data_Base()
        db.connect()
        coletar = db.select_all_users()
        
        self.ui.Tab_Usuarios.contextMenuPolicy()
        self.ui.Tab_Usuarios.clearContents()
        self.ui.Tab_Usuarios.setRowCount(len(coletar))

        if coletar == "":
            pass
        else:
            for row, text in enumerate(coletar):

                for column, data in enumerate(text):
                    self.ui.Tab_Usuarios.setItem(row, column, QTableWidgetItem(str(data)))
        db.close_connect()



