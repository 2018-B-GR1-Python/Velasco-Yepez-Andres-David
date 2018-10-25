from proyecto_personal.conexionBD import Data_Base
from proyecto_personal.models import *
from functools import *

#  ------------------------------------------------------------
#  Controladores
#  ------------------------------------------------------------




def buscar_pelicula(nombre_pelicula):
    for pelicula in Data_Base.peliculas:
        if pelicula.nombre == nombre_pelicula:
            return pelicula
    return None



def agregar(carrito, pelicula):
    carrito.append(pelicula)


#  Este metodo recibe el carrito de compra y los datos del usuario para realizar la transaccion
def comprar(carrito, **kwargs):
    import datetime
    fecha_actual = datetime.datetime.now()
    factura = Factura(
        fecha=fecha_actual.strftime("%Y-%m-%d %H:%M"),
        usuario=Usuario(kwargs['nombre'], kwargs['correo'], kwargs['cedula'])
    )
    Data_Base.facturas.append(factura)
    for pelicula in carrito:
        Data_Base.detalles.append(factura=factura, pelicula=pelicula)
    lista_detalles = buscar_detalles_factura(factura)
    generar_reporte(factura,lista_detalles)


#  busca los detalles referentes a una factura y devuelve una tupla con los mismos
def buscar_detalles_factura(factura):
    lista_detalles = []
    for detalle in Data_Base.detalles:
        if factura == detalle.factura:
            lista_detalles.append(detalle)
    return lista_detalles


def calcular_total(lista_detalles):
    total = 0
    for detalle in lista_detalles:
        totat = total + detalle.pelicula.precio
        return total


def generar_reporte(factura, lista_detalles):
    reporte = f"Tienda de peliculas\n" f"Fecha: {factura.fecha}\n" f"Propietario: {factura.fecha}\n" f"Fecha {factura.fecha}\n"
    reporte.join('Pelicula                  Precio')
    reporte.join(f'{detalle.pelicula.nombre}                {detalle.pelicula.precio}\n' for detalle in lista_detalles)
    reporte.join(f' Total: {calcular_total(lista_detalles)}')
    return reporte

# Obtiene el precio del carrito de compras
def obtener_valor_carrito(carrito):
    return reduce((lambda x,y:x+y),list(map((lambda x:x.pelicula.precio),carrito.lista_peliculas)))


def mostrar_peliculas_disponibles():
    pass