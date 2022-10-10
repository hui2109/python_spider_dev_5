import requests
import re

main_url = 'https://www.9meiju.cc/'
movie_url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'

session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

main_response = session.get(main_url)

movie_response = session.get(movie_url)
movie_response_content = movie_response.content.decode('utf-8')

first_m3u8_url = re.search(r'"url":"(.+?\.m3u8)"', movie_response_content).group(1).replace('\\', '').strip()
first_m3u8_response = session.get(first_m3u8_url)
first_m3u8_content = first_m3u8_response.content.decode('utf-8')

second_m3u8_url = 'https://new.qqaku.com' + re.search(r'/.+?\.m3u8', first_m3u8_content).group(0)
second_m3u8_response = session.get(second_m3u8_url)

with open('../00_素材箱/九九电影网/ts文件目录.txt', 'wb') as f:
    f.write(second_m3u8_response.content)
