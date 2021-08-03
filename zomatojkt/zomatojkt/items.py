# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZomatojktItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    address = scrapy.Field()
    rate = scrapy.Field()
    votes = scrapy.Field()
    location = scrapy.Field()
    rest_type = scrapy.Field()
    cuisines = scrapy.Field()
    approx_cost  = scrapy.Field()