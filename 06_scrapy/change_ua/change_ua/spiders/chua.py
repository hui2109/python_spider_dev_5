import scrapy


class ChuaSpider(scrapy.Spider):
    name = 'chua'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response, **kwargs):
        print(response.request.headers)

