from ast import Try
import pandas as pd
import pywhatkit
import numpy as np



df = pd.read_csv("Morronformulario2.csv")
telefonos = df['Telefono de contacto']
indice= 0
for i in telefonos:
    try: 
       
          
        if df['Soy'][indice] == 'Hombre':
            sexo = 'o'
        elif df['Soy'][indice] == 'Mujer':
            sexo = 'a'
        
        # pywhatkit.sendwhatmsg_instantly(f'+57{i}', f'Hola {df["Nombre"][indice]}  Bienvenid{sexo} a\
        #                                     Morrón trail run 2022, tu pago ha sido confirmado con exito;\
        #                                         Esperamos que estes entrenando \U0001F3C3 por que esta\
        #                                             montaña \U0001F5FB no es nada fácil \U0001F625 , aun así tenemos la plena certeza\
        #                                                 que lograras este reto que has puesto en tu camino \U0001F600; en los \
        #                                                     próximos días te estaremos enviando toda la información\
        #                                                         para el día de la carrera, un saludo \U0001F917.')
        
        if df['Distancia'][indice] == 27:
            print(f'+57{i}','Para el reto de los 27k te enviamos una imagen con la altimetria y puntos de hidratación\
                    con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhatmsg_instantly(f'+57{i}','Para el reto de los 27k te enviamos una imagen con la altimetria y puntos de hidratación\
            # con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhats_image(f'+57{i}', './images/alt27k.jpg')
        elif df['Distancia'][indice] == 12:
            print(f'+57{i}','Para el reto de los 12k te enviamos una imagen con la altimetria y puntos de hidratación\
                    con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhatmsg_instantly(f'+57{i}','Para el reto de los 12k te enviamos una imagen con la altimetria y puntos de hidratación\
            # con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhats_image(f'+57{i}', './images/alt12k.jpg')
    
        if df['EPS'][indice] == '1':
            print(f'+57{i}',f'{df["Nombre"][indice]} por favor confirmanos a que EPS perteneces')
            # pywhatkit.sendwhatmsg_instantly(f'+57{i}',f'{df["Nombre"][indice]} por favor confirmanos a que EPS perteneces')
        
        
        
        
        indice+=1  
    except:
        print('El mensaje no pudo ser enviado')                                
                                    