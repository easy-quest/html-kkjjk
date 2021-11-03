from scrapy.spiders import CSVFeedSpider


class CsvspiderSpider(CSVFeedSpider):
    name = 'csvspider'
    allowed_domains = ['kubnews.ru']
    start_urls = ['https://kubnews.ru/proisshestviya/feed.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Сделайте здесь какие-нибудь необходимые адаптации
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        return i
