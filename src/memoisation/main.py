"""
https://en.wikipedia.org/wiki/Memoization
"""

import functools
import sys
import timeit

from memoisation.fibonacci import (
    fibonacci,
    fibonacci_memoised,
    fibonacci_nerozi,
)

sys.setrecursionlimit(1500)


def fibonacci_timer(number: int) -> None:
    """
    Time the three different versions.
    """

    n = 30
    t = functools.partial(timeit.timeit, number=number)

    print("original:", t(lambda: fibonacci(n)))
    print("memoised:", t(lambda: fibonacci_memoised(n)))
    print("nerozi's:", t(lambda: fibonacci_nerozi(n)))


def main() -> None:
    fibonacci_timer(100)


if __name__ == "__main__":
    main()
