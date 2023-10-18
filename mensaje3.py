import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np


df = pd.read_csv("ultimos.csv")
telefonos = df['Telefono de contacto']
indice= 0
contador = 0
for i in telefonos:
    num= str(i).replace('57','') 
    nombre = df["Nombre"][indice].title()

    text = f"Hola {nombre}, hoy queremos " + "\ncompartir con tigo algunos consejos de"+"\nhidratación que nuestro entrenador" +"\nSantiago Villa recomienda para no" +"\nsufrir los efectos de la deshidratación"+ "\nen la montaña" 
    text1 = "*Recomendaciones de Hidratación*"+"\n*Para 1 semana antes:* Tomar "+"constantemente suero o bebidas "+"\nhidratantes."+ "\n"+"\n*Para el día de la carrera*"+"\n*Antes:* entre 1 y 2 horas antes tomar 400"+"\no 600 ml de bebida isitónica."+ "\n*Durante:* Tomar 250ml por cada 20 - 25 minutos de carrera."+ "\n*Después:* Cuando llegues a meta" +"\ncomienza tu rehidratación al menos"+"\n750ml de bebida te pueden ayudar"
    
     
    pywhatkit.sendwhatmsg_instantly(f'+57{i}',text1)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    
    
        
    indice+=1 
