# SIEMPRE SIEMPRE SIEMPRE empezar seleccionando la base de datos;
USE empresa;

CREATE TABLE ventas(
	id INT PRIMARY KEY,
    vendedor VARCHAR(50),
    producto VARCHAR(50),
    categoria VARCHAR(50),
	cantidad INT,
    precio DECIMAL(10, 2)
);

INSERT INTO ventas VALUES
(1,'Juan','Mouse','Perifericos',5,15000),
(2,'Juan','Teclado','Perifericos',3,25000),
(3,'Ana','Monitor','Monitores',2,180000),
(4,'Ana','Notebook','Computadoras',1,850000),
(5,'Pedro','Auriculares','Audio',4,40000),
(6,'Pedro','Mouse','Perifericos',8,15000),
(7,'Laura','Monitor','Monitores',3,180000),
(8,'Laura','Notebook','Computadoras',2,850000),
(9,'Juan','Auriculares','Audio',5,40000),
(10,'Ana','Mouse','Perifericos',6,15000);

# COUNT
# Cuenta Registros
SELECT COUNT(*) FROM ventas;

SELECT COUNT(producto) from ventas; # 10 productos vendidos

# Contar vendedores distintos
SELECT COUNT(DISTINCT vendedor) FROM ventas;

# SUM
# Suma valores
SELECT SUM(cantidad) FROM ventas; # Da la cantidad total de productos vendidos

# Cantidad total de dinero en ventas
SELECT SUM(precio) FROM ventas; # El total del precio de las cosas vendidas, pero NO ES EL TOTAL DE DINERO RECAUDADO
# ¿Porque? porque tenemos cantidad por otro lado, entonces hagamos asi ->
SELECT SUM(cantidad * precio) FROM ventas; # 4.170.000 <- este si es el total de dinero recaudado

# AVG
# Devuelve el promedio de la sumatoria de una columna
SELECT AVG(precio) FROM ventas; # precio promedio
# cantidad promedio por venta
SELECT AVG(cantidad) FROM ventas;

# MAX
# Devuelve el mayor valor
# Precio mas alto
SELECT MAX(precio) FROM ventas;

# QUe pasa si queresmo ver la venta mas alta del dataset?
SELECT * FROM ventas WHERE precio * cantidad = (SELECT MAX(precio * cantidad) FROM ventas); # Esto da la compra maxima teniendo en cuenta precio * cantidad

# MIN
SELECT * FROM ventas WHERE precio * cantidad = (SELECT MIN(precio * cantidad) FROM ventas); # Devuelve las compras mas chicas

# GROUP BY
SELECT AVG(precio) FROM ventas; # ¿Que pasa? Me da un promedio general

# Y si quiero un promedio por vendedor?
SELECT vendedor, AVG(precio)
FROM ventas
GROUP BY vendedor 
ORDER BY AVG(precio) DESC;

# Cantidad de ventas por vendedor
SELECT vendedor, COUNT(*)
FROM ventas
GROUP BY vendedor
ORDER BY COUNT(*) DESC;

# Total dinero recaudado por vendedor
SELECT vendedor, SUM(cantidad * precio)
FROM ventas
GROUP BY vendedor
ORDER BY SUM(cantidad * precio) DESC;

# Cantidad de productos por categoria
SELECT categoria, COUNT(*)
FROM ventas
GROUP BY categoria
ORDER BY COUNT(*) DESC;

# FACTURACION POR CATEGORIA
SELECT categoria,
SUM(cantidad * precio) AS total
FROM ventas
GROUP BY categoria;

# having
# Vendedores con mas de 10 unidades vendidas
SELECT vendedor,
SUM(cantidad)
FROM ventas
WHERE SUM(cantidad) > 10
GROUP BY vendedor;

# Porque me da error, en este caso?
# Porque WHERE trabaja antes que group by y se rompe la asociacion
# Para eso existe HAVING

SELECT vendedor,
SUM(cantidad)
FROM ventas
GROUP BY vendedor
HAVING SUM(cantidad) > 10;

# DIFERENCIA CLAVE:
# GROUP BY -> Filtra FIlas
# HAVING -> Filtra Grupos

# Categorias con facturacion mayor a 500.000
SELECT categoria,
SUM(precio * cantidad) AS facturacion
FROM ventas
GROUP BY categoria
HAVING SUM(precio * cantidad) > 500000;

# Vendedores con mas de dos ventas
SELECT vendedor,
COUNT(*) as cantidad_ventas
FROM ventas
GROUP BY vendedor
HAVING COUNT(*) > 2;

# Categorias con promedio superior a 100000
SELECT categoria,
AVG(precio) as precio_promedio
FROM ventas
GROUP BY categoria
HAVING AVG(precio) > 100000
ORDER BY AVG(precio) DESC;
