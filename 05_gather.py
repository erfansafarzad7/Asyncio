import asyncio
import aiohttp


async def fetch_status(session: aiohttp.ClientSession, url: str) -> int:
    """
    Fetches the HTTP status code of a given URL.
    """
    async with session.get(url) as response:
        return response.status


async def fetch_all_statuses() -> None:
    """
    Fetches the status codes of multiple URLs concurrently and prints the results.
    """
    async with aiohttp.ClientSession() as session:
        # List of URLs to fetch status codes from
        urls = [
            'https://en.wikipedia.org/wiki/Persian',
            'https://en.wikipedia.org/wiki/Persian_language',
            'https://en.wikipedia.org/wiki/Persian_Gulf',
            'https://en.wikipedia.org/wiki/Persian_cat'
        ]

        # Create a list of tasks to fetch status codes concurrently
        tasks = [fetch_status(session, url) for url in urls]

        # Run all tasks concurrently and gather the results
        status_codes = await asyncio.gather(*tasks, return_exceptions=True)

        # Print the status codes
        print(status_codes)


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(fetch_all_statuses())
