import itertools

import pytest

from src.character_encoding import (
    bin_to_hex,
    bin_to_utf8,
    bin_to_utf8_hex,
    dec_to_base,
)


@pytest.mark.parametrize(
    "binary, utf8, utf8_hex",
    [
        ("010 0100", "00100100", "24"),
        ("000 1010 0010", "11000010 10100010", "C2 A2"),
        ("0000 1001 0011 1001", "11100000 10100100 10111001", "E0 A4 B9"),
        ("0010 0000 1010 1100", "11100010 10000010 10101100", "E2 82 AC"),
        ("1101 0101 0101 1100", "11101101 10010101 10011100", "ED 95 9C"),
        (
            "0 0001 0000 0011 0100 1000",
            "11110000 10010000 10001101 10001000",
            "F0 90 8D 88",
        ),
    ],
)
def test__wikipedia_examples(
    binary: str,
    utf8: str,
    utf8_hex: str,
):
    assert bin_to_utf8(binary) == utf8
    assert bin_to_utf8_hex(binary) == utf8_hex.replace(" ", "")


def test__decimal_to_binary():
    for dec in range(10_000):
        if str(dec_to_base(dec, 2)) != f"{dec:b}":
            print(f"{dec=}", f"{dec_to_base(dec, 2)=}", f"{dec:b}")


def test__decimal_to_base():
    for dec, base in itertools.product(range(10_000), range(2, 10)):
        base_repr = str(dec_to_base(dec, base))
        if int(base_repr, base) != dec:
            print(f"{dec=}", f"{dec_to_base(dec, base)=}")


def test__binary_to_hexadecimal():
    for dec in range(10_000):
        bin_repr = f"{dec:b}"
        hex_repr = bin_to_hex(str(bin_repr))
        if int(hex_repr, 16) != dec:
            print(f"{dec=}", f"{dec_to_base(dec, 16)=}")
