import asyncio


# counter = 0
#
# async def increment():
#     global counter
#     temp_counter = counter
#     temp_counter += 1
#     await asyncio.sleep(0.01)
#     counter = temp_counter
#
# async def main():
#     global counter
#     tasks = [asyncio.create_task(increment()) for _ in range(100)]
#     await asyncio.gather(*tasks)
#     print(f'Counter is {counter}')
#
# asyncio.run(main())    # --> counter will be 1

# ----------------------------------------------------------------
# to solve this problem:


counter = 0


async def increment(lock):
    global counter
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)
        counter = temp_counter


async def main():
    lock = asyncio.Lock()
    global counter
    tasks = [asyncio.create_task(increment(lock)) for _ in range(100)]
    await asyncio.gather(*tasks)
    print(f'Counter is {counter}')

asyncio.run(main())
