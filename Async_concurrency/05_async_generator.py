import asyncio


async def generate_numbers():

    for number in range(1, 6):

        await asyncio.sleep(1)

        yield number


async def main():
    async for number in generate_numbers():

        print("Received:", number)


asyncio.run(main())