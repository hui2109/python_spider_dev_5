import requests

url = 'http://httpbin.org/ip'
proxies = {
    'http': '223.96.90.216:8085'
}

# response = requests.get(url)
response = requests.get(url, proxies=proxies)
print(response.text)
