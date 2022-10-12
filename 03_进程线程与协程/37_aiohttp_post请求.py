import asyncio
import aiohttp


async def fetch(session, url):
    async with session.post(url, data='传递数据', ssl=False) as response:
        return await response.text()


async def main():
    url = 'https://httpbin.org/post'
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, url)
        print(source)
        print(type(source))


# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
