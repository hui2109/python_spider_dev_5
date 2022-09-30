import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

main_url = 'https://xueqiu.com/'
response = requests.get(main_url, headers=headers)
cookies = response.cookies

url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=401614&size=15'
req = requests.get(url, headers=headers, cookies=cookies)
print(req.json())
