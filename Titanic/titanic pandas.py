import pandas as pd
import numpy as np
#Mediante pandas traemos la url del titanic para poder trabajar sobre la misma
df = pd.read_csv("https://raw.githubusercontent.com/NotAyushXD/Titanic-dataset/master/train.csv")

print("Separador--------------")#Con esta linea podemos ver con separacion de la sigt funcion
print(df.head()) #Con esta funcion, nos traera los primeros 5 elementos del dataframe tambien podemos utilizarlo de la sigt forma print(df.head(5)) ya que el numero condiciona la funcion y el no colocarlo por defecto nos trae los primeros 5
print("Separador--------------")
print(df.tail())#Con esta funcion, nos traera los primeros 5 elementos del dataframe tambien podemos utilizarlo de la sigt forma print(df.tail(5)) ya que el numero condiciona la funcion y el no colocarlo por defecto nos trae los primeros 5
print("Separador--------------")

print("La cantidad de columnas es de: ", len(df.columns)) #Esta funcion nos traera la cantidad de columnas traidas por el data frame

print("Separador--------------")
print("La cantidad de filas es de: ", len(df.index)) #Esta funcion nos traera la cantidad de filas traidas por el data frame
print("Separador--------------")
print("La cantidad recaudada fue de: ", df["Fare"].sum()) #Esta funcion nos sumara todo lo de la columna de Fare, se puede hacer lo mismo con cualquier otra columna teniendo en cuenta de llamarla anteriormente
print("Separador--------------")
print("La cantidad de pasajeros en primera clase son ", sum(df.Pclass==1)) #Esto nos traera la suma de los pasajeros de primera clase
print("Separador--------------")
#Con la siguiente funcion lo que logramos es poder traer de la columna de Pclass y poder graficarlos.
print("Primera clase",np.array(sum(df.Pclass==1)),"Segunda clase",np.array(sum(df.Pclass==2)),"Tercera clase",np.array(sum(df.Pclass==3)))

print(df.pivot(index=['Pclass']))

print('''
dasdasdasdajn
fsajdasd
sajfdnjasdfasf''')
