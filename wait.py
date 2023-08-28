import asyncio
import aiohttp


async def show_status(session, url):
    async with session.get(url) as result:
        return f'status for {url} is {result.status}'


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            asyncio.create_task(show_status(session, 'https://en.wikipedia.org/wiki/Persian')),
            asyncio.create_task(show_status(session, 'https://en.wikipedia.org/wiki/Persian_language')),
        ]
        done, pending = await asyncio.wait(requests, return_when=asyncio.FIRST_COMPLETED)   # ALL_COMPLETED
        print(f'Done --> {done}')
        print(f'Pending --> {pending}')

        for d in done:
            print(await d)

        # FIRST_EXCEPTION
        # for d in done:
        #     if d.exception() is None:
        #         print(d.result())
        #     else:
        #         print('Error..')
        # for p in pending:
        #     p.cancel()
        # print(f' after cancel ')

asyncio.run(main())
