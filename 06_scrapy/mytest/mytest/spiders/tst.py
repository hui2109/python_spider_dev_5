import scrapy


class TstSpider(scrapy.Spider):
    name = 'tst'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response, **kwargs):
        print(response.text)
