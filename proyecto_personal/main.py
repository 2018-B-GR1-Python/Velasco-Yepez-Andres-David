from proyecto_personal.controllers import *


us=Usuario('juan', 'correo1', '14457645')
Data_Base.usuarios.append(us)
Data_Base.usuarios.append(Factura('08/08/2018',us))


carrito = CarritoDeCompra()

def mostrar_menu_principal():
    while True:
        if len(carrito.lista_peliculas):
            print(f" Valor actual del carrito: {obtener_valor_carrito(carrito)}")
        print("...Bienvenido al sistema....")
        print("1. Mostrar Peliculas")
        print("2. Buscar Peliculas")
        print("3. Salir")
        opcion = input("Ingrese Opcion: ")
        res=switch_opcion(opcion)
        if not res:
            break

def switch_opcion(opcion):
    return {
        '1': mostrar_peliculas_disponibles(),
        '2': buscar_pelicula(input("Ingrese el nombre de la pelicula: ")),
        '3': False,

    }.get(opcion,print("\nIngrese una opcion validad!!"))


mostrar_menu_principal()