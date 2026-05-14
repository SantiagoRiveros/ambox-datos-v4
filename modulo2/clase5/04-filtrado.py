import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# Seleccionar columna
print("Seleccionar columna")
print(dataframe["Fare"])

# Seleccionamos varias columnas
print("Seleccionamos varias columnas")
print(dataframe[["Fare", "Pclass"]])

# filtrar filas
print("Filtramos los mayores de 30 años")
print(dataframe[dataframe["Age"] > 30])

print("Filtramos solo los hombres")
print(dataframe[dataframe["Sex"] == "male"])

# Podemos combinar expresiones
# Mostrar solo hombres mayores de 30.
print("Solo hombres mayores de 30")
print(dataframe[(dataframe["Sex"] == "male") & (dataframe["Age"] > 30)])

# Ordenar
print("Ordenado por edad")
print(dataframe["Age"].sort_values())  # Ordena por edad

print("Ordenado de manera descendente por edad")
print(dataframe["Age"].sort_values(ascending=False))

""" 
personas mayores a 40
mujeres
pasajeros de primera clase
"""

print("Personas mayores a 40")
print(dataframe[dataframe["Age"] > 40])

print("Mujeres")
print(dataframe[dataframe["Sex"] == "female"])

print("Pasajeros de primera clase")
print(dataframe[dataframe["Pclass"] == 1])

# renombrando columnas
spanishDataframe = dataframe.rename(columns={
    "PassengerId": "IdPasajero",
    "Survived": "Sobrevivio",
    "Pclass": "ClasePasajero",
    "Name": "Nombre",
    "Sex": "Sexo",
    "Age": "Edad",
    "SibSp": "HerPa",
    "Parch": "PaHi",
    "Fare": "Precio",
    "Cabin": "Cabina",
    "Embarked": "Embarco"
})

print(spanishDataframe.columns)

""" 
promedio edad
cantidad hombres/mujeres
pasajero más viejo
tarifa máxima
"""

# PRomedio edad
print("Promedio Edad")
print(dataframe["Age"].mean())

# Cantidad hombres/Mujeres
print("Cantidad hombres/mujeres")
print(dataframe["Sex"].value_counts())

# Pasajero mas viejo
print("Pasajero mas viejo")
print(dataframe[dataframe["Age"] == dataframe["Age"].max()])

print("Tarifa mas alta")
print(dataframe[dataframe["Fare"] == dataframe["Fare"].max()])

""" 
menores de 18
sobrevivientes
mujeres de primera clase
"""

print("Menos de 18")
print(dataframe[dataframe["Age"] < 18])

print("Sobrevivientes")
print(dataframe[dataframe["Survived"] == 1])

print("Mujeres de primera clase")
print(dataframe[(dataframe["Sex"] == "female") & (dataframe["Pclass"] == 1)])
