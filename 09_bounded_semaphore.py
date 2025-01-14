import asyncio


async def limited_access_task(semaphore: asyncio.BoundedSemaphore) -> None:
    """
    Simulates a task that requires limited concurrent access to a shared resource.
    """
    async with semaphore:  # Acquire the semaphore to limit concurrent access
        print('Task is running...')
        await asyncio.sleep(2)  # Simulate some work
        print('Task is done.')


async def main() -> None:
    """
    Main coroutine that creates and runs 10 tasks with limited concurrent access.
    """
    # Create a BoundedSemaphore to allow a maximum of 2 concurrent tasks
    semaphore = asyncio.BoundedSemaphore(2)

    # Create and run 10 tasks
    await asyncio.gather(*[limited_access_task(semaphore) for _ in range(10)])


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
