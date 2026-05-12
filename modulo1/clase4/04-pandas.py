# Que es pandas?
# Libreria para manipular y analizar datos tabulares

# Que es un dato tabular?
# Es como una tabla, con filas y columnas

import pandas as pd

datos = {
    "nombre": ["Ana", "Juan", "Luis"],
    "edad": [20, 30, 25],
    "ciudad": ["Buenos Aires", "Córdoba", "Rosario"]
}

dataframe = pd.DataFrame(datos)

print(dataframe)

# Metodo para ver las 5 primeras filas
print(dataframe.head())

# Metodo para ver las 5 ultimas filas
print(dataframe.tail())

# Informacion general
print(dataframe.info())

# Caracteristicas principales
print(dataframe.describe())

""" 
Count -> Cantidad
mean -> promedio
std -> desviacion estandar
min -> El valor minimo
25-50-75% -> Cuartiles
max -> El valor maximo
"""

# Como accedemos a una columna?
print(dataframe["nombre"])


# Filtros

# Como hago yo, para mostrar, por ejemplo, los que tienen edad > 25
print(dataframe[dataframe["edad"] > 25])


# Nueva columna
dataframe["sueldo"] = 1000


print(dataframe)

# Modificar columna
dataframe["sueldo"] = dataframe["sueldo"] * 1.1

print(dataframe)

# Eliminar columna
dataframe.drop(columns=["sueldo"], inplace=True)
# inplace determina si se sobreescribe el dataframe original
