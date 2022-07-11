import mysql.connector
import pandas as pd
import numpy as np




# connection= mysql.connector.connect(host='localhost',
#                                     database= 'Morron',
#                                     user= 'root',
#                                     password= 'N96phxst')


# df = pd.read_csv("MorronTrailRun2022.csv", sep=';')
# nombres = df["Nombre"]
# apellidos = df["Apellidos"]




def leerDatos():
        df = pd.read_csv("MorronTrailRun2022_2.csv", sep= ',')
        
        nombres = df["Nombre"]
        apellidos = df["Apellidos"]
        
        nombre = []
        salida = []
        llegada = []
        tiempo = []
        numeroCorredor = []
        posicion= np.zeros(len(df["Nombre"]))
        estado= []
        categoria = []
        for indice in range(0, len(nombres)):
            nombre.append(nombres[indice].title()+" "+apellidos[indice].title())
            salida.append("Salida")
            llegada.append("Salida")
            tiempo.append("Salida")
            estado.append('Linea de Partida')
            numeroCorredor.append("No asignado")
            if df["Edad"][indice] < 40:
                if df["Soy"][indice] == "Mujer":
                    categoria.append("Elite femenino")
                else:
                    categoria.append("Elite masculino")
            else:
                if df["Soy"][indice] == "Mujer":
                    categoria.append("Master femenino")
                else:
                    categoria.append("Master maculino") 
        data = {"#": numeroCorredor, "Nombres": nombre, "# Documento": df["Numero de documento"],
                "Distancia [Km]": df["Distancia"],"Puesto": posicion, "Categoria": categoria,
                "Hora Salida": salida, "Hora Llegada": llegada, "Tiempo de Carrera":tiempo,
                "Estado": estado,"Telefono": df["Telefono de contacto"],
                }
        keyss= list(data.keys())
        df= pd.DataFrame(data)
        
        df.to_csv('example.csv',index=False)
        df1 = pd.read_csv('example.csv',)
        print(df1.columns)

if __name__ == "__main__":
    leerDatos()