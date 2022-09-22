import requests
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com'

response = requests.get(url)
# print(response)   response.text本身是字符串，但是是乱码
# response.encoding='utf-8'
# print(response.text)

# print(response.content)  # response.content本身是子节串
print(response.content.decode('utf-8'))

print('--------------------')

print(response.url)
print(response.status_code)
print(response.request)
print(response.request.headers)
print(response.cookies)
print(response.ok)


