import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np


df = pd.read_csv("example2.csv")
telefonos = df['Telefono']
indice= 0
contador = 0
for fila in range(0,len(df['Telefono'])):
    nombre = df["Nombres"][fila].title()
    text=f"{nombre}"+f"\nHoy vivimos una gran experiencia de montaña, has concluido la distancia de {df['Distancia [Km]'][fila]}k y no ha sido nada fácil, queremos felicitarte y darte las gracias por creer en Morron Trail run, una carrera hecha con amor a la que dedicamos mucho tiempo y esfuerzo; hoy te compartimos tu tiempo de carrera y posición general."
    text1="*Tiempo de carrera*"+"\nTiempo oficial "+f"{df['Tiempo de Carrera'][fila]}"+"\nGeneral "+f"{df['General'][fila]}"+"\nCategoria "+f"{df['Puesto Cat'][fila]}"
    # text = f"{nombre} mañana es el gran día, te esperamos desde las 6:00am para el calentamiento y para que escuches a nuestro director de carrera contarte todos los por menores de la ruta. A las 7:00 am estaremos dando la partida. Adicional te compartimos la ubicación de la unidad deportiva cristo rey. *Nos vemos en la montaña*. https://maps.app.goo.gl/hup2bc1wpUnbrjqJ8"
    # text1 = "https://maps.app.goo.gl/hup2bc1wpUnbrjqJ8" 
    pywhatkit.sendwhatmsg_instantly(f'+57{df["Telefono"][fila]}',text)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    pywhatkit.sendwhatmsg_instantly(f'+57{df["Telefono"][fila]}',text1)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    
    
        
    indice+=1 
