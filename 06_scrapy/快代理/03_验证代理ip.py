import requests

url = 'https://icanhazip.com/'
proxies = {'http': 'http://dcp67640128548:xelv5nal@113.121.38.202:20445/', 'https': 'http://dcp67640128548:xelv5nal@113.121.38.202:20445/'}
response = requests.get(url, proxies=proxies)
print(response.content.decode('utf-8'))
