
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np



text="Maribel"+"\nHoy vivimos una gran experiencia de montaña, has concluido la distancia de 27k y no ha sido nada fácil, queremos felicitarte y darte las gracias por creer en Morron Trail run, una carrera hecha con amor a la que dedicamos mucho tiempo y esfuerzo; hoy te compartimos tu tiempo de carrera y posición general."
text1="*Tiempo de carrera*"+"\nTiempo oficial "+"3:00:04"+"\nGeneral "+"1"+"\nCategoria "+"1"

pywhatkit.sendwhatmsg_instantly(f'+573004719192',text)
time.sleep(1)
pg.hotkey('ctrl', 'w')
pywhatkit.sendwhatmsg_instantly(f'+573004719192',text1)
time.sleep(1)
pg.hotkey('ctrl', 'w')
    
    