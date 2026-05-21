# Similar al merge pero con indices

import pandas as pd


# En este ejemplo dejamos que panda asigne sus indices de manera automatica
dataframe1 = pd.DataFrame({
    "Nombre": ["Ana", "Luis"]
})

dataframe2 = pd.DataFrame({
    "edad": [32, 19]
})

dataframe1 = dataframe1.join(dataframe2)
# Esto une ambos dataframes por su indice, en este caos dejamos que pandas lo asigne automaticamente
print("Dataframe1")
print(dataframe1)
print("Dataframe2")
print(dataframe2)

# Ahora le asignamos los indices nosotros

dataframeA = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Ruben"]
}, index=[1, 2, 4])

print(dataframeA)

dataframeB = pd.DataFrame({
    "edad": [32, 19, 41]
}, [1, 2, 3])

print(dataframeB)

print("JOINEANDO")
print(dataframeA.join(dataframeB))

# Me trajo todas las filas del dataframeA y solo las del B que coinciden, es como un left Join
