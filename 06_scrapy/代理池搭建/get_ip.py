import asyncio
import random
import ssl
import time

import requests
from lxml import etree

from save_ip import HSaveIp
from settings import *

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


class HGetIp:
    def main(self):
        while True:
            self.redis = HSaveIp()
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.start_get_all_url())

            # 每24小时左右爬取一次
            time.sleep(random.randint(85400, 87400))

    async def start_get_all_url(self):
        tasks = [asyncio.create_task(self.get_all_url_1()), asyncio.create_task(self.get_all_url_2())]
        await asyncio.wait(tasks)

    async def get_all_url_2(self):
        for i in range(1, 6):
            await asyncio.sleep(random.randint(3, 6))

    async def get_all_url_1(self):
        self.flag = 0
        for i in range(1, PAGE_NUMBER + 1):
            ip_url = IP_URL_1 + f'{i}' + '/'
            self.get_one_ip_1(ip_url, i)
            await asyncio.sleep(random.randint(3, 6))

    def get_one_ip_1(self, ip, num):
        # 判断是否为第一页，单独处理headers
        if num == 1:
            headers = {
                'User-Agent': f'{self.redis.set_randmember()}',
                'Referer': IP_URL_1,
                'Host': 'www.kuaidaili.com'
            }
        else:
            headers = {
                'User-Agent': f'{self.redis.set_randmember()}',
                'Referer': IP_URL_1 + f'{num - 1}' + '/',
                'Host': 'www.kuaidaili.com'
            }

        _proxy = self.redis.zset_getip()
        # 最多使用三次代理
        # 如果有_proxy，则构造代理
        # 如果没有_proxy，则设为None
        if _proxy and self.flag < 3:
            proxies = {
                'http': _proxy
            }
            self.flag += 1
        else:
            proxies = None
            self.flag += 1
        try:
            response = requests.get(ip, headers=headers, proxies=proxies)
            content = response.content.decode('utf-8')
            if content:
                # 将使用成功的代理设置为100
                if proxies:
                    print('代理使用成功', proxies)
                    self.redis.zset_zadd(proxies['http'])

                tree = etree.HTML(content)
                trs = tree.xpath('//table/tbody/tr')
                for tr in trs:
                    _ip = tr.xpath('./td[1]/text()')[0]
                    port = tr.xpath('./td[2]/text()')[0]
                    ip = _ip + ':' + port
                    self.redis.zset_zadd(ip)
                    self.flag = 0
        except Exception as e:
            # 最多爬取5次 使用代理爬取3次，不使用代理爬取2次
            if self.flag <= 4:
                print(e, 'ip:', ip, 'proxy', proxies, '本次没有爬取到ip地址')
                self.get_one_ip_1(ip, num)
            else:
                print(e, 'ip:', ip, 'proxy', proxies, '总共5次，均没有爬取到ip地址')


if __name__ == '__main__':
    HGetIp().main()
