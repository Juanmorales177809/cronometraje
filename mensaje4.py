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
    text = f"Hola {nombre}"+"\nSoy Hildebrando Machado corredor de Ultra Trail running, creador y director de Morron Trail run, hoy quiero saludarte y compartir contigo algunos detalles importantes para el día de la carrera."
    text1 = "*1.* La carrera sale de la unidad deportiva "+"\ncristo rey en Copacabana y termina en "+"\nel mismo lugar."+"\n*2.* La hora de salida para las distancias "+"\nde 12k y 27k será a las 7:00am el día"+"\ndomingo."+"\n*3.* La unidad deportiva cuenta con "+"\nparqueadero para motos y carros,"+"\ntambién llega el bus alimentador desde"+"\nla estación del metro de Niquía, solo"+"\nverifica que diga Cristo Rey."+"\nNo queda mas que despedirme y decirte: *Nos vemos en la montaña* \U0001F3C3 \U0001F5FB"
    pywhatkit.sendwhatmsg_instantly(f'+57{i}',text)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    pywhatkit.sendwhatmsg_instantly(f'+57{i}',text1)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    
    
        
    indice+=1 
