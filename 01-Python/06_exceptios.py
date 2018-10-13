adrian = {
    "nombre": "andrian",

}


try:
    adrian["apellido"]
except KeyError:  # For keys
    adrian["nombre"]

arregloNumeros = [1, 2]

try:
    arregloNumeros["1"] = 0
except (KeyError, TypeError) as errores:  # For keys
    print(f'Error in {errores}')

except Exception as err:
    print("Error in types")
    print(err.__traceback__)

"""
    print(f"Ocurrio en: {type.__traceback__.tb_frame}")
    print(f"Linea del error: {type.__traceback__.tb_lineno}")
"""