from hashlib import md5
import requests
import time

url = 'https://dict.youdao.com/webtranslate'
time = int(time.time() * 1000)
obj = md5()
obj.update(f'client=fanyideskweb&mysticTime={time}&product=webfanyi&key=fsdsogkndfokasodnaso'.encode('utf-8'))
sign = obj.hexdigest()
# print(sign)

data = {
    'i': 'take',
    'from': 'auto',
    'to': '',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': str(time),
    'keyfrom': 'fanyi.web'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Referer': 'https://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1547736371.5531156; OUTFOX_SEARCH_USER_ID=-1328728229@218.194.27.203'
}
resp = requests.post(url, data=data, headers=headers)
print(resp.text)
