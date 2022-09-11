from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../00_素材箱/股票.html', 'r', True, 'utf-8'), 'lxml')


def stock(stock_info: dict):
    for tr in soup.select('tbody.tbody_right > tr'):
        code = tr.select('td.align_center.select')[0].a.string
        abbr = tr.select('td.align_center')[1].a.string
        [_circulation_mv, _total_mv, _circulation_sv, _total_sv] = tr.select('td.align_right')
        circulation_mv = _circulation_mv.string
        total_mv = _total_mv.string
        circulation_sv = _circulation_sv.string
        total_sv = _total_sv.string
        stock_info[code] = [{'简称': abbr}, {'流通市值(万元)': circulation_mv},
                            {'总市值(万元)': total_mv}, {'流通股本(万元)': circulation_sv},
                            {'总股本(万元)': total_sv}]
    return stock_info


print(stock({}))
