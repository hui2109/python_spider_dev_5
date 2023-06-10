import time

import requests
from hashlib import sha1

ti = str(int(time.time()))
tmp = "last_update_time=" + ti + "&platform=web&roll=gt&type=all"
obj = sha1()
obj.update(tmp.encode('utf-8'))
token = obj.hexdigest()

url = 'https://www.zhitongcaijing.com/immediately/content-list.html'
params = {
    'type': 'all',
    'token': token,
    'last_update_time': ti,
    'platform': 'web'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, params=params, headers=headers)
print(resp.text)
