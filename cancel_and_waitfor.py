import asyncio
from asyncio import TimeoutError


async def one():
    await asyncio.sleep(3)  # change sleep second to see result
    print('Hello')


async def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(a, timeout=5)
    except TimeoutError:
        print('deadline reached !')
        print(f'was task cancelled? {a.cancelled()}')


asyncio.run(main())

