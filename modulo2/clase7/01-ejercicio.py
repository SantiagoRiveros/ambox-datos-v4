import pandas as pd

titanic = pd.read_csv("titanic.csv")

# Ejemplo 1: pasajeros sobrevivientes
survivors = titanic[titanic["Survived"] == "Yes"]
print(survivors)  # 342

# Ejemplo 2: mujeres en primera clase
women1stClass = titanic[(titanic["Sex"] == "F") & (titanic["Pclass"] == 1)]
""" 
(titanic["Sex"] == "F") & (titanic["Pclass"] == 1) <- Esto es el filtro
Podemos partirlo en 3 partes
titanic["Sex"] == "F" <- Aca, tomo del dataset, los que "Sex" = "F", las mujeres
titanic["Pclass"] == 1 <- Aca filtra los que son de primera clase
(titanic["Sex"] == "F") & (titanic["Pclass"] == 1) <- Los uno con el operador logico AND osea & para que el resultante
cumpla las dos condiciones

"""
print(women1stClass)  # 94


# Ejemplo 3: Pasajeros con tarifa superior a 50
fareExpensive = titanic[titanic["Fare"] > 50.0]
print(fareExpensive)  # 160

""" 
Pasajeros menores de 18 años
Hombres que no sobrevivieron
Pasajeros de clase 3 con tarifa menor a 10
"""

# Pasajeros menores de 18 años
lessThan18Years = titanic[titanic["Age"] < 18.0]
print(lessThan18Years)  # 113

# Hombres que no sobrevivieron
deceasedMen = titanic[(titanic["Sex"] == "M") & (titanic["Survived"] == "No")]
print(deceasedMen)  # 468

# Pasajeros de clase 3 con tarifa menor a 10
thirdClassCheapFare = titanic[(
    titanic["Pclass"] == 3) & (titanic["Fare"] > 10.0)]
print(thirdClassCheapFare)  # 167

# AGRUPACIONES

# Ejemplo 1: supervivencia por sexo
survivedBySex = titanic.groupby("Sex")["Survived"].value_counts()
print(survivedBySex)

""" 
titanic.groupby("Sex")["Survived"].value_counts()

groupby("Sex") <- Separamos la tabla por sexo ("M"/"F"), esto crea grupos
["Survived"] <- Elegis que columna vas analizar dentro de cada grupo
.value_counts() contabiliza los valores dentro de cada grupo

"""
