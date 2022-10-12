import asyncio
import json

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as response:
        # 将返回的json数据转换为dict对象
        # return await response.json()

        # encoding指定编码格式
        # return await response.text(encoding='utf-8')

        # read()方法返回子节串
        return (await response.read()).decode('utf-8')


async def main():
    url = 'https://httpbin.org/get'
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, url)

        # 也可以手动导入json模块，将返回的json数据转换为dict对象
        source = json.loads(source)

        print(source)
        print(type(source))


asyncio.run(main())
