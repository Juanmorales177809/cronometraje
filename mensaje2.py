import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np



df = pd.read_csv("MorronTrailRun2022.csv")
telefonos = df['Telefono de contacto']
indice= 0
#df['Talla de camiseta']= df['Talla de camiseta'].fillna(0) 

for i in telefonos:
    num= str(i).replace('57','')   
    nombre = df["Nombre"][indice].title()
    text = f"Hola {nombre}"+"\nYa estamos a tan solo seis dias de" + "\nMorrón Trail run; esta semana es de"+"\nmucho descanso, pocos kilometros y" +"\nmuy buena alimentación;"+"\nnuestro nutricionista nos hace algunas"+"\nrecomendaciones para lo queda de "+"\nesta semana y para el día de la carrera."  
    text1 = "*Recomendaciones de Alimentación*"+"\n*Para 1 semana antes:* "+"Fuentes ricas en"+"\ncarbohidratos y bajos en grasas ( Pastas,"+"\nArroz, papa)"+ "\n"+"\n*Para el día de la carrera*"+"\n*Antes:* entre 1 y 2 horas, Desayunar y"+"\nrecuerda que debe ser bajo en Grasas."+ "\n*Durante:* en los puntos de avituallamiento"+"\ntendremos frutas, miel y otro productos" + "\n*Después:* frutas o algún otro alimento que" +"\ntraigas de tu casa."
    
    pywhatkit.sendwhatmsg_instantly(f'+57{i}',text)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    pywhatkit.sendwhatmsg_instantly(f'+57{i}',text1)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    pywhatkit.sendwhats_image(f'+57{i}', './images/entregaKit.jpeg')
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
   
   
    indice+=1                                 
                               