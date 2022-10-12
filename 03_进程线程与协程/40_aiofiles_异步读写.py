import asyncio
import aiofiles


async def main_write():
    async with aiofiles.open('../00_素材箱/异步读写.txt', 'w', 1, 'utf-8') as f1:
        content = await f1.write('你好呀！\n吃饭了么？')
        print(content)  # content代表写入字符的个数


async def main_read():
    async with aiofiles.open('../00_素材箱/异步读写.txt', 'r', 1, 'utf-8') as f2:
        content = await f2.read()
        print(content)  # content代表读取的字符


# asyncio.run(main_write())
asyncio.run(main_read())
