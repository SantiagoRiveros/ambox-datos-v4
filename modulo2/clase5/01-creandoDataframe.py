import pandas as pd
# Recordemos que el "pd" es un alias que le damos a la libreria

# Vamos a crear el diccionario con el cual vamos a crear el dataframe

datos = {
    "nombre": ["Ana", "Juan", "Luis"],
    "edad": [20, 30, 25],
    "ciudad": ["Buenos Aires", "Cordoba", "Rosario"]
}

# Aca convertimos el diccionario en un dataframe
dataframe = pd.DataFrame(datos)

print(dataframe)

datos2 = [{"nombre": "Ana", "edad": 20, "ciudad": "Buenos Aires"},
          {"nombre": "Juan", "edad": 30, "ciudad": "Cordoba"}, {"nombre": "Luis", "edad": 25, "ciudad": "Rosario"}]

dataframe2 = pd.DataFrame(datos2)
print(dataframe2)

dataframe.to_csv("dataframe-usuarios.csv")
