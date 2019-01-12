import scrapy


nombre_archivo = 'book_titles.txt'


def guardar_archivo(titulos, precios, stocks):
    lista_stock = []
    for stock in stocks:
        if 'In stock' in stock:
            lista_stock.append('1')
        else:
            lista_stock.append('0')

    import csv
    with open('libros-e.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        data = list(zip(titulos, precios, lista_stock))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)
    print("Listo :)")


class MiPrimerSpider(scrapy.Spider):
    name = 'intro_spider_e'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titulos = response.css('article > h3 > a::text').extract()
        precios = response.css('article > div > p:nth-child(1)::text').extract()
        stocks = response.css("article > div > p:nth-child(2)::text").extract()
        guardar_archivo(titulos, precios, stocks)