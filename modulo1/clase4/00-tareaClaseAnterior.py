def mayorNumero(lista):
    mayor = 0
    suma = 0
    for numero in lista:
        if numero > mayor:
            mayor = numero
        if numero % 2 == 0:
            print(numero, "es par")
        else:
            print(numero, "es impar")
        suma += numero
    print("El numero mayor es", mayor)
    promedio = suma / len(lista)
    print("El promedio es ", promedio)


listaNumeros = [2, 4, 1, 8, 9, 3, 2, 5, 11, 31, 22]

mayorNumero(listaNumeros)
