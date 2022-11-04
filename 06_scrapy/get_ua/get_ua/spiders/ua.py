import scrapy


class UaSpider(scrapy.Spider):
    name = 'ua'
    allowed_domains = ['useragentstring.com']
    start_urls = ['https://useragentstring.com/pages/Chrome/']

    def parse(self, response, **kwargs):
        uas = response.xpath('//div[@id="liste"]/ul/li/a')
        for ua in uas:
            user_agent = ua.xpath('./text()').extract_first()

            # 这个地方必须yield，不然不会进pipline
            yield {'User-Agent': user_agent}
