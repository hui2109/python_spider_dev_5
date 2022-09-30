import requests
from tu_jian import base64_api

verify_image_url = 'https://so.gushiwen.cn/RandCode.ashx'
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
shelf_url = 'https://so.gushiwen.cn/user/collect.aspx?type=s&id=3461800&sort=t'

data = {
    '__VIEWSTATE': 'lAADdvoxc7IlKPXbEKAgfeK2Rmb/+P+snc+UP3xgX5PLSXJeQ03NOz0gueF/0RkC/+xu7BpiMw3CU+4YuglcVfzwpXwzgpvrXpJaJqzHlMcLwMpeOQOrnjrDZAEZgfQCpv92GyqeK8Kgtb7P1sbnPkBVT8A=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13688012109',
    'pwd': '182182aA',
    'code': None,
    'denglu': '登录'
}

session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

verify_response = session.get(verify_image_url)
with open('../00_素材箱/verify_image.jpg', 'wb') as f:
    f.write(verify_response.content)
result = base64_api('hui2109', '182182aA', '../00_素材箱/verify_image.jpg', 3)
data['code'] = result
print(result)

login_response = session.post(login_url, data=data)

shelf_response = session.get(shelf_url)
with open('../00_素材箱/古诗文书架3.html', 'wb') as f:
    f.write(shelf_response.content)
