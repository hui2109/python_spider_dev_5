import scrapy


class GameSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['4399.com']
    start_urls = ['http://www.4399.com/flash/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="n-game cf"]/li')
        for li in li_list:
            game_name = li.xpath('./a/b/text()').extract_first()
            game_type = li.xpath('./em/a/text()').extract_first()
            game_time = li.xpath('./em[2]/text()').extract_first()
            yield {
                '游戏名': game_name,
                '游戏类型': game_type,
                '游戏时间': game_time,
            }
