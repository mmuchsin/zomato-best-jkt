# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

class ZomatojktItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    branch = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    cost = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    cuisines = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    featured_in = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    hours = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    location = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    name = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    rate = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    r_type = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    url = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    votes = scrapy.Field(input_proccessor=MapCompose(remove_tags), output_proccessor=TakeFirst())
    