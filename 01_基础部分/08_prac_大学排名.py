from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../00_素材箱/大学排名.html', 'r', True, 'utf-8'), 'lxml')
tbody = soup.select('table.sticky-enabled.tableheader-processed.sticky-table > tbody')[0]
university_info = {}

for tr in tbody.find_all('tr'):
    rank_indoors = tr.find_all('td')[0].string
    rank_world = tr.find_all('td')[1].string
    u_name = tr.find_all('td')[2].string
    university_info[u_name] = [{'国内排名': rank_indoors}, {'世界排名': rank_world}]

print(university_info)

