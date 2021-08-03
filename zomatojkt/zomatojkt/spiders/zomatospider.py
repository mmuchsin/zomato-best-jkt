import scrapy
from zomatojkt.items import ZomatojktItem


class ZomatospiderSpider(scrapy.Spider):
    name = 'zomatospider'
    allowed_domains = ['www.zomato.com/']
    start_urls = ['http://https://www.zomato.com/jakarta/best-restaurants?page=']
    
    def start_requests(self, response):
        max_page = response.css('#search-results-container > div.search-pagination-top.clearfix.mtop > div.row > div.col-l-4.mtop.pagination-number > div > b:nth-child(2)::text').get()
        for i in range(1, int(max_page)+1):
            yield scrapy.Request(f'https://www.zomato.com/jakarta/best-restaurants?page={i}', callback=self.parse)

    def parse(self, response):
        data = ZomatojktItem()
        
