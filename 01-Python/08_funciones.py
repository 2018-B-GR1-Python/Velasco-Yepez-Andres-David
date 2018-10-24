
def hola_mundo():
    print("Hola mundo")  # Las funciones que no tienen un return devueven None

print(hola_mundo())


def sumar_dos_numeros(num_uno ,num_dos):
    if num_uno == 1:
        return "Hola"
    else:
        return num_uno + num_dos
    return num_uno + num_dos

print(sumar_dos_numeros(1, 2))
print(sumar_dos_numeros(3, 2))

#  Parametro por defecto

def imprimir_universidad(nombre_universidad="EPN"):
    print(f"{nombre_universidad} es lo maximo")


def guardar_carros(posicion,placa,usuario,tip,color):
    print(f"Guardamos en posicion {posicion} el auto con placa {placa}"
          f"del usuario {usuario}")
    if color:
        print(f"El color del carro es {color}")
    if tip:
        print(f"Se recibior un tipo {tip}")

#  Podemos hacer esto para poner los parametros en otro orden
guardar_carros(tip=25.53,
               placa="123-ABC",
               usuario="Andres",
               posicion=1,
               color="Azul")
# Tipos de parametros
# Defecto
# Normales
# *

# Los primeros parametros que se deben escribir en las funciones son los Normales, defecto o los * y luego los defecto

def sumar_numeros(resta,*numeros,valor_inicial=0):
    print(resta)
    print(numeros)
    print(valor_inicial)
    for numero in numeros:
        valor_inicial = valor_inicial + float(numero)
    return valor_inicial

print(sumar_numeros(1, 2, 3, 4, 5, 4, 5, 3, 23, valor_inicial=10))


def imprimir_nombre(*infinito, defecto=1, normal, posicional,**kwargs):  # Key word arguments
    print(f"{kwargs['primer_nombre']} {kwargs['segundo_nombre']}"
          f"{kwargs['apellido_paterno']}"
          f"{kwargs['apellido_materno']}")

imprimir_nombre(1,2,3,4,2,6,7,5,defecto=2,normal=5,posicional=3,
                primer_nombre="Vicente",
                segundo_nombre="Adrian",
                apellido_paterno="Eguez",
                apellido_materno="Sarzosa")

# Siempre devuelve un string
"""
numero = input("Ingrese un numero: ")
print(float(numero) + 12.2 + 1)
opcional = input("Desea papas con su orden, Opc:Si Opc:No")

print("Truthy" if opcional == "Si" else "False")

if True if opcional == "Si" else False:
    print("Truthy")
else:
    print("False")
"""

# Proceso
# Recibir numeros separados por comas y usar un split
# 1)  Recibir numeros  Valdar que sean numeros y que esten separados por comas
#        1.1) Separar por comas
#        1.2) Sean numeros
# 2)  Convertir la tupla en Float
# 3) Ejecutar la funcion

"""
numeros=input("Ingrese_numeros:")
lnumeros = numeros.split(",")

print(sumar_numeros(0, valor_inicial=0, *numeros))
"""

def calculadora(numero_uno, numero_dos, operacion):
    def sum_dos_numeros():
        return numero_uno + numero_dos
    def restar_dos_numeros():
        return numero_uno + numero_dos

    def multiplicar_dos_numeros():
        return numero_uno * numero_dos

    def dividir_dos_numeros():
        return numero_uno / numero_dos

    # Implementacion de un switch
    def switch_operaciones():
        return {
            'suma': sum_dos_numeros(),
            'resta': restar_dos_numeros(),
            'multiplicacion': multiplicar_dos_numeros(),
            'division': dividir_dos_numeros()
        }[operacion]
    # Retorna el llamado de la funcion
    return switch_operaciones()


## Registrar clases
## Registrar estudiantes / eliminar clases / buscar clases
## CRUD

print(calculadora(1, 2, operacion="suma"))
print(calculadora(1, 12, operacion="resta"))
print(calculadora(2, 20, operacion="multiplicacion"))
print(calculadora(3, 5, operacion="division"))

def leer_archivo(path):
    try:
        archivo_abierto = open(path)  # Defecto es 'r'
        arreglo_de_lineas = archivo_abierto.readlines()  # Devuelve un arreglo de lineas
        # Readline devuelve un solo caracter
        for linea in arreglo_de_lineas:
            print(linea)
        archivo_abierto.close()
    except Exception:
        print("No se pudo leer el archivo")


def agregar_a_archivo(path, *lineas_escribir):
    try:
        archivo_abierto = open(path,'a')  # Defecto es 'r'
        for linea in lineas_escribir:
            archivo_abierto.write(linea)
        archivo_abierto.close()
    except Exception:
        print("No se pudo leer el archivo")

leer_archivo('./08_ejemplo.txt')
agregar_a_archivo('./08_ejemplo.txt', 'Hola esta', 'es una', 'prueba')
leer_archivo('./08_ejemplo.txt')


elevar_al_cuadrado = lambda n: n * n
sumar_dos_numeros_v2 = lambda x,y: x + y

print(elevar_al_cuadrado(4))
print(sumar_dos_numeros_v2(2,4))