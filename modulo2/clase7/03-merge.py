import pandas as pd

usuarios = pd.DataFrame({
    "id": [1, 2, 3],
    "nombre": ["Ana", "Luis", "Carla"]
})

compras = pd.DataFrame({
    "id": [1, 2, 2],
    "producto": ["Mouse", "Teclado", "Monitor"]
})

print(usuarios)
""" 
   id nombre
0   1    Ana
1   2   Luis
2   3  Carla
"""
print(compras)
""" 
   id producto
0   1    Mouse
1   2  Teclado
2   2  Monitor
"""

# INNER JOIN
innerJoin = pd.merge(usuarios, compras, on="id")
print(innerJoin)

""" 
   id nombre producto
0   1    Ana    Mouse
1   2   Luis  Teclado
2   2   Luis  Monitor

Solo trae coincidencias entre ambas tablas
pd.merge(usuarios, compras, on="id")
dentro del merge, van distintas propiedades
las dos primeras, son los dataframes que va a unir
luego, el on="id" indica cual va a ser la clave comun para unirlas
"""

# LEFT JOIN
leftJoin = pd.merge(usuarios, compras, on="id", how="left")
print(leftJoin)

""" 
   id nombre producto
0   1    Ana    Mouse
1   2   Luis  Teclado
2   2   Luis  Monitor
3   3  Carla      NaN

Trae todos las filas de la izquierda, aunque no tengan coincidencias
y solo los de la derecha cuando tienen coincidencia
si alguna de las filas de la izquierda no tiene coincidencia, en la columna que se une, se pone como valor NaN

pd.merge(usuarios, compras, on="id", how="left")
es igual al inner, pero al final le agregamos how="left" para indicar que es un left join
"""

# Right Join
rightJoin = pd.merge(usuarios, compras, on="id", how="right")
print(rightJoin)

""" 
   id nombre producto
0   1    Ana    Mouse
1   2   Luis  Teclado
2   2   Luis  Monitor

trae todas las filas de la derecha aunque no coincidan con la izquierda
igual al left join pero inverso
how="right" <- indica que es left join

"""

# Outer Join
outerJoin = pd.merge(usuarios, compras, on="id", how="outer")
print(outerJoin)

""" 
   id nombre producto
0   1    Ana    Mouse
1   2   Luis  Teclado
2   2   Luis  Monitor
3   3  Carla      NaN

Trae todo aunque no tenga coincidencias de ambos lados
how="outer" <- indica que es outer
"""
