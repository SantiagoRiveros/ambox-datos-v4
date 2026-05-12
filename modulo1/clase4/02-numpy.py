# Como traemos numpy a nuestro archivo?
import numpy as np

# Que es numpy?
# Es una libreria para calculos matematicos con arrays numericos de manera rapida y eficiente
numeros = np.array([1, 2, 3, 4])

print(numeros)

# Sum devuelve la sumatoria de todos los elementos del array
print("sum", numeros.sum())

# mean devuelve el promedio del array
print("mean", numeros.mean())

# max devuelve el numero maximo del array
print("max", numeros.max())

# min devuelve el numero minimo del array
print("min", numeros.min())

# Como hariamos si queremos multiplicar * 2 todos los elementos del array?
print(numeros * 2)

# np.arange(numeroIncial, finDelRango) nos crea un array con los numeros dentro del rango
nuevoArray = np.arange(1, 11)

print(nuevoArray)

arrayZeros = np.zeros(5)

print(arrayZeros)

# OJO! Tema complicado abajo

# Que es una matriz? Es un array bidimensional
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Como accedemos al 2, por ejemplo?

print(matriz[0][1])
