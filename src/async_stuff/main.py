import asyncio
import random
import time


async def do_io_bound_work__async(task_id: int) -> None:
    print(f"\tDoing work for task {task_id}...")
    await asyncio.sleep(random.randrange(0, 5))  # noqa: S311
    print(f"\tFinished work for task {task_id}!")


async def main() -> int:
    s = time.perf_counter()

    tasks = [asyncio.create_task(do_io_bound_work__async(i)) for i in range(10)]
    await asyncio.gather(*tasks, return_exceptions=True)

    print(f"Took {time.perf_counter() - s:.2f} seconds")

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
