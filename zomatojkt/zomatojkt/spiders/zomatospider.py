import scrapy
from zomatojkt.items import ZomatojktItem


class ZomatospiderSpider(scrapy.Spider):
    name = 'zomatospider'
    allowed_domains = ['www.zomato.com/jakarta/best-restaurants?page=1']
    start_urls = ['http://https://www.zomato.com/jakarta/best-restaurants?page=']

    def parse(self, response):
        pass
