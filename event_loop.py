import asyncio


async def one(name):
    await asyncio.sleep(2)
    print(f'Hello {name}')


async def main():
    a = asyncio.create_task(one('erfan'))
    b = asyncio.create_task(one('ali'))

    await a
    await b

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
