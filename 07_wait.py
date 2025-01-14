import asyncio
import aiohttp


async def fetch_status(session: aiohttp.ClientSession, url: str) -> str:
    """
    Fetches the HTTP status code of a given URL and returns a status message.
    """
    async with session.get(url) as response:
        return f'\n Status for {url} is {response.status}'


async def fetch_statuses_with_wait() -> None:
    """
    Fetches the status codes of multiple URLs concurrently and processes them based on their completion state.
    """
    async with aiohttp.ClientSession() as session:
        # Create tasks for fetching status codes
        tasks = [
            asyncio.create_task(fetch_status(session, 'https://en.wikipedia.org/wiki/Persian')),
            asyncio.create_task(fetch_status(session, 'https://en.wikipedia.org/wiki/Persian_language')),
        ]

        # Wait for tasks to complete, but return when the first task is done
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        # Print the completed and pending tasks
        print(f'\n Done --> {done} \n')
        print(f'\n Pending --> {pending} \n')

        # Process the completed tasks
        for task in done:
            print(await task)

        # Optional: Handle exceptions and cancel pending tasks (commented out)
        # for task in done:
        #     if task.exception() is None:
        #         print(task.result())
        #     else:
        #         print('Error occurred in task..')
        # for task in pending:
        #     task.cancel()
        # print('Pending tasks have been canceled.')


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(fetch_statuses_with_wait())
