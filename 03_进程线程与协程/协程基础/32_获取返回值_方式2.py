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
    done, pending = await asyncio.wait(tasks)

    print(done)
    print('--------------------')
    print(pending)

    for task in done:
        print('获取返回值', task.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
