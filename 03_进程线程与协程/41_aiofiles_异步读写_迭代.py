import asyncio
import aiofiles


async def main_read():
    async with aiofiles.open('../00_素材箱/异步读写.txt', 'r', 1, 'utf-8') as f:
        async for line in f:
            print(repr(line))


asyncio.run(main_read())
