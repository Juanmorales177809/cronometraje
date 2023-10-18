#diseñar interfaz grafica en tkinter que llame el modulo enviar_mensajes.py y que permita escribir el mensaje que se quiere enviar

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np
from enviar_mensaje import *
import enviar_mensaje as em


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Envio de mensajes")
        self.ventana1.geometry("500x500")
        self.ventana1.resizable(0,0)
        self.ventana1.configure(background="#2E4053")
        self.label1=tk.Label(self.ventana1, text="Envio de mensajes", bg="#2E4053", fg="white")
        self.label1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        self.label2=tk.Label(self.ventana1, text="Mensaje", bg="#2E4053", fg="white")
        self.label2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        self.texto1=tk.Text(self.ventana1, width=30, height=10)
        self.texto1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        self.boton1=tk.Button(self.ventana1, text="Enviar", command=self.enviar)
        self.boton1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        self.ventana1.mainloop()
    
    def enviar(self):
        mensaje = self.texto1.get("1.0", tk.END)
        archivo = "docs/Formulario cross country.xlsx"
        imagen = "./img/INFOCROSSCOUNTRY.png"
        df = leer_datos(archivo)
        telefonos = vec_telefonos(df)
        nombres = vec_nombres(df)
        for telefono in telefonos:
            enviar_whatsapp(telefono, mensaje)
            enviar_imagen(telefono, imagen)
        mb.showinfo("Información", "Mensajes enviados")
        self.texto1.delete("1.0", tk.END)
        self.texto1.focus_set()

aplicacion1=Aplicacion()

