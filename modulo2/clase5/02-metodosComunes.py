# Importamos pandas
import pandas as pd

# Leemos el CSV
dataframe = pd.read_csv("titanic.csv")

# print
print(dataframe.info())

# Vemaos las 5 primeras filas

print(dataframe.head())

# Veamos una cantidad persoinalizada de las primeras filas
print(dataframe.head(10))

# Veamos las ultimas 5 filas

print(dataframe.tail())

# Veamos cantidad personalizada de las ultimas filas
print(dataframe.tail(10))

print("-------------------------------")

# Vamos a ver los datos descriptivos:
print(dataframe.describe())

print("-------------------------------")

# Mostrar columnas
print(dataframe.columns)

print("-------------------------------")

# MOstrar indices
print(dataframe.index)

print("-------------------------------")

# Mostrar "forma" del dataframe
print(dataframe.shape)
print("-------------------------------")

# Mostrar valores unicos
print(dataframe["Sex"].unique())  # male female

print(dataframe["Survived"].unique())

print(dataframe["Pclass"].unique())

# Contar valores
print("-------------------------------")
print(dataframe["Sex"].value_counts())

print(dataframe["Survived"].value_counts())
print(dataframe["Pclass"].value_counts())
