from proyecto_personal.controllers import *


us=Usuario('juan', 'correo1', '14457645')
Data_Base.usuarios.append(us)
Data_Base.usuarios.append(Factura('08/08/2018',us))
Data_Base.peliculas.append(Pelicula(nombre='venom',precio=20.5,genero=Genero('accion')))
Data_Base.peliculas.append(Pelicula(nombre='eclipse',precio=10.75,genero=Genero('terror')))
Data_Base.peliculas.append(Pelicula(nombre='enigma',precio=12.58,genero=Genero('comedia')))
Data_Base.peliculas.append(Pelicula(nombre='Star Wars 9',precio=25.58,genero=Genero('drama')))

carrito = CarritoDeCompra()



def mostrar_menu_principal():
    while True:
        if carrito.lista_peliculas:
            print(f" Valor actual del carrito: {obtener_valor_carrito(carrito)}")
        print("...Bienvenido al sistema....")
        print("1. Mostrar Peliculas")
        print("2. Buscar Peliculas")
        print("3. Salir")
        opcion = input("Ingrese Opcion: ")
        switch_opcion(opcion)

def menu_compra():
    while True:
        respuesta = input("Finalizar compra y/n: ")
        if respuesta == 'y' or respuesta == 'Y':
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su email: ")
            cedula = input("Ingrese su cedula: ")
            recibo=comprar(carrito=carrito, nombre=nombre, correo=correo, cedula=cedula)
            print(recibo)
            print("-----------------------------------------------------")
            print("            FACTURA EXPORTADA A UN ARCHIVO           ")
            print("-----------------------------------------------------")
            break
        elif respuesta == 'n' or respuesta == 'n':
            break
        else:
            print("Opcion invalida")


def menu_busqueda():
    pelicula = buscar_pelicula(input("Ingrese nombre pelicula: "))
    if not pelicula:
        print("Pelicula No encontrada!!!")
        return False
    else:
        print("Pelicula encontrada:")
        print(pelicula)
        while True:
            respuesta = input("Agregar al carrito y/n: ")
            if respuesta == 'y' or respuesta == 'Y':
                agregar(carrito,pelicula)
                menu_compra()
                break
            elif respuesta == 'n' or respuesta == 'n':
                break
            else:
                print("Opcion invalida")




def switch_opcion(opcion):
    res= {
        '1': mostrar_peliculas,
        '2': menu_busqueda,
        '3': exit,
    }
    res.get(opcion,lambda: print("Opcion invalida"))()

def mostrar_peliculas():
    print(mostrar_peliculas_disponibles())

mostrar_menu_principal()