import numpy as np

# Lista python
numerosLista = [1, 2, 3, 4]

# Array Numpy
numerosArray = np.array([1, 2, 3, 4])

""" 
Un array:
-Ocupa menos memoria
-Es mas rapido
-Permite operaciones masivas y rapidas
"""

print("LISTA")
print(numerosLista)
print("ARRAY")
print(numerosArray)

print("Sumatoria")
print(numerosArray.sum())  # 10
print("Promedio")
print(numerosArray.mean())  # 2.5
print("Maximo")
print(numerosArray.max())  # 4
print("Minimo")
print(numerosArray.min())  # 1

# Podemos hacer operaciones masivas de manera resumida
# Que pasa si yo tengo un array de sueldos, y quiero subirle un 20%?
sueldos = np.array([1000, 2000, 1500, 1200, 1300])
# sueldosConAumento = sueldos * 1.20 <- Con una lista comun da error
sueldosConAumento = sueldos * 1.20
print(sueldosConAumento)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

array3 = array1 + array2
print(array3)
array4 = array1 * array2
print(array4)

array1Potencia = array1 ** 3
print(array1Potencia)

print("------------------")
# Crear arrays automaticamente
# Esto, me devuelve un array, con los numeros desde el primero que le pongo entre parentesis hasta el ultimo (Sin incluirlo)
arrayAutomatico = np.arange(1, 11)
print(arrayAutomatico)
