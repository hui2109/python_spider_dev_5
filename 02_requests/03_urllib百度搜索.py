import urllib.request
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?ie=UTF-8&wd=%E8%B7%AF%E9%A3%9E'
# print(urllib.request.unquote(url))

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))