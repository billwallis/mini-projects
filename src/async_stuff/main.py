"""
https://youtu.be/oAkLSJNr5zY?si=5n5ytU5MssdzDqS2
"""

import asyncio
import random
import time


async def do_io_bound_work__async(task_id: int) -> None:
    print(f"\tDoing work for task {task_id}...")
    await asyncio.sleep(random.randrange(0, 5))  # noqa: S311
    print(f"\tFinished work for task {task_id}!")


def do_io_bound_work__sync(task_id: int) -> None:
    print(f"\tDoing work for task {task_id}...", flush=True)
    time.sleep(random.randrange(0, 5))  # noqa: S311
    print(f"\tFinished work for task {task_id}!", flush=True)


async def main() -> int:
    # Async IO work
    s = time.perf_counter()
    tasks = [asyncio.create_task(do_io_bound_work__async(i)) for i in range(10)]
    await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Async IO work took {time.perf_counter() - s:.2f} seconds")

    # Sync IO work
    s = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        [
            tg.create_task(asyncio.to_thread(do_io_bound_work__sync, i))
            for i in range(10)
        ]
    print(f"Sync IO work took {time.perf_counter() - s:.2f} seconds")

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
