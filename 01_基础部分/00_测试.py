import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
proxies = {
    'http': '47.93.232.37:80',
}

response = requests.get('http://icanhazip.com/', headers=headers, proxies=proxies)
content = response.content.decode('utf-8')
print(content)
