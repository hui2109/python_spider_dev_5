import scrapy
from sele.sel_req import SeleniumRequest


class SeSpider(scrapy.Spider):
    name = 'se'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/web/geek/job?query=python&city=101270100']

    def start_requests(self):
        yield SeleniumRequest(self.start_urls[0])

    def parse(self, response, **kwargs):
        print(response.text)
