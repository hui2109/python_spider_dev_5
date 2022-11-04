import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = ['66ip.cn']
    start_urls = ['http://www.66ip.cn/']

    def parse(self, response, **kwargs):
        pass
