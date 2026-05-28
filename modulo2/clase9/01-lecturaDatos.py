import pandas as pd

dataframe = pd.read_csv("day.csv")

# Vamos a ver el head y el tail
print("HEAD")
print(dataframe.head())

print("TAIL")
print(dataframe.tail())

print("SHAPE")
print(dataframe.shape)  # nos da -> (filas, columnas)


print("INFO")
print(dataframe.info())

print("ESTADISTICAS")
print(dataframe.describe())

print("COLUMNAS")
print(dataframe.columns)

print("Tipos de datos")
print(dataframe.dtypes)
