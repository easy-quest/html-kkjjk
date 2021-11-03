from scrapy.spiders import XMLFeedSpider


class XmlspiderSpider(XMLFeedSpider):
    name = 'xmlspider'
    allowed_domains = ['https://kubnews.ru/proisshestviya/']
    start_urls = ['https://kubnews.ru/proisshestviya//feed.xml']
    iterator = 'iternodes' # вы можете изменить это; см. Документы
    itertag = 'item' # измените его соответствующим образом

    def parse_node(self, response, selector):
        item = {}
        #item['url'] = selector.select('url').get()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()
        return item
