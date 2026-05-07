# Ejercicio 1: Pedir un numero y decir si es negativo, positivo, o cero

numero = 8

if numero == 0:
    print("El numero es cero")
elif numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")

# Ejericicio 2: Mostrar numero del 1 al 10, usando for

for numero in range(1, 11):
    print(numero)

# Ejericio 3: Mostrar numeros PARES del 1 al 20:

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

# Ejercicio 4: Mostrar la suma de los numeros del 1 al 100, usando un for

suma = 0

for numero in range(1, 101):
    suma += numero

print(suma)

# Ejercicio 5: Crear una funcion que reciba una edad, y diga si es mayor de edad, o no


def esMayorDeEdad(edad):
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")


esMayorDeEdad(19)

# Ejercicio 6: Funcion que calcule el promedio de una lista:


def promedio(lista):
    suma = 0

    for numero in lista:
        suma += numero

    # La palabra return, corta el funcionamiento de una funcion, es decir, "la termina"
    # Ademas, devuelve un valor, es decir lo que va a la derecha del return, "Sale" de la funcion

    # len() devuelve el largo del elemento que tiene adentro de sus parentesis
    return suma / len(lista)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Deberia 5.5 el promedio

print(promedio(lista))
print(len(lista))


""" 
Ejercicio 7:

Crear lista de notas:

mostrar aprobados
mostrar promedio
"""

notas = [3, 7, 8, 1, 5, 6, 9, 2]
# SUpongamos que con 4 aprueba


for nota in notas:
    if nota >= 4:
        print("Aprobado:", nota)

print(promedio(notas))
