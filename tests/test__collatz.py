import pytest

from src.collatz import collatz


# fmt: off
@pytest.mark.parametrize(
    "number, expected",
    [
        (1, [1]),
        (2, [2, 1]),
        (3, [3, 10, 5, 16, 8, 4, 2, 1]),
        (4, [4, 2, 1]),
        (5, [5, 16, 8, 4, 2, 1]),
        (6, [6, 3, 10, 5, 16, 8, 4, 2, 1]),
        (7, [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
        (8, [8, 4, 2, 1]),
        (9, [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
        (10, [10, 5, 16, 8, 4, 2, 1]),
    ],
)
def test__collatz(number: int, expected: list[int]) -> None:
    """
    The collatz function calculates the Collatz sequence.
    """

    assert list(collatz(number)) == expected
# fmt: on
