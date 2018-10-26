
class Pelicula(object):
    def __init__(self, pnombre, precio):
        self.nombre = pnombre
        self.precio = precio


class CarritoDeCompra(object):
    def __init__(self):
        self.lista_peliculas = None
        self.valor_carrito = None

    def agregar_carrito(self, pelicula):
        self.lista_articulos.append(pelicula)
        self.valor_carrito = self.get_valor_carrito()

    def _get_valor_carrito(self):
        valor = 0
        for objeto in self.lista_peliculas:
            valor = valor + objeto.precio
        return valor


class Cliente(object):
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula


class Factura(object):
    def __init__(self, cliente, carrito, fecha):
        self.cliente = cliente
        self.carrito = carrito
        self.fecha = fecha


carrito = CarritoDeCompra()


def mostrar_menu_principal():
    if carrito.valor_carrito:
        print(f" Valor actual del carrito: {carrito.valor_carrito}")
    print("...Bienvenido al sistema....")
    print("1. Mostrar Peliculas")
    print("2. Buscar Peliculas")
    print("3. Salir")
    opcion = input("Ingrese Opcion: ")


def switch_opcion(opcion):
    return {
        '1': print(""),
        '2': print(""),
        '3': print(""),

    }[opcion]