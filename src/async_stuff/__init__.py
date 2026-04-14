import asyncio
import random
import time


async def do_io_bound_work(task_id: int) -> None:
    print(f"Doing work for task {task_id}...")
    await asyncio.sleep(random.randrange(0, 10))  # noqa: S311
    print(f"Finished work for task {task_id}!")


async def main() -> int:
    s = time.perf_counter()

    tasks = [asyncio.create_task(do_io_bound_work(i)) for i in range(50)]
    [await task for task in tasks]

    e = time.perf_counter()
    print(f"Took {round(e - s, 2)} seconds")

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
