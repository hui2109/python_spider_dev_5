# windows下首先应该锁定参数
import os

if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests

song_id = 2041974276
i3x = {
    'csrf_token': "",
    'encodeType': "aac",
    'ids': f"[{song_id}]",
    'level': "standard",
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

with open('逆向代码.js', 'r', True, 'utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
result = js.call('fn', i3x)
# print(type(result))

data = {
    'params': result['encText'],
    'encSecKey': result['encSecKey']
}
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
response = requests.post(url, data=data, headers=headers)
# print(response.json())

song_url = response.json()['data'][0]['url']
if not os.path.exists('../../00_素材箱/网易音乐'):
    os.makedirs('../../00_素材箱/网易音乐')
with open(f'../../00_素材箱/网易音乐/{song_id}.m4a', 'wb', ) as f:
    response = requests.get(song_url, headers=headers)
    f.write(response.content)
