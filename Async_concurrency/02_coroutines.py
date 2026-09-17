import asyncio


async def download_file(filename):

    print(f"Downloading {filename}...")

    await asyncio.sleep(2)

    print(f"{filename} downloaded.")

    return f"{filename} completed"


async def main():

    result = await download_file("file1.txt")

    print(result)


asyncio.run(main())