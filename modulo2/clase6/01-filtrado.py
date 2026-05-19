""" 
¿Quiénes sobrevivieron más?
¿Las mujeres sobrevivieron más?
¿Qué clase pagó más?
¿Qué edad promedio tenía cada clase?
"""

import pandas as pd

dataframe = pd.read_csv("titanic-corregido.csv")

# Primero veamos cantidad total de sobrevivientes
print(dataframe["Survived"].value_counts())
# No -> 549 | Yes -> 342
# Murieron más personas de las que sobrevivieron.

# Veamoslo en porcentaje
# normalize=True pasa este valor a porcentaje
print(dataframe["Survived"].value_counts(normalize=True))

# Vamos a la pregunta que mas se hace con este CSV
# ¿Las mujeres, sobrevivieron mas? -> Si, sobrevivieorn mas
print(dataframe.groupby("Sex")["Survived"].value_counts())

""" 
F    Yes         233
     No           81
M    No          468
     Yes         109
"""

# Veamos en porcentajes
print(dataframe.groupby("Sex")["Survived"].value_counts(normalize=True))

# Sobrevivieron un 74% de mujeres, y un 18% de hombres
# Conclusion -> Si, sobrevivieron MUCHO mas
# Porque? Se aplico la regla -> “Women and children first”


# Que clase pago mas?
# Promedio de tarifa por clase

print(dataframe.groupby("Pclass")["Fare"].mean())
""" 
1    84.154687
2    20.662183
3    13.675550
"""

# La primera calse pago mas del cuatruple que la segunda, por ende son los que pagaron pasajes mas caros

""" 
El Titanic reflejaba:

diferencias sociales enormes
lujo extremo en primera clase
condiciones muy malas en tercera
"""

# ¿QUÉ EDAD PROMEDIO TENÍA CADA CLASE?

# Promedio edad por clase
print(dataframe.groupby("Pclass")["Age"].mean())

""" 
1    37.092593
2    29.880435
3    26.478615
"""

# De que clase sobrevivieron mas?
print(dataframe.groupby("Pclass")["Survived"].value_counts())

""" 
1       Yes         136
        No           80
2       No           97
        Yes          87
3       No          372
        Yes         119
"""
# Hagamoslo en porcentaje
print(dataframe.groupby("Pclass")["Survived"].value_counts(normalize=True))
""" 
1       Yes         0.629630
        No          0.370370
2       No          0.527174
        Yes         0.472826
3       No          0.757637
        Yes         0.242363
"""

# ¿Que porcentaje del total viajaba en cada clase?
print(dataframe["Pclass"].value_counts(normalize=True) * 100)

# Supervivencia por sexo y clase
print(dataframe.groupby(
    ["Sex", "Pclass"]
)["Survived"].value_counts(normalize=True) * 100)

""" 
F    1       Yes         96.808511
             No           3.191489
     2       Yes         92.105263
             No           7.894737
     3       No          50.000000
             Yes         50.000000
M    1       No          63.114754
             Yes         36.885246
     2       No          84.259259
             Yes         15.740741
     3       No          86.455331
             Yes         13.544669
"""

# Mujeres -> Mas alta probabilidad de supervivencia, a esto se le suma segun su Pclass
