import asyncio
import aiohttp


async def fetch_status_with_delay(session: aiohttp.ClientSession, url: str, delay: int) -> None:
    """
    Fetches the HTTP status code of a given URL after a specified delay.
    """
    await asyncio.sleep(delay)  # Simulate a delay before making the request
    async with session.get(url) as response:
        print(f'Status for {url} is {response.status}')


async def fetch_statuses_in_order_of_completion() -> None:
    """
    Fetches the status codes of multiple URLs concurrently and processes them in the order they complete.
    """
    async with aiohttp.ClientSession() as session:
        # List of tasks with their respective URLs and delays
        tasks = [
            fetch_status_with_delay(session, 'https://en.wikipedia.org/wiki/Persian', 3),
            fetch_status_with_delay(session, 'https://en.wikipedia.org/wiki/Persian_language', 5),
            fetch_status_with_delay(session, 'https://en.wikipedia.org/wiki/Persian_Gulf', 7),
            fetch_status_with_delay(session, 'https://en.wikipedia.org/wiki/Persian_cat', 9),
        ]

        # Process tasks in the order they complete
        for task in asyncio.as_completed(tasks):
            await task


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(fetch_statuses_in_order_of_completion())
