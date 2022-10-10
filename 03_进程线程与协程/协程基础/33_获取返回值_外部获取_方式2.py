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
        _task = asyncio.create_task(coroutine)
        tasks.append(_task)
    return await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    done, pending = loop.run_until_complete(main())

    for task in done:
        print('获取返回值', task.result())
