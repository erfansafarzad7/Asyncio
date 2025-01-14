import asyncio
from asyncio import TimeoutError


async def greet_after_delay(delay: int) -> None:
    """
    Simulates an asynchronous task that prints a greeting after a specified delay.
    """
    await asyncio.sleep(delay)  # Simulate a task that takes `delay` seconds
    print('Hello')


async def run_with_timeout() -> None:
    """
    Main coroutine that runs the `greet_after_delay` task with a timeout.
    If the task exceeds the timeout, a TimeoutError is caught and handled.
    """
    # Create a task for the `greet_after_delay` coroutine
    greeting_task = asyncio.create_task(greet_after_delay(6))  # <===== Change delay to see different results

    try:
        # Wait for the task to complete, but timeout after 5 seconds
        await asyncio.wait_for(greeting_task, timeout=5)
    except TimeoutError:
        # Handle the timeout case
        print('Deadline reached!')
        print(f'Was the task cancelled? {greeting_task.cancelled()}')


if __name__ == "__main__":
    asyncio.run(run_with_timeout())
