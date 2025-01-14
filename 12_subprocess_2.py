import asyncio


async def main():
    # Create a subprocess and communicate with it
    process = await asyncio.create_subprocess_exec(
        'python', '12_subprocess_1.py',  # Corrected the file name
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Send input to the subprocess and wait for it to complete
    stdout, stderr = await process.communicate(input=b'erfan\n')  # Send input and read output

    # Decode and print the output
    if stdout:
        print(f"stdout: {stdout.decode().strip()}")
    if stderr:
        print(f"stderr: {stderr.decode().strip()}")


if __name__ == "__main__":
    asyncio.run(main())
