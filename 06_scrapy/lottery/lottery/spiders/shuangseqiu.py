import scrapy


class ShuangseqiuSpider(scrapy.Spider):
    name = 'shuangseqiu'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://match.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs']

    def parse(self, response, **kwargs):
        trs = response.xpath('//tbody[@id="cpdata"]/tr')
        for tr in trs:
            issue = tr.xpath('./td[1]/text()').extract_first()

            if not issue:
                continue

            red_nums = tr.xpath('./td[@class="chartball01"]/text() | ./td[@class="chartball20"]/text()').extract()
            blue_num = tr.xpath('./td[@class="chartball02"]/text()').extract_first()
            sum_value = tr.xpath('./td[last()-3]/text()').extract_first()
            span = tr.xpath('./td[last()-2]/text()').extract_first()
            ratio = tr.xpath('./td[last()-1]/text() | ./td[last()-1]/div/text()').extract_first()
            odd = tr.xpath('./td[last()]/text() | ./td[last()]/div/text()').extract_first()
            yield {
                'issue': issue,
                'red_nums': red_nums,
                'blue_num': blue_num,
                'sum_value': sum_value,
                'span': span,
                'ratio': ratio,
                'odd': odd
            }
