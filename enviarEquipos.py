from ast import Try
import pandas as pd
import pywhatkit
import numpy as np


df = pd.read_csv("MorronTrailRun2022-SinCamiseta (respuestas) - Respuestas de formulario 1.csv")
telefonos = df['Telefono de contacto']
indice= 0
#df['Talla de camiseta']= df['Talla de camiseta'].fillna(0) 

for i in telefonos:
      
    num= str(i).replace('57','')   
    if df['Soy'][indice] == 'Hombre':
        sexo = 'o'
    elif df['Soy'][indice] == 'Mujer':
        sexo = 'a'
    nombre = df["Nombre"][indice].title()
    print(f'Hola, {nombre} Bienvenid{sexo} a Morrón trail run  tu numero es: {num}' )
    if int(df['Distancia en kilometros [Km]'][indice]) == 27:
        pywhatkit.sendwhatmsg_instantly(f'+57{i}', f'Hola {df["Nombre"][indice]}  Bienvenid{sexo} a Morrón trail run 2022, ya eres parte de esta gran fiesta que viviremos el 17 de Julio \U0001F600 . Sigue entrenado por que la montaña te está esperando \U0001F3C3 \U0001F5FB. En los proximos días te estaremos enviando toda la información necesaria para el día de la carrera, un saludo \U0001F917.')
        print('El reto de los 27k no es facil, así que te enviamos una imagen con la altimetria y puntos de hidratación\
            para que organices tu estrategia de carrera.')
    elif int(df['Distancia en kilometros [Km]'][indice]) == 12:
        print('El reto de los 12 kilometros no es facil, así que te enviamos una imagen con la altimetria y puntos de hidratación\
            para que organices tu estrategia de carrera .')
    