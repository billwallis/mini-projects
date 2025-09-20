"""
The Collatz conjecture, AKA the "3n + 1 problem".

https://en.wikipedia.org/wiki/Collatz_conjecture
https://www.youtube.com/watch?v=094y1Z2wpJg
"""

from collections.abc import Generator


def collatz(n: int) -> Generator[int]:
    while n > 1:
        yield n
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
    yield n
