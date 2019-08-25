import sqlite3  
import sys
from PyQt5 import QtWidgets,QtGui, QtCore,uic

form_class= uic.loadUiType("kita.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow,form_class):
    
    def __init__(self,parent= None):
        
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.btn_Guardar.clicked.connect(self.btn_Guardar_clicked)
        self.IniciarBase()
        self.lista.itemSelectionChanged.connect(self.itemChanged)
        self.btn_Nuevo.clicked.connect(self.btn_Nuevo_clicked)
        
    def IniciarBase(self):
        self.con = sqlite3.connect("prueba.bd")
        self.cursor = self.con.cursor()
        self.cursor.execute ("""CREATE TABLE IF NOT EXISTS campos(KITA TEXT NOT NULL, EMAIL TEXT NOT NULL, ADRESS TEXT NOT NULL,TELEPHON TEXT NOT NULL, ZEIT TEXT NOT NULL)""" )
        self.con.commit()
        self.btn_Cargar_clicked()   
        self.con.close()

    def btn_Cargar_clicked(self):
 
      self.con = sqlite3.connect("prueba.bd")
      self.cursor = self.con.cursor()
       
      # loading data from table
      self.cursor.execute("SELECT KITA, EMAIL, ADRESS,TELEPHON,ZEIT FROM campos")
     
      # clear form
      self.lista.clear()
      
      # table in the qlist
      self.con = sqlite3.connect("prueba.bd")
      self.cursor = self.con.cursor()
      self.cursor.execute("SELECT KITA, EMAIL, ADRESS,TELEPHON,ZEIT FROM campos")

      for i in self.cursor:
       
          
       self.kita = str(i[0])
       self.email = str(i[1])
       self.adress = str(i[2]) 
       self.telephon=str(i[3])
       self.zeit = str(i[4])
       self.lista.addItem(self.kita)
       
      self.con.commit()
      self.con.close()


    def btn_Guardar_clicked(self):

            self.con = sqlite3.connect("prueba.bd")
            self.cursor = self.con.cursor()
 
        # Datos
            
            self.kita = str(self.line_Kita.text())
            if self.kita != "":
                for i in str(self.lista == self.kita):
                    self.Modificar(self.kita)
                
                            
                self.email = str(self.line_Email.text())
                self.adress = str(self.line_Adress.text())
                self.telephon = str(self.line_Tel.text())
                self.zeit = str(self.line_Zeit.text())      
                self.datos = (self.kita, self.email, self.adress,self.telephon,self.zeit)
                
                 # Insert data in the fields
                self.cursor.execute("INSERT INTO campos (kita, email, adress,telephon,zeit) VALUES (?,?,?,?,?)", self.datos)
                self.con.commit()
                 
            # fields clear when i save
                       
            self.line_Kita.setText("")
            self.line_Email.setText("")
            self.line_Adress.setText("")
            self.line_Tel.setText("")
            self.line_Zeit.setText("")
            
            self.con.commit()
            self.con.close()
            self.btn_Cargar_clicked()   
    
    def itemChanged(self):
        
        item = QtWidgets.QListWidgetItem(self.lista.currentItem())
        self.con = sqlite3.connect("prueba.bd")
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT KITA, EMAIL, ADRESS,TELEPHON,ZEIT FROM campos")

        print("Sistema seleccionado: ", item.text())
        for i in self.cursor:
            self.kita = str(i[0])
            self.email = str(i[1])
            self.adress = str(i[2]) 
            self.telephon=str(i[3])
            self.zeit = str(i[4])


            if str(item.text()) == (self.kita):
                self.line_Kita.setText(self.kita)
                self.line_Email.setText(self.email)       
                self.line_Adress.setText(self.adress)
                self.line_Tel.setText(self.telephon)
                self.line_Zeit.setText(self.zeit)

        self.con.commit()
        self.con.close()

    def btn_Nuevo_clicked(self):

        self.line_Kita.setText("")
        self.line_Email.setText("")
        self.line_Adress.setText("")
        self.line_Tel.setText("")
        self.line_Zeit.setText("")

    def Modificar(self,kita):
        None
app = QtWidgets.QApplication(sys.argv)

MyWindow = MyWindowClass(None)

MyWindow.show()
app.exec_()
