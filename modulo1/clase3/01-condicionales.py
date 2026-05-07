usuario = {
    "nombre": "Santiago",
    "apellido": "Riveros",
    "edad": 33,
    "altura": 1.64,
    "intereses": ["Futbol", "Ciclismo"]
}

if usuario["altura"] > 1.65 and usuario["edad"] < 60:
    print("Puede ser guardia de seguridad")
elif usuario["nombre"] == "Santiago":
    print("Santiago puede tener cualquier puesto")
else:
    print("NO puede ser guardia de seguridad")
