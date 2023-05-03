# 在逆向的过程中. 有可能需要我们在处理cookie的时候. 需要进行手动的urlencode
# 但urlencode没办法帮我们完成一个字符串的处理.
# quote和quote_plus可以帮你完成字符串的处理。在处理cookie的时候【可能会用】。


from urllib.parse import urlencode
from urllib.parse import quote, quote_plus, unquote, unquote_plus

data = {
    'usrname': '&#/?dasas法师法',
    'password': '182ssZ的'
}
# 只能处理字典
r = urlencode(data)
print(r)

# 使用可以处理字符串的quote, quote_plus
s = '我要上天'
print(quote(s))
print(quote_plus(s))

# 将url中%还原的unquote, unquote_plus
url = 'https://www.baidu.com/s?ie=UTF-8&wd=%E6%88%91%E8%A6%81%E4%B8%8A%E5%A4%A9'
print(unquote(url))
print(unquote_plus(url))
