import asyncio
import time
from aiohttp.client_exceptions import ClientError
import aiohttp

from save_ip import HSaveIp


class HTestIp:
    async def test_one_ip(self, ip, signal):
        try:
            async with signal:
                async with aiohttp.ClientSession() as session:
                    # aiohttp模块的proxy参数必须加http://
                    # requests模块的proxies参数可以直接写ip
                    async with session.get('http://httpbin.org/ip', ssl=False, proxy='http://' + ip) as response:
                        content = await response.text(encoding='utf-8')
                        if content:
                            print(ip, '测试成功')
                            self.redis.zset_zadd(ip)
                        else:
                            self.redis.zet_zincrby(ip)
        except Exception as e:
            if not isinstance(e, ClientError):
                print(ip, 'test_one_ip出现错误')
            else:
                self.redis.zet_zincrby(ip)

    async def run(self):
        ips = self.redis.zet_zrange()
        tasks = []
        semaphore = asyncio.Semaphore(100)
        if ips:
            for ip in ips:
                con = self.test_one_ip(ip, semaphore)
                task = asyncio.create_task(con)
                tasks.append(task)
            await asyncio.wait(tasks)

    def main(self):
        self.redis = HSaveIp()
        while True:
            for i in range(3):
                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(self.run())
                except Exception as e:
                    print(e, 'ip测试异步出现错误')
            # 每6小时测试三次
            time.sleep(21600)


if __name__ == '__main__':
    HTestIp().main()
