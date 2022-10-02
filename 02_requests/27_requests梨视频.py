import requests
import urllib.request as req

session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

url = 'https://video.pearvideo.com/mp4/third/20220627/cont-1766250-15902642-090049-hd.mp4'

response = session.get(url)
print(response)
req.urlretrieve(url, '../00_素材箱/梨视频.mp4')
