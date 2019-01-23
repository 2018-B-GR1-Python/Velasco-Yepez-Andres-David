import scrapy
from scrapy.loader import ItemLoader


from mercadolibre.items import CelularItem


def exportar_csv(titulo, precio, link):
    with open('telefonos.csv', 'a') as lista:
            lista.write(f'{titulo},{precio},{link}\n')
            lista.close()


## #comment_js_7me > div > div > div > div:nth-child(2) > div > div > div > div.UFICommentContent > div._26f8 > div > span
class DetallesTelefono(scrapy.Spider):
    name = 'telefonos'

    start_urls = [
        'https://celulares.mercadolibre.com.ec/celulares-smartphones/'
    ]

    def parse(self, response):
        resultados_busqueda = response.css('div.item__info-container.highlighted > div')

        for celular in resultados_busqueda:
            celular_loader = ItemLoader(
                item=CelularItem(),
                selector=celular
            )

            titulo = celular_loader.add_css('titulo', 'h2 > a > span::text')
            precio = celular_loader.add_css('precio', 'div.price__container > div > span.price__fraction::text')
            link = celular_loader.add_css('link', 'h2 > a.item__info-title::attr(href)')
            celular_loader.load_item().get('titulo')
            exportar_csv(
                celular_loader.load_item().get('titulo')[0].replace(',', '-'),
                celular_loader.load_item().get('precio')[0],
                celular_loader.load_item().get('link')[0]
            )
            yield celular_loader.load_item()  # Es un return q no para el loop
