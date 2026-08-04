import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.isnull().sum()) # ¿Que columnas tienen datos faltantes?

print("--------------------------------------")

print(df.duplicated().sum()) # ¿Que filas estan duplicadas?

# PERFECTA LA CALIDAD