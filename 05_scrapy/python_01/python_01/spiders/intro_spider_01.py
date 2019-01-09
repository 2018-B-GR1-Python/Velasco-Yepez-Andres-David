import scrapy


nombre_archivo = 'book_titles.txt'


class MiPrimerSpider(scrapy.Spider):
    name = 'intro_spider'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       #print(response.css('li.col-xs-6:nth-child(1) > article:nth-child(1) > h3:nth-child(3) > a:nth-child(1)').extract())
       #print(response.xpath('/html/body/div/div/div/div/section/div/ol/li/article/h3/a/text()').extract())
       #print(response.xpath("//article/h3/a/text()").extract())
        titulos = response.css('article > h3 > a::text').extract()
        precios = response.css('article > div > p:nth-child(1)::text').extract()
        stocks = response.xpath("/html/body/div/div/div/div/section/div/ol/li/article/div/p[@class='instock availability']/text()").extract()
        self.guardar_archivo(titulos,precios,stocks)

    def guardar_archivo(self,titulos,precios,stocks):
        lista_stock = []
        for stock in stocks:
            if 'In stock' in stock:
                lista_stock.append('1')
            else:
                lista_stock.append('0')

        import csv
        with open('libros.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

            data = list(zip(titulos, precios, lista_stock))
            for row in data:
                row = list(row)
                spamwriter.writerow(row)
        print("Listo :)")