from lxml import etree

tree = etree.HTML(open('../00_素材箱/股票.html', 'r', True, 'utf-8').read())

stock_code = tree.xpath('//td[@class="align_center select"]/a/text()')
stock_abbr = tree.xpath('//tbody[@class="tbody_right"]//td[@class="align_center"]/a/text()')
circulation_mv = tree.xpath('//tbody[@class="tbody_right"]//td[@class="align_right "][1]/text()')
total_mv = tree.xpath('//tbody[@class="tbody_right"]//td[@class="align_right "][2]/text()')
circulation_sv = tree.xpath('//tbody[@class="tbody_right"]//td[@class="align_right "][3]/text()')
total_sv = tree.xpath('//tbody[@class="tbody_right"]//td[@class="align_right "][4]/text()')

stock_info = {}
for i in range(len(stock_code)):
    stock_info[stock_code[i]] = [{'简称': stock_abbr[i]},
                                 {'流通市值(万元)': circulation_mv[i]},
                                 {'总市值(万元)': total_mv[i]},
                                 {'流通股本(万元)': circulation_sv[i]},
                                 {'总股本(万元)': total_sv[i]}]
print(stock_info)
