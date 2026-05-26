import numpy as np

""" 
Crear array:

números del 1 al 20
mostrar promedio
mostrar máximo
multiplicar por 5
"""

array = np.arange(1, 21)
print(array)

# Mostramos promedio
print("Promedio:", array.mean())

# Mostramos maximo
print("Maximo:", array.max())

# Multiplicamos por 5
print("Multiplicado por 5:")
print(array * 5)

# Ejercicio 2:
# Crear array del 1 al 50, y que "salten" los numeros cada 2
arrayConSalto = np.arange(1, 51, 2)  # El tercer parametro es el "salto"
# Si vos le metes solo 2 argumentos, el primero es el inicio, el segundo el fin
# Si vos le metes 3,  el tercero es el "salto" numerico, si no se lo aclaras, el salto es cada 1
print(arrayConSalto)

# Linspace
# Genera numeros de manera uniforma entre el principio y el fin
arrayConLinspace = np.linspace(0, 1, 5)
print(arrayConLinspace)
# Diferencia con arange, es que vos con linspace le decis cuantos numeros queres, pero no el salto en si

arrayConZeros = np.zeros(5)
print(arrayConZeros)

""" 
¿Para que sirve?
-Inicializar Array
-Reservar en memoria
-etc
"""

# Ones
arrayConOnes = np.ones(5)
print(arrayConOnes)

# randint
# Genera numeros aleatorios en el rango que le indicamos y la cantidad que le indicamos
# radint(principio, fin, cantidad)
arrayConRandoms = np.random.randint(1, 100, 25)
print(arrayConRandoms)
