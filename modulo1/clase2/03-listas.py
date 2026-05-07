# Que es una lista?
# Una lista es una coleccion de elementos ordenados

numeros = [1, 2, 3, 4]
# indice   0  1  2  3
# Los indices se empiezan SIEMPRE a contar desde 0


nombres = ["Ana", "Luis", "Pedro"]
# indice    0       1       2

# Se escribe, entre corchetes, y sus elementos estna divididos por comas
# Cada elemento, ocupa una posicion definida
# Estas posiciones, se llaman indices

# Entonces, como accedo a un elemento en un indice?
lista = [3, 9, 2]
# Quiero imprimir el 9, indice 1
print(lista[1])

lista[1] = "Milanesa"
print(lista)
# Para acceder a un elemento, debemos utilizar corchetes, y el numero de indice


# Como agregamos o eliminamos elementos?
empleados = ["Carlos", "Ana", "Jorge"]

# Agregamo a Luis
empleados.append("Luis")

print(empleados)

# Eliminamos a Carlos
empleados.remove("Carlos")

print(empleados)
