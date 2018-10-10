print("Hola mundo")

edad: int = 20
sueldo = 1.02

print(edad + int(sueldo))
nombre = "Adrian "  # Comentario
apellido = 'Eguez'
apellido_materno = """Sarzosa"""
print(nombre == apellido)  # False
print("{}{} {}".format(nombre, apellido, apellido_materno))
print(int(False))  # 0
print(int(True))  # 1

print(str(False))  # False
print(str(True))  # True
print("andres velasco".capitalize())  # Andres velasco
print("andres velasco".split())  # ["andres","velasco"]
nombre_completo = "andres velasco".split()
print("Vicente".isalpha())  # True
print("Vicente10".isalpha())  # False
print("10".isnumeric())  # True
print("Vicente10".isnumeric())  # False
print("andres10".isalnum())     # True
print("Mi nombre es  {1} {0}".format(nombre_completo[0].capitalize(),nombre_completo[1].capitalize()))
print(f"Mi nombre es  {nombre_completo[0].capitalize()} {nombre_completo[1].capitalize()}")
print(r"Mi nombre es  {nombre_completo[0].capitalize()} {nombre_completo[1].capitalize()}")  # raw
no_existe = None
print(no_existe)
[print(a.capitalize()) for a in "andres velasco".split()]

