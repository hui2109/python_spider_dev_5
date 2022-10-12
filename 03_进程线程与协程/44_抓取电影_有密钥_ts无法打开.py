import asyncio
import os
import re
import time

import aiofiles
import aiohttp


class MyCaptureMovie:
    def __init__(self, first_m3u8_url):
        self.first_m3u8_url = first_m3u8_url

    def get_started(self):
        # 如果本地文件不存在，就调用以下函数创建本地文件
        if not os.path.exists('../00_素材箱/电影网/3_有密钥_ts打不开/index.m3u8'):
            print('true')
            asyncio.run(self.get_second_m3u8_url())
            asyncio.run(self.get_movie_url())
        asyncio.run(self.download_all_video())

    async def get_second_m3u8_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(self.first_m3u8_url, ssl=False) as response:
                content = await response.text(encoding='utf-8')
                self.second_m3u8_url = 'https://s7.fsvod1.com' + re.search(r'/.+?\.m3u8', content).group(0)

    async def get_movie_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(self.second_m3u8_url, ssl=False) as response:
                content = await response.text(encoding='utf-8')
                async with aiofiles.open('../00_素材箱/电影网/3_有密钥_ts打不开/index.m3u8', 'w', 1, 'utf-8') as f:
                    await f.write(content)

    async def download_all_video(self):
        t1 = time.time()
        semaphore = asyncio.Semaphore(50)
        with open('../00_素材箱/电影网/3_有密钥_ts打不开/index.m3u8', 'r', True, 'utf-8') as f:
            count = 0
            tasks = []
            for line in f:
                if not line.startswith('#'):
                    count += 1
                    ts_url = 'https://s7.fsvod1.com' + line.strip()
                    tasks.append(asyncio.create_task(self.download_one_video(ts_url, count, semaphore)))
        await asyncio.wait(tasks)
        print(time.time() - t1)

    # 使用retry，文件下载不全
    # @retry(stop_max_attempt_number=3)
    async def download_one_video(self, ts_url, count, signal):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        for c in range(3):
            try:
                async with signal:
                    print(f'开始下载第{count}个ts文件')
                    async with aiohttp.ClientSession(headers=headers) as session:
                        async with session.get(ts_url, ssl=False) as response:
                            content = await response.read()
                            async with aiofiles.open(f'../00_素材箱/电影网/3_有密钥_ts打不开/{count}.ts', 'wb') as f:
                                await f.write(content)
                            print(f'第{count}个ts文件下载完毕！')
                            return None
            except BaseException as e:
                print(e)
                print(f'第{count}个ts文件的第{c + 1}次下载失败，正在重新下载！')

    def modify_index_file(self):
        index = 1
        with open('../00_素材箱/电影网/3_有密钥_ts打不开/index.m3u8', 'r', True, 'utf-8') as f1:
            with open('../00_素材箱/电影网/3_有密钥_ts打不开/index_modify.m3u8', 'w', True, 'utf-8') as f2:
                for line in f1:
                    if line.startswith('/'):
                        f2.write(
                            f'/Users/hui99563/Documents/01_编程学习/python/09_爬虫开发第5期/00_素材箱/电影网/3_有密钥_ts打不开/{index}.ts\n')
                        index += 1
                    else:
                        f2.write(line)

    async def get_key_file(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

        f1 = open('../00_素材箱/电影网/3_有密钥_ts打不开/index_modify.m3u8', 'r', True, 'utf-8')
        f3 = open('../00_素材箱/电影网/3_有密钥_ts打不开/index_modify_key.m3u8', 'w', True, 'utf-8')
        for line in f1:
            if line.startswith('#EXT-X-KEY'):
                match_item = re.search(r'URI="(.+?)"', line).group(0)
                key_url = 'https://s7.fsvod1.com' + re.search(r'URI="(.+?)"', line).group(1)
                async with aiohttp.ClientSession(headers=headers) as session:
                    async with session.get(key_url, ssl=False) as response:
                        content = await response.read()
                        async with aiofiles.open(f'../00_素材箱/电影网/3_有密钥_ts打不开/key.m3u8', 'wb') as f2:
                            await f2.write(content)
                new_line = line.replace(match_item,
                                        'URI="/Users/hui99563/Documents/01_编程学习/python/09_爬虫开发第5期/00_素材箱/电影网/3_有密钥_ts打不开/key.m3u8"')
                print(new_line)
                f3.write(new_line)
            else:
                f3.write(line)
        f3.flush()
        f1.close()
        f3.close()

    def merge(self, filename='movie'):
        os.chdir('../00_素材箱/电影网/3_有密钥_ts打不开')
        cmd = f'ffmpeg -i index_modify_key.m3u8 -c copy {filename}.mp4'
        os.system(cmd)


if __name__ == '__main__':
    first_m3u8_url = 'https://s7.fsvod1.com/20220622/5LnZiDXn/index.m3u8'
    mcm = MyCaptureMovie(first_m3u8_url)
    # mcm.get_started()
    # mcm.modify_index_file()
    # asyncio.run(mcm.get_key_file())
    mcm.merge()
