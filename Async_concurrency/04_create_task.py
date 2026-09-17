import asyncio


async def task(name):

    print(f"{name} started")

    await asyncio.sleep(2)

    print(f"{name} finished")

    return f"{name} completed"


async def main():

    task1 = asyncio.create_task(
        task("Task 1")
    )

    task2 = asyncio.create_task(
        task("Task 2")
    )

    task3 = asyncio.create_task(
        task("Task 3")
    )

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print("\nResults:")
    print(result1)
    print(result2)
    print(result3)


asyncio.run(main())