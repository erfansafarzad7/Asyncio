import asyncio
import functools


def trigger_event(event: asyncio.Event) -> None:
    """
    Sets the event to notify waiting tasks.
    """
    event.set()


async def perform_work_on_event(event: asyncio.Event) -> None:
    """
    Waits for the event to be set, performs work, and then clears the event.
    """
    print('Waiting for the event...')
    await event.wait()  # Wait until the event is set
    print('Performing work...')
    await asyncio.sleep(2)  # Simulate some work
    print('Work is finished.')
    event.clear()  # Clear the event for future use


async def main() -> None:
    """
    Main coroutine that creates an event, schedules it to be triggered after 5 seconds,
    and runs two tasks that wait for the event.
    """
    event = asyncio.Event()  # Create an event

    # Schedule the event to be triggered after 5 seconds
    asyncio.get_running_loop().call_later(5, functools.partial(trigger_event, event))

    # Run two tasks that wait for the event
    await asyncio.gather(perform_work_on_event(event), perform_work_on_event(event))


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
