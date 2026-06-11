# Hasta ahora veniamos trabajando con una sola tabla
# Ej: -> SELECT * FROM VENTAS

# Pero en bases de datos reales, la informacion esta distribuida en multiples tablas
# Tabla Clientees
# | id | nombre |
# | -- | ------ |
# | 1  | Juan   |
# | 2  | Ana    |

# Tabla Pedidos
#| id | cliente_id | producto |
#| -- | ---------- | -------- |
#| 1  | 1          | Mouse    |
#| 2  | 2          | Monitor  |


# ¿Como mostramos el nombre del cliente junto al pedido?

CREATE TABLE clientes(
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    ciudad VARCHAR(50)
);

INSERT INTO clientes VALUES
(1,'Juan','Buenos Aires'),
(2,'Ana','Cordoba'),
(3,'Pedro','Rosario'),
(4,'Laura','Mendoza'),
(5,'Martin','Salta');

CREATE TABLE pedidos(
    id INT PRIMARY KEY,
    cliente_id INT,
    producto VARCHAR(50),
    cantidad INT,
    precio DECIMAL(10,2)
);

INSERT INTO pedidos VALUES
(1,1,'Mouse',2,15000),
(2,1,'Teclado',1,25000),
(3,2,'Monitor',1,180000),
(4,3,'Auriculares',3,40000),
(5,4,'Notebook',1,850000);
INSERT INTO pedidos VALUES(6, 6, "Pelela", 3, 600);
# Primary Key (PK) -> Es la clave unica e irrepiteble, que nos ayuda a identificar de manera unica una fila

# Foreign Key (FK) -> Apunta a la PK de otra tabla (no necesariamente), sirve para indicar relacion entre tablas.

# JOINS

# ¿Que es un JOIN y porque no deberia tenerle miedo?
# Es una forma de "unir" tablas de manera temporal, dando lugar a lo que se llama "tabla expandida"

SELECT * FROM clientes;
SELECT * FROM pedidos;

# INNER JOIN
# Trae solo las coincidencias entre ambas tablas
SELECT * 
FROM clientes
INNER JOIN pedidos # Aca le estoy indicando con que tabla va a hacer join
ON clientes.id = pedidos.cliente_id; # Aca le decimos con que columna se van a relacionar
# NO ES LO MISMO QUE UNIR TABLAS CON RELACIONES CON FK

# Traeme la tabla de clientes, adicionandole la de pedidos, siempre y cuando haya coincidencia (Esto se evalua fila por fila)

# OUTER JOIN
# TRAE TODO RELACIONANDOLO, AUNQUE NO TENGA COINCIDENCIA
SELECT *
FROM clientes
LEFT JOIN pedidos
ON clientes.id = pedidos.cliente_id

UNION

SELECT *
FROM clientes
RIGHT JOIN pedidos
ON clientes.id = pedidos.cliente_id;


# Se hace con outer JOIN

# LEFT JOIN
# TRAE TODOS LOS REGISTROS DE LA TABLA "IZQUIERDA" AUNQUE NO TENGA COINCIDENCIA
SELECT * FROM 
clientes LEFT JOIN pedidos 
ON clientes.id = pedidos.cliente_id; 

# RIGHT JOIN
# Lo mismo que el left pero al reves
SELECT * FROM 
clientes RIGHT JOIN pedidos 
ON clientes.id = pedidos.cliente_id; 

# Para que usaria right si yo puedo poner en el orden que quiero?
# En vez de hacer lo de arriba
SELECT * FROM 
pedidos LEFT JOIN clientes
ON clientes.id = pedidos.cliente_id; 


# SUBCONSULTAS
# --------------------
# Consulta dentro de consulta
# ¿Cual es el producto mas caro?
SELECT MAX(precio) as precio_maximo FROM productos;

# Ahora yo tengo el precio maximo, pero no el producto con precio maximo, como hago?
SELECT * 
FROM productos 
WHERE precio = 
(SELECT MAX(precio) FROM productos);
# TRaeme todo de productos donde el precio sea igual al precio maximo.

# La subquery se hace DONDE LA NECESITE, ustedes piensen en Python, cuando yo ejecuto una funcion
# esa funcion, igual a que es? Es igual a su retorno

# Producto mas barato
SELECT *
FROM productos
WHERE precio =
(
	SELECT MIN(precio) FROM productos
);

# Productos mas caros que el promedio
SELECT *
FROM productos
WHERE precio >
(
	SELECT AVG(precio) FROM productos
);
# Productos mas baratos que el promedio
SELECT *
FROM productos
WHERE precio <
(
	SELECT AVG(precio) FROM productos
);

# Cliente con mayor facturacion
SELECT
c.nombre, # Ahora vemos que es c
SUM(p.cantidad * p.precio) as total
FROM clientes c # Aca le digo que a clientes lo llame "c"
JOIN productos p
ON c.id = p.cliente_id
GROUP BY c.nombre
ORDER BY total DESC
LIMIT 1; # En este caso no funciona porque no tengo cantidad en productos


# Otra forma de hacer esto, usando subconsulta.
SELECT *
FROM clientes
WHERE id =
(
    SELECT cliente_id
    FROM pedidos
    GROUP BY cliente_id
    ORDER BY SUM(cantidad * precio) DESC
    LIMIT 1
);

# Como traigo cliente con compras?
SELECT *
FROM clientes c
WHERE EXISTS # Verifica existencia
(
    SELECT *
    FROM pedidos p
    WHERE p.cliente_id = c.id
);