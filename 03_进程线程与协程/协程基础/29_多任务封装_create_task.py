import asyncio


async def run(url):
    print('协程', url, '开始抓取')
    await asyncio.sleep(5)
    return url


def call_back(future):
    print('返回值', future.result())


async def main():
    url_list = ['baidu.com', 'taobao.com', 'aiqiyi.com']
    tasks = []

    for url in url_list:
        coroutine = run(url)
        task = loop.create_task(coroutine)
        task.add_done_callback(call_back)
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
