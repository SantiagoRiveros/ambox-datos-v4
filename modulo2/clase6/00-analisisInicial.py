# Empezamos importando pandas para su uso
import pandas as pd

# Ahora importamos el dataframe del titanic
dataframe = pd.read_csv("titanic.csv")

# Ahora, deberiamos analizar cuantos nulos tengo
print(dataframe.isnull().sum())

# El isnull, te devuelve en cada fila, True si es que es nulo o BLANK
# Entonces, isnull, aplicado sobre el dataframe, nos devuelve True todas las filas que esten nulas
# Sum, nos suma todas esas filas, y nos devuelve como un numero
# POr ende, sabriamos cuantas filas por columna son nulas

# Age -> 177 Nulos, esta columna es MUY importante
# Cabin -> 687 Nulos, son la gran mayoria, esta columna no es importante
# Embarked -> 2 Nulos, esta columna es importante

# Tipos de datos:
# Age -> Numerico
# Cabin -> Texto
# Embarked -> Texto

dataframe["Age"] = dataframe["Age"].fillna(dataframe["Age"].mean())

# fillna() rellena los nulos
# mean() devuelve el rpomedio
# Por ende, se rellenan los nulos, con el promedio

# Volvemos a usar el print para ver si no nos quedaron nulos en age
print(dataframe.isnull().sum())

# Ahora nos quedan Cabin y Embarked
dataframe["Embarked"] = dataframe["Embarked"].fillna("X")

# Volvemos a usar el print para ver si no nos quedaron nulos en embarked
print(dataframe.isnull().sum())

# Elimino la columna Cabin
dataframe = dataframe.drop("Cabin", axis=1)


print(dataframe.isnull().sum())

# Detectamos duplicados
print(dataframe.duplicated().sum())  # Da 0 duplicados

# Vamos a reemplazar el survived 0/1 por yes/no
# dataframe["Survived"] = dataframe["Survived"].map({0: "No", 1: "Yes"})

print(dataframe["Survived"])

# Vamos a reemplazar lo de EMbarked por el nombre completo de la ciudad
dataframe["Embarked"] = dataframe["Embarked"].map(
    {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton", "X": "Unknown"})

print(dataframe["Embarked"])

# Vamos a reemplazar male/female por M/F
dataframe["Sex"] = dataframe["Sex"].map({"male": "M", "female": "F"})
print(dataframe["Sex"])

# Borramos ticket
dataframe = dataframe.drop("Ticket", axis=1)

# Sacamos los decimales "raros" en edad
dataframe["Age"] = round(dataframe["Age"], 0)

dataframe.to_csv("titanic-corregido2.csv", index=False)
