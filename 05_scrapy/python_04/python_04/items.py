# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

def shorten_amazon_link(link):
  id_producto = link.split('/')[-1]  # ultimo elemento
  short_link = 'https://www.amazon.com/dp/' + id_producto
  return short_link

class ProductoItem(scrapy.Item):
    titulo = scrapy.Field()
    precio = scrapy.Field()
    link = scrapy.Field(
        input_processor=MapCompose(shorten_amazon_link)
    )
