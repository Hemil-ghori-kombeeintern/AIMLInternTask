# import asyncio

# async def task(name, seconds):
#     print(f"{name} started")

#     await asyncio.sleep(seconds)

#     print(f"{name} finished")

# async def main():
#     # await task("Task 1", 3)
#     # await task("Task 2", 2)
#     # await task("Task 3", 1)

#     await asyncio.gather(
#         task("Task 1", 3),
#         task("Task 2", 2),
#         task("Task 3", 1)
#     )

# asyncio.run(main())

# import asyncio

# async def task(name):
#     print(f"{name} started")

#     await asyncio.sleep(2)

#     print(f"{name} finished")

# async def main():

#     task1 = asyncio.create_task(task("Task 1"))
#     task2 = asyncio.create_task(task("Task 2"))

#     await task1
#     await task2

# asyncio.run(main())

import asyncio

async def calculate(x):
    await asyncio.sleep(1)
    return x * 2

async def main():

    results = await asyncio.gather(
        calculate(10),
        calculate(20),
        calculate(30)
    )

    print(results)

asyncio.run(main())