from proyecto_personal.conexionBD import Data_Base
from proyecto_personal.models import *
from functools import *

#  ------------------------------------------------------------
#  Controladores
#  ------------------------------------------------------------

def buscar_peliculav2(nombre_pelicula):
    return list(filter(lambda x:x==nombre_pelicula,list(map(lambda x:x.nombre,Data_Base.peliculas))))

def buscar_pelicula(nombre_pelicula):
    for pelicula in Data_Base.peliculas:
        if pelicula.nombre == nombre_pelicula:
            return pelicula
    return None

# Agrega una pelicula al carrito de compra
def agregar(carrito, pelicula):
    carrito.lista_peliculas.append(pelicula)


#  Este metodo recibe el carrito de compra y los datos del usuario para realizar la transaccion
def comprar(carrito, **kwargs):
    import datetime
    fecha_actual = datetime.datetime.now()
    factura = Factura(
        fecha=fecha_actual.strftime("%Y-%m-%d %H:%M"),
        usuario=Usuario(kwargs['nombre'], kwargs['correo'], kwargs['cedula'])
    )
    Data_Base.facturas.append(factura)
    for pelicula in carrito.lista_peliculas:
        Data_Base.detalles.append(Detalle(factura=factura, pelicula=pelicula))
    lista_detalles = buscar_detalles_factura(factura)
    carrito.lista_peliculas=[]
    return generar_reporte(factura,lista_detalles)


#  busca los detalles referentes a una factura y devuelve una tupla con los mismos
def buscar_detalles_factura(factura):
    lista_detalles = []
    for detalle in Data_Base.detalles:
        if factura == detalle.factura:
            lista_detalles.append(detalle)
    return lista_detalles

# Calcula el precio total de las peliculas
def calcular_total(lista_detalles):
    return reduce((lambda x,y:x.pelicula.precio+y.pelicula.precio),lista_detalles)

# Genera la descripcion de la factura y la guarda en un archivo
def generar_reporte(factura, lista_detalles):
    reporte = f"--------Tienda de peliculas--------\n" \
              f"Fecha: {factura.fecha}\n" f"Propietario: {factura.usuario}\n"
    reporte=reporte+''.join(f'{detalle.pelicula.nombre}    {detalle.pelicula.precio}\n' for detalle in lista_detalles)
    reporte=reporte+f'Total: {calcular_total(lista_detalles)}'
    exportar_factura_archivo(f"./facturas_generadas/factura{factura.usuario.cedula}.txt",reporte)
    return reporte

# Obtiene el precio del carrito de compras
def obtener_valor_carrito(carrito):
    return reduce((lambda x,y:x+y),list(map((lambda x:x.precio),carrito.lista_peliculas)))

# Retorna las peliculas disponibles en la BD
def mostrar_peliculas_disponibles():
    return ''.join( str(pelicula) for pelicula in Data_Base.peliculas)

# Exporta una factura y sus detalles a un archivo
def exportar_factura_archivo(path, datos):
    try:
        archivo_abierto = open(path,'w+')  # Defecto es 'r'
        archivo_abierto.write(datos)
        archivo_abierto.close()
    except Exception:
        print("No se pudo leer el archivo")