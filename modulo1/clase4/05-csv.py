# Comma Separated Values
import pandas as pd

# Como leemos un csv dentro de pandas?

dataframe = pd.read_csv("titanic.csv")

# head
print(dataframe.head())

# tail
print(dataframe.tail())

print("---------------------------------------")

# info
print(dataframe.info())

# describe
print(dataframe.describe())

# OBtenemos la cantidad de nulos
print(dataframe.isnull().sum())

# Reemplazamos los faltantes de edad, con el promedio
# Fillna, te rellena los nulos, el primer argumento es con que va a rellenar esos nulos, el segundo es el inplace
dataframe["Age"].fillna(dataframe["Age"].mean(), inplace=True)

print(dataframe.isnull().sum())

# Reemplazamos los faltantes de Embarked
dataframe["Embarked"].fillna("X", inplace=True)

print(dataframe.isnull().sum())

print(dataframe["Cabin"])

# Eliminemos Cabin
dataframe = dataframe.drop("Cabin", axis=1)

print(dataframe.isnull().sum())
