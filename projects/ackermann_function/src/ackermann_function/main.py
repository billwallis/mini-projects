"""
Testing the Ackermann function.

https://www.youtube.com/watch?v=i7sm9dzFtEI&ab_channel=Computerphile
https://en.wikipedia.org/wiki/Ackermann_function
"""

import itertools


def ack(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)

    return ack(m - 1, ack(m, n - 1))


def main() -> None:
    x, y = 4, 4
    for i, j in itertools.product(range(x), range(y)):
        print(f"ackermann({i}, {j}) = {ack(i, j)}")


if __name__ == "__main__":
    main()
