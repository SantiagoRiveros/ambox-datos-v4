import time
import numpy as np

""" 
Crear un millon de numeros, y multiplicarlos por 2
"""

# Listas
# Consume mas RAM de la que tengo <- Ocupába 40GB de RAM con mil millones
lista = list(range(1_000_000))

inicio = time.time()

resultado_lista = [x * 2 for x in lista]

fin = time.time()

print("Tiempo con listas:", fin - inicio)

# Arrays
array = np.arange(1_000_000)  # ocupa 7.45 de RAM con mil millones

inicio = time.time()

resultado_array = array * 2

fin = time.time()

print("Tiempo con NumPy:", fin - inicio)

""" 
Tiempo con listas: 0.05485343933105469
Tiempo con NumPy: 0.001994609832763672

Podria hacer aprox 25 arrays en el tiempo que me lleva hacer 1 lista
"""
