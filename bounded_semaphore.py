import asyncio


async def show(smp):
    async with smp:
        print('Show method..')
        await asyncio.sleep(2)


async def main():
    smp = asyncio.BoundedSemaphore(2)
    await asyncio.gather(*[show(smp) for _ in range(10)])


asyncio.run(main())
