import sqlite3

conexion = sqlite3.connect("empresa.db")
# Si la base existe -> Se abre
# Si no existe -> La crea

# Crear un cursor
# ¿Que es un cursor? Permite ejecutar instrucciones SQL

cursor = conexion.cursor()

# Crear una tabla

# LA query la deje en el .txt


# Cuando ya ecutamos un script, lo comentamos seleccionandolo y tocando:
# Alt + Shift + A, para comentarlo, porque la tabla ya se creo

print(conexion)

# gUARDAMOS CAMBIOS:
conexion.commit()
# Todo cambio requiere un commit

# Insertarle datos


# Deje la query en el txt

conexion.commit()

print(cursor.execute("""
SELECT * FROM empleados
                 """))
resultado = cursor.fetchall()
print(resultado)

print("----------")

# Cerramos la conexion
conexion.close()
