import asyncio
from time import perf_counter


async def say_hello(name: str) -> None:
    """
    Simulates an asynchronous task that takes 2 seconds to complete.
    """
    print('Starting Tasks...')
    await asyncio.sleep(2)  # Simulate a task that takes 2 seconds
    print(f'Hello {name}')


async def main() -> None:
    """
    Main coroutine that creates and runs two tasks concurrently.
    """
    task_erfan = asyncio.create_task(say_hello('erfan'))
    task_ali = asyncio.create_task(say_hello('ali'))

    # Wait for both tasks to complete
    await task_erfan
    await task_ali


if __name__ == "__main__":
    # Measure the execution time of the main coroutine
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()

    # Print the total execution time
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
