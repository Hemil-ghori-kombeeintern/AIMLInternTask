import asyncio
import time


# -----------------------------
# Synchronous version
# -----------------------------

def sync_task(name):
    print(f"Starting {name}")

    time.sleep(2)

    print(f"Finished {name}")


def run_sync():

    start = time.perf_counter()

    sync_task("Task 1")
    sync_task("Task 2")
    sync_task("Task 3")

    end = time.perf_counter()

    print("\nSynchronous execution time:")
    print(f"{end - start:.2f} seconds")


# -----------------------------
# Asynchronous version
# -----------------------------

async def async_task(name):

    print(f"Starting {name}")

    await asyncio.sleep(2)

    print(f"Finished {name}")


async def run_async():

    start = time.perf_counter()

    await asyncio.gather(
        async_task("Task 1"),
        async_task("Task 2"),
        async_task("Task 3")
    )

    end = time.perf_counter()

    print("\nAsynchronous execution time:")
    print(f"{end - start:.2f} seconds")


print("===== SYNCHRONOUS =====")
run_sync()

print("\n===== ASYNCHRONOUS =====")
asyncio.run(run_async())