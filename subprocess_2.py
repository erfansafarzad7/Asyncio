import asyncio


async def main():
    process = await asyncio.create_subprocess_exec('python', 'subprocess_1.py',
                                                   stdin=asyncio.subprocess.PIPE,
                                                   stdout=asyncio.subprocess.PIPE)

    std_out, std_in = await process.communicate(b'amin')
    print(std_in)
    print(std_out)


asyncio.run(main())
