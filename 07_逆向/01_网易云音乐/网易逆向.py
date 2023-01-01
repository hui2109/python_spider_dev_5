import execjs
import subprocess
from functools import partial
import requests
import urllib.request as urr

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

_data = {
    'csrf_token': "fa77e5120e948330aa6652cdf4ba3702",
    'encodeType': "aac",
    'ids': "[2005574298]",
    'level': "standard"
}
with open('./源代码.js', 'r', True, 'utf-8') as f:
    js_code = execjs.compile(f.read())
    key = js_code.call('getkey', _data)
data = {
    'params': key['encText'],
    'encSecKey': key['encSecKey']
}
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=fa77e5120e948330aa6652cdf4ba3702'
response = requests.post(url, data=data)
song_url = response.json()['data'][0]['url']
urr.urlretrieve(song_url, '../00_resource/2005574298.m4a')
