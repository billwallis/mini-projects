import pytest
from binary_and_trinary import (
    decimal_to_binary,
    decimal_to_trinary,
)


@pytest.mark.parametrize(
    "decimal, expected",
    [
        (0, 0),
        (1, 1),
        (2, 10),
        (3, 11),
        (4, 100),
        (5, 101),
        (6, 110),
        (7, 111),
        (8, 1000),
    ],
)
def test__decimal_to_binary(decimal: int, expected: int) -> None:
    assert expected == decimal_to_binary(decimal)


@pytest.mark.parametrize(
    "decimal, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 10),
        (4, 11),
        (5, 12),
        (6, 20),
        (7, 21),
        (8, 22),
        (9, 100),
    ],
)
def test__decimal_to_trinary(decimal: int, expected: int) -> None:
    assert expected == decimal_to_trinary(decimal)
