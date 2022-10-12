import asyncio

import aiohttp


async def main():
    url = 'https://httpbin.org/get'
    params = {'name': 'lucky', 'age': 18}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, ssl=False) as response:
            # 获取当前请求的url
            print(response.url)
            return await response.text()


print(asyncio.run(main()))
