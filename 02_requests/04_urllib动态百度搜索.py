import urllib.request
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?ie=UTF-8&wd='
key_word = input('请输入您想搜索的关键词：')
url += urllib.request.quote(key_word)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

# 将获取到到内容写入文件
with open('../00_素材箱/baidu.html', 'wb') as f:
    f.write(response.read())
