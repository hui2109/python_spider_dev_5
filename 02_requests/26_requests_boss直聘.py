import requests

home_url = 'https://www.zhipin.com/chengdu/'
query_url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101270100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=1&pageSize=30'
headers = {
    'referer': 'https://www.zhipin.com/web/geek/job?query=&city=101270100'
}

session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

home_response = session.get(home_url)
query_response = session.get(query_url, headers=headers)
print(query_response.content.decode('utf-8'))
