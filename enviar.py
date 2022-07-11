
import pandas as pd
#import pywhatkit
import numpy as np

class enviar:
    

    def leerDatos(self):
        df = pd.read_csv("morron22-07-06.csv")
        telefonos = df['Telefono de contacto']
        indice= 0
        enviados = [0]
        for i in telefonos:
            
            # for envio in range(0, len(enviados)):
            #     if i != enviados[envio]:
            #         print(f'{indice}  Felicitaciones {df["Nombre"][indice]} has logrado superar este gran reto de {df["Distancia"][indice]} kilometros, por encima de cualquier obsataculo llegaste a la meta en tan solo ya eres un campeón. ')
            #         indice+=1
            #         enviados.append(i)
                        
            #     else:
                   
            #         print(f"El mensaje ya ha sido enviado previamente al telefono: {i}")
                        # if int(df['Distancia'][indice]) == 27:
            if df['Soy'][indice] == 'Hombre':
                sexo = 'o'
            elif df['Soy'][indice] == 'Mujer':
                sexo = 'a'
            #print(f'+57{i}', f'Hola {df["Nombre"][indice]}  Bienvenid{sexo} a Morrón trail run 2022, ya eres parte de esta gran fiesta que viviremos el 17 de Julio \U0001F600 . Sigue entrenado \U0001F3C3 por que la montaña te está esperando \U0001F5FB. En los proximos días te estaremos enviando toda la información necesaria para el día de la carrera, un saludo \U0001F917.')
            pywhatkit.sendwhatmsg_instantly(f'+57{i}', f'Hola {df["Nombre"][indice]}  Bienvenid{sexo} a Morrón trail run 2022, ya eres parte de esta gran fiesta que viviremos el 17 de Julio \U0001F600 . Sigue entrenado por que la montaña te está esperando \U0001F3C3 \U0001F5FB. En los proximos días te estaremos enviando toda la información necesaria para el día de la carrera, un saludo \U0001F917.')
            
        
            # print(f'+57{i}','Para el reto de los 27k te enviamos una imagen con la altimetria y puntos de hidratación\
            # con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhatmsg_instantly(f'+57{i}','Para el reto de los 27k te enviamos una imagen con la altimetria y puntos de hidratación con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhats_image(f'+57{i}', './images/alt27k.jpg')
        #     pywhatkit.sendwhatmsg_instantly(f'+57{i}',"https://api.sports-tracker.com/apiserver/v1/workouts/export/AHFB3jbjh61bp-_VzmmtwwyTwzWY3z9mBKVxHbjmvA-Wv8pr9DuQ2NcTZY74iB7EaA==?brand=SUUNTOAPP")
        # elif int(df['Distancia'][indice]) == 12:
            # print(f'+57{i}','Para el reto de los 12k te enviamos una imagen con la altimetria y puntos de hidratación\
            # con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhatmsg_instantly(f'+57{i}','Para el reto de los 12k te enviamos una imagen con la altimetria y puntos de hidratación con el fin de que organices tu estrategia de carrera.')
            # pywhatkit.sendwhats_image(f'+57{i}', './images/alt12k.jpg')
        #     pass
        # print(indice,'  ',f'+57{i}', f'Envio a: {df["Nombre"][indice]} con exito')
        # if df['Talla de camiseta'][indice] == 0:
        #     print(f'{df["Nombre"][indice]} por favor confirmanos la talla de tu camiseta')
        # if df['EPS'][indice] == '1':
        #     print(f'{df["Nombre"][indice]} por favor confirmanos a que EPS perteneces')
        
        #print(f'Hola, {df["Nombre"][indice]} Bienvenid{sexo} a Morrón trail run tu numero es: {i}' )
        
        
         
        
        
            #print('El mensaje no pudo ser enviado')                                

if __name__ == "__main__":
    df = enviar()
    df.leerDatos()
