import asyncio


async def increment(lock: asyncio.Lock) -> None:
    """
    Increments the global counter safely using a lock to avoid race conditions.
    """
    global counter
    async with lock:  # Acquire the lock to ensure exclusive access
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)  # Simulate some asynchronous work
        counter = temp_counter


async def main() -> None:
    """
    Main coroutine that creates and runs 100 tasks to increment the global counter.
    """
    lock = asyncio.Lock()  # Create a lock to synchronize access to the global counter
    global counter
    # Create 100 tasks to increment the counter
    tasks = [asyncio.create_task(increment(lock)) for _ in range(500)]
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    # Print the final value of the counter
    print(f'Counter is {counter}')


if __name__ == "__main__":
    # Initialize the global counter
    counter = 0
    # Run the main coroutine
    asyncio.run(main())
