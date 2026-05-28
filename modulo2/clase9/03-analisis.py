import pandas as pd

dataframe = pd.read_csv("dataframe_mejorado.csv")

# Dias con mas de 5000 alquileres
print("Dias con mas de 5000 alquileres")
print(dataframe[dataframe["total_alquileres"] > 5000])
print("----------")

# Dias frios
print("Dias frios")
print(dataframe[dataframe["temperatura"] < 10])
print("----------")

# Dias calurosos
print("Dias calurosos")
print(dataframe[dataframe["temperatura"] >= 30])
print("----------")

# Dias laborales
print("Dias laborales")
print(dataframe[dataframe["workingday"] == 1])
print("----------")

# Dias no laborales
print("Dias no laborales")
print(dataframe[dataframe["workingday"] == 0])
print("----------")

# Ordenar por alquileres
print("Dataframe ordenado por alquileres")
print(dataframe.sort_values(by="total_alquileres", ascending=False))
print("----------")

# PAsamos dteday a datetime para poder filtrar
dataframe["dteday"] = pd.to_datetime(dataframe["dteday"])


# dias desde 15/09/2011 al 20/12/2011
print("Dias desde 15/09/2011 al 20/12/2011")
print(dataframe[(dataframe["dteday"] >= "2011-09-15")
      & (dataframe["dteday"] <= "2011-12-20")])
print("----------")

# Dia de la semana uqe mas se alquila
print(dataframe.groupby("weekday")["total_alquileres"]
      .sum()
      .sort_values(ascending=False))
print("----------")

# Promedio Alquileres por estacion
print("Promedio alquileres por estacion")
print(dataframe.groupby("season")["total_alquileres"].mean())
print("----------")

# Promedio alquileres por clima
print("Promedio alquileres por clima")
print(dataframe.groupby("clima")["total_alquileres"].mean())
print("----------")

# Promedio temperatura por estacion
print("Promedio temperatura por estacion")
print(dataframe.groupby("season")["temperatura"].mean())
