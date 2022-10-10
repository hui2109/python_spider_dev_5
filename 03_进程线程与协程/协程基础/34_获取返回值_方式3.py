import asyncio


async def run(url):
    print('协程', url, '开始抓取')
    await asyncio.sleep(5)
    return url


async def main():
    url_list = ['baidu.com', 'taobao.com', 'aiqiyi.com']
    tasks = []

    for url in url_list:
        coroutine = run(url)
        task = asyncio.create_task(coroutine)
        tasks.append(task)
    done = await asyncio.gather(*tasks)

    print(type(done))
    print(done)
    print('--------------------')

    for result in done:
        print('获取返回值', result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
