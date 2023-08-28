import asyncio
import aiohttp


async def show_status(session, url):
    async with session.get(url) as result:
        return result.status


async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://en.wikipedia.org/wiki/Persian', 'https://en.wikipedia.org/wiki/Persian_language',
                'https://en.wikipedia.org/wiki/Persian_Gulf', 'https://en.wikipedia.org/wiki/Persian_cat']
        rqs = [show_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*rqs, return_exceptions=True)

        print(status_codes)


asyncio.run(main())
