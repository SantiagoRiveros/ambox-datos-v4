import pandas as pd

dataframe1 = pd.DataFrame({
    "id": [1, 2],
    "nombre": ["Ana", "Luis"]
})

dataframe2 = pd.DataFrame({
    "id": [3, 4],
    "nombre": ["Carla", "Pedro"]
})

# Yo quiero analizar ambos, no me sirve analizarlos por separado
# Con Concat, en este caso puedo unirlos

dataframeFinal = pd.concat([dataframe1, dataframe2])
print(dataframeFinal)

""" 
   id nombre
0   1    Ana
1   2   Luis
0   3  Carla
1   4  Pedro

porque me muestra 0 1 0 1 en los indices?
por que, sigue tomando los indices del dataframe original que componian
"""

# reset de indice
dataframeFinal2 = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframeFinal2)

""" 
   id nombre
0   1    Ana
1   2   Luis
2   3  Carla
3   4  Pedro

Me reseteo los indices para que correspondan al dataframe final.
"""

# Ahora, imaginemos que le queremos agregar una columna mas, edad
dataframe3 = pd.DataFrame({
    "edad": [31, 42, 23, 19]
})

# axis=1 indica que se concatene como columna y no como fila
dataframeFinal3 = pd.concat([dataframeFinal2, dataframe3], axis=1)

print(dataframeFinal3)
