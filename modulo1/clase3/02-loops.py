frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)


# Acumuladores

numeros = [10, 20, 30]

suma = 0

for numero in numeros:
    suma = suma + numero

print(suma)


for numero in range(11):
    print(numero)

# range, es para determinar un rango de algo, como si fuera una lista.
# si no le indicamos el numero inicial, va a empezar de 0, y llega hasta el numero anterior al que le indicamos

contador = 0

for numero in range(1, 11):
    contador += numero

print(contador)

# El bucle while, repite mientras se cumple la condicion


condicion = 0

while condicion < 5:
    print(condicion)
    condicion += 1
