from collections.abc import Generator

import pytest

from src.memoisation import (
    fibonacci,
    fibonacci_memoised,
    fibonacci_nerozi,
)


@pytest.fixture(params=range(0, 30))
def number(request: pytest.FixtureRequest) -> Generator[int]:
    yield request.param


def test__fibonacci(number: int):
    """
    Test the fibonacci function with a range of numbers.
    """

    assert (
        fibonacci(number)
        == fibonacci_memoised(number)
        == fibonacci_nerozi(number)
    )
