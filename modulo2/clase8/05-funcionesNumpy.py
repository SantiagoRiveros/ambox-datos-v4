import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Promedio
print(np.mean(array))  # 5.5

# Mediana
# Esto, da el numero "Del medio" si ordenamos el array de menor a mayor
# En este caso, al ser par, no hay un "numero del medio", por ende suma los dos del medio, y los divide
print(np.median(array))  # 5.5

# Desviacion estandar
print(np.std(array))  # 2.8722813232690143
# Mide dispersion, cuanto mas separados los numeros, mas alto es

# Suma acumulada
print(np.cumsum(array))

# Producto acumulado
print(np.cumprod(array))

# Raiz cuadrada
print(np.sqrt(array))

# Potencias
print(np.power(array, 2))

# Logaritmo
print(np.log(array))

# Exponencial
print(np.exp(array))

# Redondeo
# El segundo parametro es cuantos decimales va a conservar
print(np.round(3.14159, 2))

# Valores unicos:
# Te filtra los "repetidos"
print(np.unique([1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 6]))

# Cuenta frecuencia
print(np.bincount([1, 1, 2, 3, 3, 3]))
