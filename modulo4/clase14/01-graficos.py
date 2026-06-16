import matplotlib.pyplot as plt

ventas = [10, 20, 30, 40, 50]

# Como hacemos nuestro primer grafico?
plt.plot(ventas)  # Este comando, nos arma el grafico

# Aca, lo guardamos con el nombre que le pasamos entre comillas
plt.savefig("primer-grafico.jpg")

plt.show()  # Con esto, lo vemos sin necesidad de guardarlo
# En este caso, no se va a ver, porque sale en una ventana aparte (Y estoy compartiendo Visual Studio nomas)

# QUe pasa si ahora quiero hacer otro grafico?
plt.clf()  # SIEMPRE SIEMPRE SIEMPRE despues de mostrar o guardar un grafico en imagen
# SIEMPRE ejecutamos plt.clf() porque esto borra la memoria temporal de matplotlib
# Para poder ejecutar otro grafico

meses = ["Ene", "Feb", "Mar"]
ventas = [100, 150, 200]

plt.plot(meses, ventas)  # Primero va lo del eje X, luego lo del eje Y
# Vamos a personalizarlo
plt.title("Ventas por mes")  # Esto le da un titulo al grafico
plt.xlabel("Meses")  # Le damos un titulo al eje X
plt.ylabel("Ventas")  # Le damos un titulo al eje Y

plt.savefig("grafico-lineas.jpg")

plt.clf()

# Grafico de barra:
productos = ["Mouse", "Teclado", "Monitor"]
ventas = [50, 35, 25]

plt.bar(productos, ventas)
plt.title("Ventas por producto")
plt.xlabel("Productos")
plt.ylabel("Ventas")
plt.savefig("grafico-barras.jpg")

plt.clf()

# Histograma
edades = [
    20, 21, 22, 23, 24,
    25, 25, 25, 26, 27,
    30, 32, 35, 40
]

plt.hist(edades)
plt.title("Distribucion de edades")
plt.savefig("Histograma.jpg")
plt.clf()

# Scatterplot
horas = [1, 2, 3, 4, 5, 6]
notas = [2, 4, 5, 6, 8, 10]

plt.scatter(horas, notas)
plt.title("Relacion horas vs notas")
plt.xlabel("Horas")
plt.ylabel("Notas")
plt.savefig("scatterplot.jpg")
plt.clf()

# Pie plot (o grafico torta)
categorias = ["Tecnologia", "Ropa", "Alimentos"]
ventas = [50, 30, 20]

plt.pie(ventas, labels=categorias)  # Labels es lo que va a "dividir" la torta
plt.savefig("pieplot.jpg")
