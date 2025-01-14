import asyncio


async def wait_and_work(condition: asyncio.Condition) -> None:
    """
    Waits for a condition to be notified, then performs some work.
    """
    async with condition:  # Acquire the condition lock
        print('Lock acquired, waiting for notification...')
        await condition.wait()  # Wait for the condition to be notified
        print('Notification received, starting work...')
        await asyncio.sleep(1)  # Simulate some work
        print('Work finished.')


async def notify_tasks(condition: asyncio.Condition) -> None:
    """
    Notifies all tasks waiting on the condition after a delay.
    """
    await asyncio.sleep(5)  # Simulate a delay before notifying
    async with condition:  # Acquire the condition lock
        print('Notifying all waiting tasks...')
        condition.notify_all()  # Notify all tasks waiting on the condition
    print('Notification process completed.')


async def main() -> None:
    """
    Main coroutine that creates a condition, starts a notifier task,
    and runs two worker tasks that wait for the condition.
    """
    condition = asyncio.Condition()  # Create a condition

    # Start the notifier task
    asyncio.create_task(notify_tasks(condition))

    # Run two worker tasks that wait for the condition
    await asyncio.gather(wait_and_work(condition), wait_and_work(condition))


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
