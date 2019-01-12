import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor


class LinkOnu(CrawlSpider):
    name = 'follow_links_onu_02'
    start_urls = [
        'http://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    # Reglas
    rules = (Rule(LinkExtractor(
                                allow='funds-programmes-specialized-agencies-and-others',
                                deny=('zh/sections', 'fr/sections', 'ru/sections')
                                ), callback='parse_page'),)

    def parse_page(self,response):
        lista_agencias = response.css('div.field-item.even > h4::text').extract()
        for agencia in lista_agencias:
            with open('onu_agencias.txt', 'a+') as archivo:
                archivo.write(agencia+'\n')
                archivo.close()
