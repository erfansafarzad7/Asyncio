import asyncio


async def greet_after_delay(name: str) -> None:
    """
    Simulates an asynchronous task that prints a greeting after a delay.
    """
    await asyncio.sleep(2)  # Simulate a task that takes 2 seconds
    print(f'Hello {name}')


async def run_concurrent_tasks() -> None:
    """
    Main coroutine that creates and runs two tasks concurrently.
    """
    # Create two tasks to run concurrently
    task_erfan = asyncio.create_task(greet_after_delay('erfan'))
    task_ali = asyncio.create_task(greet_after_delay('ali'))

    # Wait for both tasks to complete
    await task_erfan
    await task_ali


if __name__ == "__main__":
    # Create a new event loop
    event_loop = asyncio.new_event_loop()

    try:
        # Run the main coroutine until it completes
        event_loop.run_until_complete(run_concurrent_tasks())
    finally:
        # Close the event loop
        event_loop.close()
