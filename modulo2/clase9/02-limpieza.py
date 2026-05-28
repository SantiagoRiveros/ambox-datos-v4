import pandas as pd

dataframe = pd.read_csv("day.csv")

# Ver nulos
print(dataframe.isnull().sum())  # 0 nulos

# Ver duplicados
print("DUPLICADOS")
print(dataframe.duplicated().sum())

# Renombramos columnas
dataframe.rename(columns={
    "cnt": "total_alquileres",
    "temp": "temperatura",
    "hum": "humedad",
    "yr": "year",
    "mnth": "month"
}, inplace=True)

# Creamos columna nueva
dataframe["usuarios_totales"] = (dataframe["casual"] + dataframe["registered"])
print(dataframe["usuarios_totales"])

# cuando la temperatura esta normalizada -> tempNormalizada * 41 = temperaturaReal

dataframe["temperatura"] = dataframe["temperatura"] * 41

print(dataframe["temperatura"])

# Creamos columna clima
dataframe["clima"] = dataframe["weathersit"].map({
    1: "Despejado",
    2: "Nublado",
    3: "Lluvioso",
    4: "Tormenta"
})

dataframe["season"] = dataframe["season"].map(
    {1: "springer", 2: "summer", 3: "fall", 4: "winter"})

dataframe.to_csv("dataframe_mejorado.csv")
