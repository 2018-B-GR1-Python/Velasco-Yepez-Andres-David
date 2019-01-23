import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from python_04.items import ProductoItem

def truncar_texto(texto):
    return texto[:50]

class DetallesProducto(scrapy.Spider):
    name = 'novicompu'

    start_urls = [
        'https://www.novicompu.com/12-laptops'
    ]

    def parse(self, response):
        resultados_busqueda = response.css('div.product-container > div')
        for producto in resultados_busqueda:
            producto_loader = ItemLoader(
                item=ProductoItem(),
                selector=producto
            )

            producto_loader.default_input_processor = MapCompose(truncar_texto)

            producto_loader.default_output_processor = TakeFirst()

            titulo = producto_loader.add_css('titulo', 'h5 > a.product-name::text')
            precio = producto_loader.add_css('precio', 'span.price.product-price::text')
            link = producto_loader.add_css('link', 'h5 > a.product-name::attr(href)')
            print(titulo, precio, link)


            yield producto_loader.load_item()  # Es un return q no para el loop