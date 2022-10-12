import asyncio


async def run1(signal, count):
    async with signal:
        print('开始执行异步函数run1', count)
        await asyncio.sleep(5)
        print('异步函数run1执行完毕', count)


async def run2(count):
    # 没有控制并发
    print('开始执行异步函数run1', count)
    await asyncio.sleep(5)
    print('异步函数run1执行完毕', count)


async def main1():
    semaphore = asyncio.Semaphore(10)
    tasks = []
    for i in range(100):
        con = run1(semaphore, i + 1)
        task = asyncio.create_task(con)
        tasks.append(task)
    await asyncio.wait(tasks)


async def main2():
    # 没有控制并发
    tasks = []
    for i in range(100):
        con = run2(i + 1)
        task = asyncio.create_task(con)
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main1())
    # asyncio.run(main2())
