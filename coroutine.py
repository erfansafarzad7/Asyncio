import asyncio
from time import perf_counter


async def one(name):
    await asyncio.sleep(2)
    print(f'Hello {name}')


async def main():
    a = asyncio.create_task(one('erfan'))
    b = asyncio.create_task(one('ali'))

    await a
    await b

s = perf_counter()
asyncio.run(main())
print(perf_counter()-s)


    