import requests

login_url = 'https://passport.17k.com/ck/user/login'
book_shelf_url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
data = {
    'loginName': '13688012109',
    'password': '182182aA'
}

session = requests.Session()
login_response = session.post(login_url, data=data, headers=headers)

shelf_response = session.get(book_shelf_url, headers=headers)
print(shelf_response.json())
