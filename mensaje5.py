import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np


df = pd.read_csv("MorronTrailRun2022.csv")
telefonos = df['Telefono de contacto']
indice= 0
contador = 0
for i in telefonos:
    nombre = df["Nombre"][indice].title()
    text = f"{nombre} mañana es el gran día, te esperamos desde las 6:00am para el calentamiento y para que escuches a nuestro director de carrera contarte todos los por menores de la ruta. A las 7:00 am estaremos dando la partida. Adicional te compartimos la ubicación de la unidad deportiva cristo rey. *Nos vemos en la montaña*. https://maps.app.goo.gl/hup2bc1wpUnbrjqJ8"
    text1 = "https://maps.app.goo.gl/hup2bc1wpUnbrjqJ8" 
    pywhatkit.sendwhatmsg_instantly(f'+57{i}',text)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    # pywhatkit.sendwhatmsg_instantly(f'+57{i}',text1)
    # time.sleep(1)
    # pg.hotkey('ctrl', 'w')
    
    
        
    indice+=1 
