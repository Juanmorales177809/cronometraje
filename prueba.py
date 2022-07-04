
import pandas as pd
import pywhatkit
import numpy as np

# msg = '''text \U0001F600 \n 

# new line

# \U0001F600 '''

iki= ['3016868154', '3016868154']
name= ["Santiago", "Caliche", ]
for i in range(0,len(iki)):
    
    pywhatkit.sendwhatmsg_instantly(f'+57{iki[i]}',f'Hola {name[i]}  Bienvenido a Morrón trail run 2022, ya eres parte de esta gran fiesta que viviremos el 17 de Julio \U0001F600 . Sigue entrenado \U0001F3C3 por que la montaña te está esperando \U0001F5FB. En los proximos días te estaremos enviando toda la información necesaria para el día de la carrera, un saludo \U0001F917.')
    
    pywhatkit.sendwhatmsg_instantly(f'+57{iki[i]}','El reto de los 27k no es facil, así que te enviamos una imagen con la altimetria y puntos de hidratación\
                                        para que organices tu estrategia de carrera.')
    pywhatkit.sendwhats_image(f'+57{iki[i]}', './images/alt27k.jpg')
                                        
# c= '\U0001F3C3 \U0001F5FB'

# pywhatkit.sendwhatmsg_instantly(f'+57{i}' , c)
