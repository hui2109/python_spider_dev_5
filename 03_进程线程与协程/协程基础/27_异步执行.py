import asyncio
import time


async def run1(url):
    print('开始执行协程1')

    # 使用await可以针对耗时操作进行挂起，就与生成器的yield一样，函数交出控制权。协程遇到await，消息循环会挂起该协程，执行别的协程，直到其他协程也会挂起或者执行完毕，再进行下一次执行
    await asyncio.sleep(10)

    print('协程1执行完毕')
    return url


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    t1 = time.time()
    tasks = []

    for i in range(8):
        coroutine = run1(f'baidu.com{i}')
        task = asyncio.ensure_future(coroutine)
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    t2 = time.time()
    print(f"总耗时：{(t2 - t1):.2f}")
