import scrapy
from zomatojkt.items import ZomatojktItem


class ZomatospiderSpider(scrapy.Spider):
    name = 'zomatospider'
    allowed_domains = ['www.zomato.com/']
    start_urls = ['https://www.zomato.com/jakarta/best-restaurants?page=']
    
    # def start_requests(self, response):
    #     max_page = response.css('#search-results-container > div.search-pagination-top.clearfix.mtop > div.row > div.col-l-4.mtop.pagination-number > div > b:nth-child(2)::text').get()
    #     for i in range(1, int(max_page)+1):
    #         yield scrapy.Request(f'https://www.zomato.com/jakarta/best-restaurants?page={i}', callback=self.parse)

    def parse(self, response):
        data = ZomatojktItem()
        list_restaurant = response.css('div.card.search-snippet-card.search-card')
        
        for i in range(len(list_restaurant)):
            name = response.css('a.result-title.hover_feedback.zred.bold.ln24.fontsize0::text')
            url = response.css('a.result-title.hover_feedback.zred.bold.ln24.fontsize0::attr(href)')
            address = response.css('div.col-m-16.search-result-address.grey-text.nowrap.ln22::text')
            rate = response.css('span.rating-value::text')
            votes = response.css('span.review-count.medium::text')
            location = response.css(f'#orig-search-list > div:nth-child({i+1}) > div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.ln24.search-page-text.mr10.zblack.search_result_subzone.left > b::text')
            rest_type1 = response.css('#orig-search-list > div > div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.res-snippet-small-establishment.mt5 > a:nth-child(1)::text')
            rest_type2 = response.css('#orig-search-list > div > div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.res-snippet-small-establishment.mt5 > a:nth-child(3)::text')
            cuisine1 = response.css(f'#orig-search-list > div:nth-child({i+1}) > div.content > div > article > div.search-page-text.clearfix.row > div:nth-child(1) > span.col-s-11.col-m-12.nowrap.pl0 > a:nth-child(1)::text')
            cuisine2 = response.css(f'#orig-search-list > div:nth-child({i+1}) > div.content > div > article > div.search-page-text.clearfix.row > div:nth-child(1) > span.col-s-11.col-m-12.nowrap.pl0 > a:nth-child(2)::text')
            approx_cost = response.css(f'#orig-search-list > div > div.content > div > article > div.search-page-text.clearfix.row > div.res-cost.clearfix > span.col-s-11.col-m-12.pl0::text')
            
            data['url'] = url[i].get()
            data['name'] = name[i].get()
            data['address'] = address[i].get()
            data['rate'] = rate[i].get()
            data['votes'] = votes[i].get()
            data['location'] = location.get()
            data['rest_type'] = f'{rest_type1[i].get()}, {rest_type2[i].get()}'
            data['cuisines'] = f'{cuisine1.get()}, {cuisine2.get()}'
            data['approx_cost'] = approx_cost[i].get()
            
            yield data