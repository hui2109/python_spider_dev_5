import scrapy


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/dongman/']

    def parse(self, response, **kwargs):
        lis = response.xpath('//ul[@class="pic-list2  clearfix"]/li')
        for li in lis:
            _detail_src = li.xpath('./a/@href').extract_first()
            if _detail_src.endswith('.exe'):
                continue

            detail_src = response.urljoin(_detail_src)
            yield scrapy.Request(url=detail_src, callback=self.parse_image)

    def parse_image(self, response, **kwargs):
        image_src = response.xpath('//div[@id="mouscroll"]/img/@src').extract_first()
        print(image_src)
        yield {
            "src": image_src
        }
