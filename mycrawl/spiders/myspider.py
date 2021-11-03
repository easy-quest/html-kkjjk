import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Все новости и события Краснодара и Краснодарского края | Кубанские новости
# https://kubnews.ru/all/?type=news
# https://kubnews.ru/proisshestviya/?PAGEN_1=2


class LinkspiderSpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['http://sipwhiskey.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'collections/japanese-whisky/', deny='products')),
        Rule(LinkExtractor(allow=r'products/'), callback='parse_item')
    )
        # Rule(LinkExtractor(allow=r'PAGEN_1='), callback='parse_item', follow=True)}

def parse_item(self, response):
    yield {
            'vendor': response.css('div.vendor a::text').get(),
            'name': response.css('h1.title::text').get(),
            'price': response.css('span.price::text').get()
    }