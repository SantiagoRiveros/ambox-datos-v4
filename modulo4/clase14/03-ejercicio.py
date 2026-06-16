""" Histograma de edades.
Barras de pasajeros por clase.
Barras de supervivientes por sexo.
Scatter edad vs tarifa.
Pie chart de pasajeros por puerto de embarque. """

import pandas as pd
import matplotlib.pyplot as plt

# Vamos a leer el csv
dataframe = pd.read_csv("titanic.csv")

# Histograma de edades
# Ver como se distribuyen las edades de los pasajeros
# El dropna esta puesto por si le quedaron nulos
plt.hist(dataframe["Age"].dropna())

plt.title("Distribucion de edades")
plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")

plt.savefig("distribucion-de-edades.jpg")
plt.clf()

# La mayoria esta entre 25 y 45 años
# Poco uniforme la distribucion
# Hay pocos niños y pocos ancianos


# Barras de pasajeros por clase.
# Ver cuantos pasajeros viajaban por clase
pasajeros_por_clase = dataframe["Pclass"].value_counts()

print(pasajeros_por_clase)
plt.bar(
    pasajeros_por_clase.index,  # Son las clases, 1 2 y 3
    pasajeros_por_clase.values  # Son la cantidad de pasajeros por clase
)

plt.title("Pasajeros por clase")
plt.xlabel("Clase")
plt.ylabel("Cantidad")

plt.savefig("pasajeros-por-clase.jpg")
plt.clf()

# La tercer clase es la que mas pasajeros tenia
# La segunda clase es minoria

# Barras de supervivientes por sexo.
# Quien sobrevivio mas

# Paso 1 -> Agrupar
supervivientes = dataframe[dataframe["Survived"] == "Yes"]

# Paso 2 -> Contar
por_sexo = supervivientes["Sex"].value_counts()

# Paso 3 -> Graficar
plt.bar(
    por_sexo.index,
    por_sexo.values
)

plt.title("Supervivientes por sexo")
plt.xlabel("Sexo")
plt.ylabel("Cantidad")
plt.savefig("Supervivientes-por-sexo.jpg")
