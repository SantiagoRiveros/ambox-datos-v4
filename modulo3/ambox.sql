# Esto de aca es un comentario, se hace con el simbolo de numeral

# Vamos a crear nuestra Database
CREATE DATABASE empresa;
# sintaxis -> CREATE DATABASE <nombre_de_la_db>
# En SQL todas las consultas deben terminar con ;

# Ahora le indicamos a MySQL workbench que vamos a hacer las consultas en esta DB.
USE empresa;
# sintaxis -> USE <nombre_de_la_db>

# Vamos a crear su primera tabla:
CREATE TABLE empleados(
	id INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);

# INT -> indica el tipo de dato, en SQL debemos indicar TODOS los tipos de datos
# PRIMARY KEY, le indica que va a ser la PK de esta tabla.
# VARCHAR -> Variable Character (Cadena de caracteres de longitud variable)
# (50) -> Cantidad maxima de caracteres que puede contener

# VAmos a insertar datos en empleados
INSERT INTO empleados
VALUES 
(1, "Juan", 25),
(2, "Carlos", 41),
(3, "Carla", 27);

# sintaxis -> INSERT INTO <nombre_de_la_tabla> VALUES (valores a insertar), (valores a insertar...
# El orden importa

# Vamos a leer la tabla empleados
SELECT * FROM empleados;

# * -> Simboliza TODO
# SELECT <columnas o *> FROM <nombre_de_la_tabla>

# Podemos traer tambien las columnas que queramos
SELECT nombre FROM empleados;

# Podemos traer varias columnas
SELECT nombre, edad FROM empleados;

# Con WHERE le damos una condicion 
SELECT * FROM empleados WHERE edad < 40;

# Podemos traer una fila en concreto
SELECT * FROM empleados WHERE id = 3;

# Podemos filtrar
SELECT * FROM empleados WHERE nombre != "Juan" AND edad < 40;

# Podemos usar BETWEEN para indicarle un rango
SELECT * FROM empleados WHERE edad BETWEEN 20 AND 30;

# ORDER BY, para ordenar datos
SELECT * FROM empleados ORDER BY edad; # ASCENDENTE

SELECT * FROM empleados ORDER BY EDAD DESC; # DESCENDENTE

# Limitar candidad de registros que trae
# Por ejemplo 2
SELECT * FROM empleados ORDER BY edad DESC LIMIT 2;

# A modo de ejercicio vamos a crear una tabla productos
CREATE TABLE productos(
	id INT PRIMARY KEY,
    nombre VARCHAR(50),
    categoria VARCHAR(50),
    precio DECIMAL(10,2),
    stock INT
);

INSERT INTO productos 
VALUES
(1, "Mouse", "Perifericos", 15000, 50),
(2, "Teclado", "Perifericos", 25000, 30),
(3, "Monitor", "Monitores", 100000, 10),
(4, "Notebook", "Computadoras", 850000, 5),
(5, "Auriculares", "Audio", 40000, 25);

# Mostrar todos los productos
SELECT * FROM productos;

# Mostrar productos con precio mayor a 30000
SELECT * FROM productos WHERE precio > 30000;

# Mostrar productos con stock menor a 20
SELECT * FROM productos WHERE stock < 20;

# Mostrar productos ordenados por precio descendente
SELECT * FROM productos ORDER BY precio DESC;

# Mostrar los 3 productos mas caros
SELECT * FROM productos ORDER BY precio DESC LIMIT 3;