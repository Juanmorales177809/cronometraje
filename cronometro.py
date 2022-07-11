# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cronometro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ast import Lambda
from datetime import datetime
from email.errors import MessageError
from xml.dom.pulldom import parseString
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import time
import pandas as pd
import numpy as np
import mysql.connector
import sys
from PyQt5.QtCore import *
from tkinter import messagebox
from datetime import datetime




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo_dis = QtWidgets.QComboBox(self.centralwidget)
        self.combo_dis.setGeometry(QtCore.QRect(120, 40, 141, 31))
        self.combo_dis.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.combo_dis.setObjectName("combo_dis")
        self.combo_dis.addItem("")
        self.combo_dis.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.button_correr = QtWidgets.QPushButton(self.centralwidget)
        self.button_correr.setGeometry(QtCore.QRect(980, 100, 121, 31))
        self.button_correr.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.button_correr.setObjectName("button_correr")
        self.button_parar = QtWidgets.QPushButton(self.centralwidget)
        self.button_parar.setGeometry(QtCore.QRect(980, 140, 121, 31))
        self.button_parar.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.button_parar.setObjectName("button_parar")
        self.button_carrera = QtWidgets.QPushButton(self.centralwidget)
        self.button_carrera.setGeometry(QtCore.QRect(20, 200, 131, 31))
        self.button_carrera.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);")
        self.button_carrera.setObjectName("button_carrera")
        self.button_meta = QtWidgets.QPushButton(self.centralwidget)
        self.button_meta.setGeometry(QtCore.QRect(180, 200, 131, 31))
        self.button_meta.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);")
        self.button_meta.setObjectName("button_meta")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 250, 1201, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1199, 239))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.table_corredores = QTableWidget(self.scrollAreaWidgetContents)
        # self.table_corredores = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.table_corredores.setGeometry(QtCore.QRect(0, 0, 1201, 241))
        self.table_corredores.setObjectName("table_corredores")
        self.table_corredores.setSelectionMode(QAbstractItemView.SingleSelection)
        
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 150, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 190, 61, 16))
        self.label_6.setObjectName("label_6")
        self.edit_corredor = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_corredor.setGeometry(QtCore.QRect(690, 180, 141, 31))
        self.edit_corredor.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.edit_corredor.setObjectName("edit_corredor")
        self.button_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar.setGeometry(QtCore.QRect(850, 170, 41, 41))
        self.button_buscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/buscar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_buscar.setIcon(icon)
        self.button_buscar.setIconSize(QtCore.QSize(38, 38))
        self.button_buscar.setObjectName("button_buscar")

        self.button_buscar1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar1.setGeometry(QtCore.QRect(330, 80, 41, 41))
        self.button_buscar1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Edit_icon_(the_Noun_Project_30184).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_buscar1.setIcon(icon1)
        self.button_buscar1.setIconSize(QtCore.QSize(38, 38))
        self.button_buscar1.setObjectName("button_buscar")

        self.button_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.button_guardar.setGeometry(QtCore.QRect(980, 180, 121, 31))
        self.button_guardar.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.button_guardar.setObjectName("button_guardar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(900, 190, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 121, 16))
        self.label_8.setObjectName("label_8")
        self.button_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.button_enviar.setGeometry(QtCore.QRect(1150, 200, 41, 41))
        self.button_enviar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/enviar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_enviar.setIcon(icon1)
        self.button_enviar.setIconSize(QtCore.QSize(38, 38))
        self.button_enviar.setObjectName("button_enviar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 10, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 90, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 121, 16))
        self.label_9.setObjectName("label_9")
        self.button_buscar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar_3.setGeometry(QtCore.QRect(280, 80, 41, 41))
        self.button_buscar_3.setText("")
        self.button_buscar_3.setIcon(icon)
        self.button_buscar_3.setIconSize(QtCore.QSize(38, 38))
        self.button_buscar_3.setObjectName("button_buscar_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 20, 81, 16))
        self.label_10.setObjectName("label_10")
        self.combo_dis_2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo_dis_2.setGeometry(QtCore.QRect(360, 40, 141, 31))
        self.combo_dis_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.combo_dis_2.setObjectName("combo_dis_2")
        self.combo_dis_2.addItem("")
        self.combo_dis_2.addItem("")
        self.combo_dis_2.addItem("")
        self.combo_dis_2.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(960, 500, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 510, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.button_buscar.clicked.connect(self.buscarCorredor)
        self.button_buscar_3.clicked.connect(self.buscar)
        self.button_buscar1.clicked.connect(self.listar)
        self.button_guardar.clicked.connect(self.asignarNumero)
        self.button_enviar.clicked.connect(self.enviar)
        self.button_parar.clicked.connect(self.parar)
        self.button_correr.clicked.connect(self.correr)
        self.button_carrera.clicked.connect(self.enCarrera)
        self.button_meta.clicked.connect(self.listarDistancia)
        
        #Tabla de datos
        #Ocultar encabezado vertical
        # self.table_corredores.verticalHeader().setVisible(False)
        self.table_corredores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_corredores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_corredores.setWordWrap(False)
        #Deshabilitar resaltado de en el texto al seleccionar una fila
        self.table_corredores.horizontalHeader().setHighlightSections(False)
        self.table_corredores.horizontalHeader().setStretchLastSection(True)
        #Establecer ancho de las columnas
        # self.table_corredores.horizontalHeader().setDefaultSectionSize(150)
        self.table_corredores.setAutoScrollMargin(10)
        #darle una funcion al combobox
        self.combo_dis.activated.connect(self.listarDistancia)
        self.combo_dis_2.activated.connect(self.listarCategoria)
                
        stylesheet = "::section{Background-color:rgb(255, 255, 0)}"
        self.table_corredores.horizontalHeader().setStyleSheet(stylesheet)
        self.table_corredores.verticalHeader().setStyleSheet(stylesheet)
        #Cronometro
        # reloj = Cronometro(self.label_3)
        self.hora_inicio = datetime.now()
        self.distancia = 'Todas'
        self.leerDatos()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_4.setText(self.obtenerTiempo())
        
        self.contadorEliteMasculino =1
        self.contadorEliteFemenino =1
        self.contadorMasterFemenino =1
        self.contadorMasterMasculino =1
        
    

    def obtenerTiempo(self):
        segundos_transcurridos = (datetime.now()-self.hora_inicio).total_seconds()
        
        return self.formatearTiempo(int(segundos_transcurridos))
    def formatearTiempo(self,segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas *60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    def refrescarTiempo(self):
        return "Refrescando"
    def start(self):
        pass

    
    def columns(self):
        self.keyss= list(self.data.keys())
        self.columnas = []
        for nombre in self.keyss:
            self.columnas.append(nombre)
        self.table_corredores.setColumnCount(len(self.columnas))
        self.table_corredores.setRowCount(len(self.data["Nombres"]))
        
        self.table_corredores.setHorizontalHeaderLabels(self.columnas)
        header_view = self.table_corredores.horizontalHeader()
        idx = header_view.count() - 1
        header_view.setSectionResizeMode(idx, QtWidgets.QHeaderView.ResizeToContents)
    
    
    def leerDatos(self):
        df = pd.read_csv("example1.csv", sep= ',')
        self.data = {"#": list(df["#"]), "Nombres": list(df["Nombres"]), "# Documento": df["# Documento"],
                "Distancia [Km]": df["Distancia [Km]"],"Puesto": df["Puesto"], "Categoria": df["Categoria"],
                "Hora Salida": df["Hora Salida"], "Hora Llegada": df["Hora Llegada"], "Tiempo de Carrera":df["Tiempo de Carrera"],
                "Estado": df["Estado"],"Telefono": df["Telefono"],
                }
        self.keyss= list(self.data.keys())

    # def leerDatos(self):
    #     df = pd.read_csv("MorronTrailRun2022_2.csv", sep= ',')
        
    #     nombres = df["Nombre"]
    #     apellidos = df["Apellidos"]
        
    #     nombre = []
    #     salida = []
    #     llegada = []
    #     tiempo = []
    #     numeroCorredor = []
    #     posicion= []
    #     estado= []
    #     categoria = []
    #     for indice in range(0, len(nombres)):
    #         nombre.append(nombres[indice].title()+" "+apellidos[indice].title())
    #         salida.append("Salida")
    #         llegada.append("Salida")
    #         tiempo.append("Salida")
    #         estado.append('Linea de Partida')
    #         numeroCorredor.append("No asignado")
    #         posicion.append(int(0))
    #         if df["Edad"][indice] < 40:
    #             if df["Soy"][indice] == "Mujer":
    #                 categoria.append("Elite femenino")
    #             else:
    #                 categoria.append("Elite masculino")
    #         else:
    #             if df["Soy"][indice] == "Mujer":
    #                 categoria.append("Master femenino")
    #             else:
    #                 categoria.append("Master maculino") 
    #     self.data = {"#": numeroCorredor, "Nombres": nombre, "# Documento": df["Numero de documento"],
    #             "Distancia [Km]": df["Distancia"],"Puesto": posicion, "Categoria": categoria,
    #             "Hora Salida": salida, "Hora Llegada": llegada, "Tiempo de Carrera":tiempo,
    #             "Estado": estado,"Telefono": df["Telefono de contacto"],
    #             }
    #     self.keyss= list(self.data.keys())
        
    #     self.df = pd.DataFrame(self.data)
    
    def guardarCsv(self):
        df = pd.DataFrame(self.data)
        df.to_csv('example1.csv',index=False)    
        
   
    def listar(self):
        # self.leerDatos()
        self.columns()
        
        for fila in range(0,len(self.data["Nombres"])):
            for columna in range(0, len(self.keyss)):
                colu= self.keyss[columna]
                self.table_corredores.setItem(fila,columna,QTableWidgetItem(str(self.data[colu][fila])))
        self.guardarCsv()
    def listarDistancia(self):
        self.deleteAllRows(self.table_corredores)
        self.leerDatos()
        self.columns()
        distancia = self.combo_dis.currentText()
        print(distancia)
        print(type(self.data["Distancia [Km]"]))
        if distancia == "12k":
            dist= 12
            freq = list(self.data["Distancia [Km]"]).count(12)
        else:
            freq = list(self.data["Distancia [Km]"]).count(27)
            dist=27
        
        self.table_corredores.setColumnCount(len(self.columnas))
        self.table_corredores.setRowCount(freq)
        contador=0
        for fila in range(0,len(self.data["#"])):
            if dist == self.data["Distancia [Km]"][fila]:
                contador+=1
                for columna in range(0, len(self.keyss)):
                    colu= self.keyss[columna]
                    self.table_corredores.setItem(contador-1,columna,QTableWidgetItem(str(self.data[colu][fila])))

    def listarCategoria(self):
        self.deleteAllRows(self.table_corredores)
        self.leerDatos()
        self.columns()
        categoria = self.combo_dis_2.currentText()
        if categoria == "Elite masculino":
            freq = list(self.data["Categoria"]).count("Elite masculino")
        elif categoria == "Elite femenino":
            freq = list(self.data["Categoria"]).count("Elite femenino")
        elif categoria == "Master femenino":
            freq = list(self.data["Categoria"]).count("Master femenino")
        elif categoria == "Master maculino":
            freq = list(self.data["Categoria"]).count("Master maculino")
        self.table_corredores.setColumnCount(len(self.columnas))
        self.table_corredores.setRowCount(freq)
        contador =0
        for fila in range(0,len(self.data["#"])):
           if categoria == self.data["Categoria"][fila]:
                contador+=1
                for columna in range(0, len(self.keyss)):
                    colu= self.keyss[columna]
                    self.table_corredores.setItem(contador-1,columna,QTableWidgetItem(str(self.data[colu][fila])))
                    
        #self.button_buscar.hide()
    
    


    def mostrarHora(self):
            self.label_11.setText(time.strftime("%H:%M:%S"))
            QtCore.QTimer.singleShot(1000, self.mostrarHora)
    def enviar(self):
        print('Enviar')
    def asignarNumero(self):
        corredor = int(self.lineEdit.text())
        numero = self.edit_corredor.text()
        for fila in range(0, len(self.data["# Documento"])):
            if corredor == self.data["# Documento"][fila]:
                self.data["#"][fila]= int(numero)
                
        self.listar()
    def buscarCorredor(self):
        self.corredor = self.edit_corredor.text()
        print(self.corredor)
    def guardar(self):
        self.tiempoCorredor = time.strftime("%H:%M:%S")
        print(self.tiempoCorredor)
    def deleteAllRows(self, table:QTableWidget) -> None:
        #Obtener el modelo de la tabla
        model:QAbstractTableModel = table.model()
        #Remover todos las filas
        model.removeRows(0, model.rowCount())   
    def buscar(self):
        self.corredor = int(self.lineEdit.text())
        if self.corredor != "":
            self.deleteAllRows(self.table_corredores)
            for fila in range(0, len(self.data["# Documento"])):
                if self.corredor == self.data["# Documento"][fila]:
                    for columna in range(0, len(self.keyss)):
                        colu= self.keyss[columna]
                        self.table_corredores.setColumnCount(len(self.columnas))
                        self.table_corredores.setRowCount(1)
                        self.table_corredores.setItem(0,columna,QTableWidgetItem(str(self.data[colu][fila])))
                        

        else:
            self.listar()
    def correr(self):
        inicio = time.strftime("%H:%M:%S")
        for fila in range(0, len(self.data["# Documento"])):
            if self.data["#"][fila] != 'Null':
                self.data["Hora Salida"][fila]= inicio
                self.data["Hora Llegada"][fila]= "..."
                self.data["Tiempo de Carrera"][fila]= "esperando..."
                self.data["Estado"][fila]= "En ruta ...\U0001F3C3 \U0001F5FB "
                self.listar()
                self.button_correr.setEnabled(False)
    def calcularTiempo(self,salida, llegada):
        print(salida)
        print(llegada)
        time_1=datetime.strftime(salida,"%H:%M:%S")
        time_2=datetime.strftime(llegada,"%H:%M:%S")

        time_interval = time_2 - time_1
        return time_interval
        



    def parar(self):

            final = time.strftime("%H:%M:%S")
            corredor = int(self.edit_corredor.text())
            
            for fila in range(0, len(self.data["# Documento"])):
                if self.data["Hora Llegada"][fila] == "...":
                    if self.data["#"][fila]==corredor:
                        self.data["Hora Llegada"][fila]= final
                        self.data["Estado"][fila]= "En Meta \U0001F973 \U0001F5FB "
                        tiempo1=self.data["Hora Salida"][fila]
                        tiempo2= self.data["Hora Llegada"][fila]
                        time_1=datetime.strptime(tiempo1,"%H:%M:%S")
                        time_2=datetime.strptime(tiempo2,"%H:%M:%S")
                        time_interval = time_2 - time_1
                        print(time_interval)
                        self.data["Tiempo de Carrera"][fila]= time_interval
                        if self.data["Categoria"][fila] == "Elite masculino":
                            self.data["Puesto"][fila]=self.contadorEliteMasculino
                            self.contadorEliteMasculino += 1
                        elif self.data["Categoria"][fila] == "Elite femenino":
                            self.data["Puesto"][fila] = self.contadorEliteFemenino
                            self.contadorEliteFemenino +=1
                        elif self.data["Categoria"][fila] == "Master femenino":
                            self.data["Puesto"][fila] = self.contadorMasterFemenino
                            self.contadorMasterFemenino +=1
                        elif self.data["Categoria"][fila] == "Master maculino":
                            self.data["Puesto"][fila] = self.contadorMasterMasculino
                            self.contadorMasterMasculino +=1
                        self.listar()
                else:
                    print("Corredor en meta")
    
    def enCarrera(self):
        self.estado = True
        print(self.estado)
    def enMeta(self):
        self.estado = False
        print(self.estado)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_dis.setItemText(0, _translate("MainWindow", "12k"))
        self.combo_dis.setItemText(1, _translate("MainWindow", "27k"))
        self.label.setText(_translate("MainWindow", "Distancia"))
        self.label_2.setText(_translate("MainWindow", "Elegir distancia"))
        self.label_3.setText(_translate("MainWindow", "Control Cronometro"))
        self.button_correr.setText(_translate("MainWindow", "CORRER"))
        self.button_parar.setText(_translate("MainWindow", "PARAR"))
        self.button_carrera.setToolTip(_translate("MainWindow", "<html><head/><body><p>Carrera</p></body></html>"))
        self.button_carrera.setText(_translate("MainWindow", "EN CARRERA"))
        self.button_meta.setToolTip(_translate("MainWindow", "<html><head/><body><p>Meta</p></body></html>"))
        self.button_meta.setText(_translate("MainWindow", "EN META"))
        self.label_5.setText(_translate("MainWindow", "Ingrese el numero del corredor"))
        self.label_6.setText(_translate("MainWindow", "# Corredor"))
        self.button_guardar.setText(_translate("MainWindow", "GUARDAR"))
        self.label_7.setText(_translate("MainWindow", "Marcar tiempo"))
        self.label_8.setText(_translate("MainWindow", "Estado del corredor"))
        self.button_enviar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enviar Tiempos</p></body></html>"))
        self.mostrarHora()
        
        self.label_9.setText(_translate("MainWindow", "# Documento"))
        self.label_10.setText(_translate("MainWindow", "Elegir categoria"))
        self.combo_dis_2.setItemText(0, _translate("MainWindow", "Elite masculino"))
        self.combo_dis_2.setItemText(1, _translate("MainWindow", "Elite femenino"))
        self.combo_dis_2.setItemText(2, _translate("MainWindow", "Master maculino"))
        self.combo_dis_2.setItemText(3, _translate("MainWindow", "Master femenino"))
        
        #self.label_11.setText(time.strftime("%H:%M:%S"))
        self.label_12.setText(time.strftime("%d/%m/%y"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    
    MainWindow.show()
    sys.exit(app.exec_())
    
