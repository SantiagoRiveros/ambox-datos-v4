# Una funcion es un bloque de codigo reutilizable

def saludar():
    print("Hola")

# Como ejecutamos la funcion?


saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar()


# Una de las cosas, mas interesantes, de las funciones, que se pueden volver dinamicas

def decidir(numero):
    if numero < 3:
        print("Numero muy bajo")
    elif numero < 5:
        print("Numero promedio")
    elif numero < 8:
        print("Numero alto")
    elif numero < 10:
        print("Numero muy alto")
    else:
        print("Numero fuera de rango")


decidir(7)
