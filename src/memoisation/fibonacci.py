def fibonacci(n: int) -> int:
    """
    Naive fibonacci implementation.
    """

    return 1 if n in {0, 1} else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoised(n: int) -> int:
    """
    Memoised version of the fibonacci function.
    """

    cache = {0: 1, 1: 1}

    def wrapper(n_: int) -> int:
        if n_ in cache:
            return cache[n_]

        value = wrapper(n_ - 1) + wrapper(n_ - 2)
        cache[n_] = value

        return value

    return wrapper(n)


def fibonacci_nerozi(n: int) -> int:
    """
    Stolen from the main man, Mr Nerozi.
    """

    if n in {0, 1}:
        return 1

    sequence = [1, 1]
    sequence.extend(sequence[c - 1] + sequence[c - 2] for c in range(2, n + 1))

    return sequence[n]
