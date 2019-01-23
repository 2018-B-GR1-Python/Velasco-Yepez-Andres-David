import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

from facebook.items import ComentarioItem

## #comment_js_7me > div > div > div > div:nth-child(2) > div > div > div > div.UFICommentContent > div._26f8 > div > span
class DetallesComentario(scrapy.Spider):
    name = 'comentarios'

    start_urls = [
        'https://www.facebook.com/EzPhones-2255760827994179/'
    ]

    def parse(self, response):
        resultados_busqueda = response.css('comment_js_7me > div > div > div > div:nth-child(2) > div > div > div > div.UFICommentContent > div._26f8 > div > span')
        print(resultados_busqueda)
        """
        for comentario in resultados_busqueda:
            comentario_loader = ItemLoader(
                item=ComentarioItem(),
                selector=comentario
            )

            username = comentario_loader.add_css('username', 'h5 > a.product-name::text')
            content = comentario_loader.add_css('content', 'span.price.product-price::text')
            print(username, content)


            yield comentario_loader.load_item()  # Es un return q no para el loop
        """