import asyncio
import time


async def task(name, delay):

    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} finished")

    return f"{name} result"


async def main():

    start = time.perf_counter()

    results = await asyncio.gather(
        task("Task 1", 3),
        task("Task 2", 2),
        task("Task 3", 1)
    )

    end = time.perf_counter()

    print("\nResults:")

    for result in results:
        print(result)

    print(f"\nTotal time: {end - start:.2f} seconds")


asyncio.run(main())