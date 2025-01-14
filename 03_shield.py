import asyncio
from asyncio import TimeoutError


async def greet_after_delay() -> None:
    """
    Simulates an asynchronous task that prints a greeting after a delay.
    """
    await asyncio.sleep(7)  # Simulate a task that takes 3 seconds
    print('Hello World!')


async def run_with_shield() -> None:
    """
    Main coroutine that runs the `greet_after_delay` task with a timeout.
    If the task exceeds the timeout, it is shielded from cancellation and continues running.
    """
    # Create a task for the `greet_after_delay` coroutine
    greeting_task = asyncio.create_task(greet_after_delay())

    try:
        # Wait for the task to complete, but timeout after 5 seconds
        # Use `asyncio.shield` to protect the task from cancellation
        await asyncio.wait_for(asyncio.shield(greeting_task), timeout=5)
    except TimeoutError:
        # Handle the timeout case
        print('Task is taking longer than usual, but we are working on it...')
        # Wait for the shielded task to complete
        await greeting_task


if __name__ == "__main__":
    asyncio.run(run_with_shield())
