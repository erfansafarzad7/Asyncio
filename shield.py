import asyncio
from asyncio import TimeoutError


async def one():
    await asyncio.sleep(3)  # change sleep second to see result
    print('Hello')


async def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(asyncio.shield(a), timeout=5)
    except TimeoutError:
        print('task is taking longer than usual, but we working on it..')
        await a


asyncio.run(main())
