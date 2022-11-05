import requests

url = 'http://httpbin.org/ip'
proxies = {
    'http': 'http://187.190.252.248:999'
}

response = requests.get(url, proxies=proxies)
print(response.text)
