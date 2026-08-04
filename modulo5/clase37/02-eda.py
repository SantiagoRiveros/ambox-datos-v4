import pandas as pd 

df = pd.read_csv("dataset.csv")

# ¿Cuantos pacientes no asistieron?
print("¿Cuantos pacientes no asistieron?")

print(df["No-show"].value_counts())
""" 
No-show
No     88208
Yes    22319
"""
print("--------------------------------------")

# ¿Cuantos hombres y mujeres existen?
print("¿Cuantos hombres y mujeres existen?")

print(df["Gender"].value_counts())

""" 
Gender
F    71840
M    38687
"""

print("--------------------------------------")

# ¿Cual es la edad promedio?
print("¿Cual es la edad promedio?")

print(df["Age"].mean())

""" 
37.08887421173107
"""

print("--------------------------------------")

# ¿Cual es la edad maxima?
print("¿Cual es la edad maxima?")

print(df["Age"].max())

""" 115 """

print("--------------------------------------")

# ¿Cuantos pacientes tienen hipertension?
print("¿Cuantos pacientes tienen hipertension?")

print(df["Hipertension"].value_counts())

""" 
Hipertension
0    88726
1    21801
"""

print("--------------------------------------")

# ¿Cuantos pacientes tienen diabetes?
print("¿Cuantos pacientes tienen diabetes?")
print(df["Diabetes"].value_counts())

"""
Diabetes
0    102584
1      7943
"""

print("--------------------------------------")

# ¿Cuantos recibieron SMS?
print("¿Cuantos recibieron SMS?")

print(df["SMS_received"].value_counts())

""" 
SMS_received
0    75045
1    35482
"""

print("--------------------------------------")

# ¿Cuales son los barrios con mayor cantidad de turnos?
print("¿Cuales son los barrios con mayor cantidad de turnos?")

print(df["Neighbourhood"].value_counts().head(10))

""" 
Neighbourhood
JARDIM CAMBURI       7717
MARIA ORTIZ          5805
RESISTÊNCIA          4431
JARDIM DA PENHA      3877
ITARARÉ              3514
CENTRO               3334
TABUAZEIRO           3132
SANTA MARTHA         3131
JESUS DE NAZARETH    2853
BONFIM               2773
"""
print("--------------------------------------")

# ¿Existe relacion entre recibir SMS y asistir al turno?
print("¿Existe relacion entre recibir SMS y asistir al turno?")

print(pd.crosstab(df["SMS_received"], df["No-show"]))

""" 
No-show          No    Yes
SMS_received              
0             62510  12535
1             25698   9784
"""
# Parece que si hay relacion

print("--------------------------------------")

# ¿Existe relacion entre tener diabetes o hipertension con faltar al turno?

print("¿Existe relacion entre tener diabetes o hipertension con faltar al turno?")

print("DIABETES")
print(pd.crosstab(df["Diabetes"], df["No-show"]))
""" 
No-show      No    Yes
Diabetes              
0         81695  20889
1          6513   1430
"""
print("HIPERTENSION")
print(pd.crosstab(df["Hipertension"], df["No-show"]))
""" 
No-show          No    Yes
Hipertension              
0             70179  18547
1             18029   3772
"""

print("--------------------------------------")

# ¿La edad promedio cambia entre quienes asisten y quienes no?
print("¿La edad promedio cambia entre quienes asisten y quienes no?")

print(df.groupby("No-show")["Age"].mean())

""" 
No-show
No     37.790064
Yes    34.317667
"""

