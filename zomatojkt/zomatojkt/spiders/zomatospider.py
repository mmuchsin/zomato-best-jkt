import scrapy
from zomatojkt.items import ZomatojktItem
from scrapy.loader import ItemLoader

class ZomatospiderSpider(scrapy.Spider):
    name = 'zomatospider'
    start_urls = ['https://www.zomato.com/jakarta/best-restaurants?page=']

    def parse(self, response):
        for restaurant in response.css('div.card.search-snippet-card.search-card'):
            l = ItemLoader(item=ZomatojktItem(), selector=restaurant)
            
            l.add_css('address','div.col-m-16.search-result-address.grey-text.nowrap.ln22::text')
            l.add_css('branch', 'div.ui.col-l-16.fontsize5.grey-text::text')
            l.add_css('cost', 'span.col-s-11.col-m-12.pl0::text')
            l.add_css('cuisines', 'span.col-s-11.col-m-12.nowrap.pl0>a::text')
            l.add_css('featured_in', 'div.col-s-11.col-m-12.pl0.search-grid-right-text>a::text')
            l.add_css('hours', 'div.col-s-11.col-m-12.pl0.search-grid-right-text::text')
            l.add_css('location','a.ln24.search-page-text.mr10.zblack.search_result_subzone.left>b::text')
            l.add_css('name', 'a.result-title.hover_feedback.zred.bold.ln24.fontsize0::text')
            l.add_css('r_type', 'a.zdark.ttupper.fontsize6::text')
            l.add_css('rate', 'span.rating-value::text')           
            l.add_css('url', 'a.result-title.hover_feedback.zred.bold.ln24.fontsize0::attr(href)')           
            l.add_css('votes', 'span.review-count.medium::text')
                       
            yield l.load_item()
            
            next_page = response.css('a.paginator_item.next.item::attr(href)').get()

            if next_page != None:
                yield response.follow(url=next_page, callback=self.parse)
