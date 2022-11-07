import asyncio

import aiohttp

url = 'http://httpbin.org/ip'
# url = 'https://www.kuaidaili.com/free/inha/1/'
proxies = {
    'http': '58.20.184.187:9091'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
proxy = 'http://58.20.184.187:9091'


# aiohttp用不起代理
async def test():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False, proxy=proxy) as response:
            content = await response.text(encoding='utf-8')
            if content:
                print('代理使用成功', proxy)
                print(content)


asyncio.run(test())
