# https://user.wangxiao.cn/login?url=http%3A%2F%2Fks.wangxiao.cn%2F

import base64
import json

import requests
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

from tu_jian import base64_api


def login():
    # 使用session保持会话
    base_url = 'https://user.wangxiao.cn/login?url=http%3A%2F%2Fks.wangxiao.cn%2F'
    session = requests.Session()
    session.headers[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    session.get(base_url)
    print(session.cookies)

    # 获取时间
    time_url = 'https://user.wangxiao.cn/apis//common/getTime'
    session.headers['Referer'] = 'https://user.wangxiao.cn/login?url=http%3A%2F%2Fks.wangxiao.cn%2F'
    # session.headers['Host'] = 'user.wangxiao.cn' 不要随便加Host！
    session.headers['Content-Type'] = 'application/json;charset=UTF-8'
    time_response = session.post(url=time_url)
    time_data = time_response.json()['data']
    print(time_data)

    # RSA加密
    public_key_str = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'
    public_key = RSA.import_key(base64.b64decode(public_key_str))
    rsa = PKCS1_v1_5.new(public_key)

    ming = f'18-218-2aA@{time_data}'
    ming_bs = ming.encode('utf-8')
    mi_bs = rsa.encrypt(ming_bs)
    mi_str = base64.b64encode(mi_bs).decode()

    # 获取验证码
    captcha_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
    captcha_response = session.post(captcha_url)
    captcha_b64 = captcha_response.json()['data'].split(',')[1]
    imageCaptchaCode = base64_api(b64=captcha_b64)
    print(imageCaptchaCode)

    # 发送请求
    base_url = 'https://user.wangxiao.cn/apis//login/passwordLogin'
    data = {
        'imageCaptchaCode': imageCaptchaCode,
        'password': mi_str,
        'userName': '13688012109'
    }
    response = session.post(url=base_url, json=data)
    login_info = response.json()
    print(login_info)

    return session, response.json()


def getdata(session, res_json):
    # session只能帮我们处理响应头的cookie. 不能处理js动态加载的cookie
    # 需要手动去维护cookie的信息
    session.cookies['autoLogin'] = None
    session.cookies['userInfo'] = json.dumps(res_json['data'])
    session.cookies['token'] = res_json['data']['token']
    session.cookies['UserCookieName'] = res_json['data']['userName']
    session.cookies['OldUsername2'] = res_json['data']['userNameCookies']
    session.cookies['OldUsername'] = res_json['data']['userNameCookies']
    session.cookies['OldPassword'] = res_json['data']['passwordCookies']
    session.cookies['UserCookieName_'] = res_json['data']['userName']
    session.cookies['OldUsername2_'] = res_json['data']['userNameCookies']
    session.cookies['OldUsername_'] = res_json['data']['userNameCookies']
    session.cookies['OldPassword_'] = res_json['data']['userNameCookies']
    session.cookies[res_json['data']['userName'] + "_exam"] = res_json['data']['sign']

    question_url = 'http://ks.wangxiao.cn/practice/listQuestions'
    data = {
        'examPointType': "",
        'practiceType': "2",
        'questionType': "",
        'sign': "jzs1",
        'subsign': "2918984b5c8870f7b257",
        'top': "30"
    }
    data_resp = session.post(url=question_url, json=data)

    return data_resp.text


session, res_json = login()
question = getdata(session, res_json)
print(question)
