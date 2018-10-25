#  ------------------------------------------------------------
#  Entidades
#  ------------------------------------------------------------
#  Factura
class Factura(object):

    def __init__(self, usuario, fecha):
        self.usuario = usuario
        self.fecha = fecha


#  Linea de detalle
class Detalle(object):
    def __init__(self, pelicula, factura):
        self.pelicula = pelicula
        self.factura = factura

    def __str__(self):
        return f'{self.pelicula.nombre} {self.pelicula.precio}'


#  Clase del producto del negocio
class Pelicula(object):
    def __init__(self, nombre, precio, genero):
        self.nombre = nombre
        self.precio = nombre
        self.genero = genero


#  Generos de las peliculas
class Genero(object):
    def __init__(self, nombre):
        self.nombre = nombre


# Clase usuario
class Usuario(object):
    def __init__(self, nombre, correo, cedula):
        self.nombre = nombre
        self.correo = correo
        self.cedula = cedula


class CarritoDeCompra(object):
    def __init__(self):
        self.lista_peliculas=None
