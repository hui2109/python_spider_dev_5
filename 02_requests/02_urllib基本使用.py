import urllib.request as urr
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

request = urr.Request("https://www.baidu.com")
response = urr.urlopen(request)

print(response.getcode())
print(response.geturl())
print(response.getheaders())
print(response.read().decode('utf-8'))

urr.urlretrieve("https://www.baidu.com", filename='../00_素材箱/baidu.html')
