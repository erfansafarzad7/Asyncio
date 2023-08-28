import asyncio
import aiohttp


async def show_status(session, url, delay):
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        print(f'status for {url} is {result.status}')


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            show_status(session, 'https://en.wikipedia.org/wiki/Persian', 3),
            show_status(session, 'https://en.wikipedia.org/wiki/Persian_language', 5),
            show_status(session, 'https://en.wikipedia.org/wiki/Persian_Gulf', 7),
            show_status(session, 'https://en.wikipedia.org/wiki/Persian_cat', 9),
        ]

        for rqs in asyncio.as_completed(requests):
            await rqs


asyncio.run(main())
