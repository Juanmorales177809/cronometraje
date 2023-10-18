import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import numpy as np

def leer_datos(archivo):
    df = pd.read_excel(archivo)
    return df

def vec_telefonos(dataframe):
    telefonos = dataframe["TELEFONO CELULAR "].tolist() #convertir la columna TELEFONO CELULAR en una lista
    contador = 0    
    for x in telefonos:
        if str(x) == "nan":
            contador += 1
    telefonos = [0 if str(x) == "nan" else x for x in telefonos]
    return telefonos

def vec_nombres(dataframe):
    nombres = dataframe["NOMBRE Y APELLIDOS"].tolist() #convertir la columna TELEFONO CELULAR en una lista
    contador = 0    
    for x in nombres:
        if str(x) == "nan":
            contador += 1
    nombres = [0 if str(x) == "nan" else x for x in nombres]
    return nombres

def enviar_whatsapp(telefono, mensaje):
    pywhatkit.sendwhatmsg_instantly(f'+57{telefono}', mensaje)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
def enviar_imagen(telefono, imagen):
    pywhatkit.sendwhats_image(f'+57{telefono}', imagen)
    time.sleep(1)
    pg.hotkey('ctrl', 'w')

# if __name__ == "__main__":
#     imagen = "./img/INFOCROSSCOUNTRY.png"
#     archivo = "docs/Formulario cross country.xlsx"
#     df = leer_datos(archivo)
#     telefonos = vec_telefonos(df)
#     nombres = vec_nombres(df)
#     mensaje = "Hola, este es un mensaje de prueba"
#     for telefono in telefonos:
#         enviar_whatsapp(telefono, mensaje)
#         enviar_imagen(telefono, imagen)

