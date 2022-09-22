import urllib.request
import urllib.parse
import json
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
data_form = {
    'cname': '',
    'pid': '',
    'keyword': '成都',
    'pageIndex': 1,
    'pageSize:': 10
}
data_form = urllib.parse.urlencode(data_form).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, data=data_form, headers=headers)
response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

print(type(json.loads(response.read().decode('utf-8'))))
