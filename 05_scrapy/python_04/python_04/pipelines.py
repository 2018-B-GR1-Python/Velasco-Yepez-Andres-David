# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class ValidarMacbook(object):
    def process_item(self, item, spider):
        if ('lenovo' not in item['titulo'].lower()):

            raise DropItem()

        return item

class ValidarPrecio(object):
    def process_item(self,item,spider):
        print(item['precio'])
        precio = float(item['precio'].replace('$','').replace(',','.'))
        if(precio < 900):
            item['precio'] = 'Muy barato'
            raise DropItem()

        return item


class MarkarComoViable(object):
    def process_item(self, item, spider):
        if item['titulo'] != 'No-Lenovo' and item['precio'] != 'Muy barato':
            print("\n \nItem encontrado")
            print("Titulo", item['titulo'])
            print("Precio", item['precio'])
            print("Link", item['link'])
            print("\n")

        return item










