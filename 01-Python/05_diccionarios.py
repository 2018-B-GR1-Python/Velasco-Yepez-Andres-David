andres = {
    "nombre": "Andres",
    "apellido": "Velasco",
    "edad": 22,
    "sueldo": 1.01,
    "hijos": [],
    "casado": False,
    "lotera": None,
    "mascota": {
        "nombre": "Cachetes",
        "edad": 3,
    },
}

if andres:
    print("Si")
else:
    print("No")

print(andres['nombre'])
print(andres['mascota']['nombre'])
andres.pop("casado")
print(andres)

# Iterar por valores
for valor in andres.values():
    print(f"Valor: {valor}")

# Iterar por llaves
for llave in andres.keys():
    print(f"Llave: {llave} Valor: {andres[llave]} {andres.get(llave)}")

# Otra forma de iterar el diccionario
for clave, valor in andres.items():
    print(f"clave: {clave} valor: {valor}")

# Agregar un nuevo atributo al diccionario
andres["profesion"] = "Maestro"
andres.update({"peso": 0, "altura": 1})
print(andres)
