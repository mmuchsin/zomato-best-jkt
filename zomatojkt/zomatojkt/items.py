# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class ZomatojktItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_proccessor =  MapCompose(remove_tags), output_proccessor = TakeFirst())
    url = scrapy.Field()
    address = scrapy.Field()
    rate = scrapy.Field()
    votes = scrapy.Field()
    location = scrapy.Field()
    rest_type = scrapy.Field()
    cuisines = scrapy.Field()
    approx_cost = scrapy.Field()