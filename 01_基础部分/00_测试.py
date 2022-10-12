import asyncio


async def run1():
    print('yes')


async def run2():
    await run1()
    await run3()
    print('another')


def run3():
    print('ert')


asyncio.run(run2())
