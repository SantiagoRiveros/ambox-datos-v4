import pandas as pd

alumnos = pd.DataFrame({
    "id": [1, 2, 3],
    "nombre": ["Ana", "Luis", "Carla"]
})

notas = pd.DataFrame({
    "id": [1, 2, 2, 3],
    "materia": ["Math", "Math", "History", "Math"],
    "nota": [9, 7, 8, 10]
})

""" 
Unir alumnos con notas X
Ver notas promedio por alumno
Ver cuántas materias rindió cada alumno
Identificar mejor alumno
"""
# Unir alumnos con notas
alumnosConNotas = pd.merge(alumnos, notas, on="id")
print(alumnosConNotas)

# Ver notas promedio por alumno
print("Notas promedio")
print(alumnosConNotas.groupby("nombre")["nota"].mean())

# Ver cuantas materias rindio cada alumno
print("Materias por alumno")
print(alumnosConNotas.groupby("nombre")["materia"].count())

# Identificar mejor alumno
print("Mejor alumno")
print(alumnosConNotas.groupby("nombre")["nota"].mean().idxmax(
), alumnosConNotas.groupby("nombre")["nota"].mean().max())
# idxmax te devuelve el indice del que tenga el valor maximo
print(alumnosConNotas.groupby("nombre")["nota"].mean())


# Mostrar rankings de alumnos
print("Ranking de alumnos")
print(alumnosConNotas.groupby("nombre")[
      "nota"].mean().sort_values(ascending=False))
