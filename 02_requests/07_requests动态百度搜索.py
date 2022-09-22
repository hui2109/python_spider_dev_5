import requests
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?'
key_word = input('请输入您想搜索的内容：')
data_form = {
    'wd': key_word
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(url, params=data_form, headers=headers)
with open('../00_素材箱/requests_baidu.html', 'wb') as f:
    f.write(response.content)
