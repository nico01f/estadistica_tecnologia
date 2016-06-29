# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SueldosItem(scrapy.Item):
    sueldo = scrapy.Field()
    nombre_empresa = scrapy.Field()
    tecnologia = scrapy.Field()
