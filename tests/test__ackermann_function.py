import pytest

from src.ackermann_function import ack


@pytest.mark.parametrize(
    "m, n, expected",
    [
        (0, 0, 1),
        (1, 0, 2),
        (2, 0, 3),
        (3, 0, 5),
        (4, 0, 13),
        (0, 1, 2),
        (1, 1, 3),
        (2, 1, 5),
        (3, 1, 13),
        (0, 2, 3),
        (1, 2, 4),
        (2, 2, 7),
        (3, 2, 29),
        (0, 3, 4),
        (1, 3, 5),
        (2, 3, 9),
        (3, 3, 61),
        (0, 4, 5),
        (1, 4, 6),
        (2, 4, 11),
        (3, 4, 125),
    ],
)
def test__b64_encode(m: int, n: int, expected: int):
    """
    The Ackermann function correctly computes values.
    """

    assert ack(m, n) == expected
