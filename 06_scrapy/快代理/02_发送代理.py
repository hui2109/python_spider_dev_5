#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

import requests

# 提取代理API接口，获取1个代理IP
api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=oo0cx7cu9gqzdhby4m0d&signature=oij7dvnq7zoiv1ugel3mpj4ddi&num=1&pt=1&sep=1"

# 获取API接口返回的代理IP
proxy_ip = requests.get(api_url).text
print(proxy_ip)


username = "dcp67640128548"
password = "xelv5nal"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
}
print(proxies)

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
#     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
# }
# print(proxies)

# 要访问的目标网页
target_url = "https://dev.kdlapi.com/testproxy"

# 使用代理IP发送请求
response = requests.get(target_url, proxies=proxies)

# 获取页面内容
if response.status_code == 200:
    print(response.content.decode('utf-8'))
