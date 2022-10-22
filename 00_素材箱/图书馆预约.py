import asyncio
import json
import os

import requests

os.chdir(os.path.dirname(__file__))

if not os.path.exists('./scu_libs.json'):
    with open('./scu_libs.json', 'w', True, 'utf-8') as f:
        json.dump({
            "0": {"2021224020228": "205513"},
            "1": {},
            "2": {},
            "3": {}}, f)
with open('./scu_libs.json', 'r', True, 'utf-8') as f:
    info_dict = json.load(f)

reservation_dict = [
    {'工学馆': 'http://lib.scu.edu.cn:8088/reservation_myaccount/%E5%B7%A5%E5%AD%A6%E9%A6%86'},
    {'江安馆': 'http://lib.scu.edu.cn:8088/reservation_myaccount/%E6%B1%9F%E5%AE%89%E9%A6%86'},
    {'文理馆': 'http://lib.scu.edu.cn:8088/reservation_myaccount/%E6%96%87%E7%90%86%E9%A6%86'},
    {'医学馆': 'http://lib.scu.edu.cn:8088/reservation_myaccount/%E5%8C%BB%E5%AD%A6%E9%A6%86'},
    {'取消预约': 'http://lib.scu.edu.cn:8088/reservation/cancel'}
]

login_url = 'http://lib.scu.edu.cn:8088/student/login?from=reservation'
reservation_url = 'http://lib.scu.edu.cn:8088/reservation'
semaphore = asyncio.Semaphore(10)


async def reserve(loc, username, password, signal=semaphore):
    for i in range(5):
        try:
            async with signal:
                data = {
                    'form_build_id': 'form-s3Nw6PTcMng5_mN0OT8BZvxjPY7_sT55yqyAxG4xgqs',
                    'form_id': 'studentlogin',
                    'academic': username,
                    'passwd': password,
                    'op': '登录'
                }

                session = requests.Session()
                session.headers[
                    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

                session.post(login_url, data=data)
                reservation_response = session.get(reservation_url)
                content = reservation_response.content.decode('utf-8')
                if '你好' in content:
                    if '您已预约' in content:
                        print('您已预约')
                        return None
                    if '您已在馆' in content:
                        print('您已在馆')
                        return None
                    for name, url in reservation_dict[int(loc)].items():
                        session.get(url)
                        print(f'您已成功预约【{name}】')
                    return None
                else:
                    raise Exception()
        except Exception as e:
            print(e)
            print('账号密码错误')


async def run():
    for loc, info in info_dict.items():
        if info != {}:
            for username, password in info.items():
                await reserve(loc, username, password)


if __name__ == '__main__':
    asyncio.run(run())
    # 临时切换分馆
    # asyncio.run(reserve('0', "2021224020229", "252310"))
