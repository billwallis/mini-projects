"""
Converting between base representations
"""

import json
import math
import pathlib
from collections.abc import Generator

from bidict import bidict

HERE = pathlib.Path(__file__).parent
MAPPINGS = HERE / "mappings"
DEC_HEX_DICT = bidict(json.loads((MAPPINGS / "dec_hex.json").read_text()))
HEX_BIN_DICT = bidict(json.loads((MAPPINGS / "hex_bin.json").read_text()))
BASE_MIN, BASE_MAX = 2, 10


def chunkify(text: str, chunk_size: int) -> list[str]:
    """
    Split a string into a list of chunk_size strings.
    """

    return [text[i : (i + chunk_size)] for i in range(0, len(text), chunk_size)]


def dec_to_base(base_10_integer: int, new_base: int) -> int:
    """
    Convert a base 10 integer into a new base representation. Only integer
    bases 2 through 9 are supported.
    """

    def get_divisor_and_remainder(integer: int, modulo: int) -> tuple[int, int]:
        """
        Return the divisor and remainder as a 2-tuple.
        """

        return integer // modulo, integer % modulo

    def enumerate_remainders(current_divisor: int) -> Generator[int]:
        """
        Recursively yield the remainder of divisors until the divisor is
        less than the new base.

        Similar to: https://stackoverflow.com/a/34559825/8213085
        """
        div, rem = get_divisor_and_remainder(current_divisor, new_base)
        yield rem
        if div >= new_base:
            yield from enumerate_remainders(div)
        else:
            yield div

    if new_base < BASE_MIN or new_base > BASE_MAX:
        # Need character set mapping after 10, eg F = 15 in hex
        raise ValueError("Bases outside of 2 to 9 are not supported.")

    if base_10_integer == 0:
        return 0

    return int(
        "".join(
            [
                str(i)
                for i in reversed(list(enumerate_remainders(base_10_integer)))
            ]
        )
    )


def bin_to_hex_old(bin_string_in: str) -> str:
    sig_bin = bin_string_in.replace(" ", "").lstrip("0")
    bin_length = 8 * (
        (len(sig_bin) // 8) + (len(sig_bin) % 8 > 0)
    )  # round up to nearest 8
    bin_string = sig_bin.zfill(bin_length)
    ret_string = ""
    for i in range(bin_length // 4):
        nibble = bin_string[(4 * i) : (4 * (i + 1))]
        space = " " * ((i % 2) == 0)
        ret_string += space + HEX_BIN_DICT.inverse[nibble]

    return ret_string[1:]


def bin_to_hex(binary_repr: str) -> str:
    """
    Convert a binary string into its corresponding hexadecimal string
    representation.
    """

    def ceil_to_nearest(number: int, multiple: int) -> int:
        """
        https://datagy.io/python-round-to-multiple/
        """
        return multiple * math.ceil(number / multiple)

    def binary_to_nibbles(bin_repr: str) -> list[str]:
        """
        Convert a binary string into a list of nibbles.
        """
        if bin_repr == "0":
            return ["0000"]

        reduced_binary = bin_repr.replace(" ", "").lstrip("0")
        return chunkify(
            text=reduced_binary.zfill(ceil_to_nearest(len(reduced_binary), 8)),
            chunk_size=4,
        )

    return "".join(
        [
            HEX_BIN_DICT.inverse[nibble]
            for nibble in binary_to_nibbles(binary_repr)
        ]
    )


def hex_to_bin(hex_string_in: str, nibbles: int = -1) -> str:
    if nibbles != -1:
        assert nibbles >= len(hex_string_in)  # noqa: S101
        hex_string = "0" * (nibbles - len(hex_string_in)) + hex_string_in
    else:
        hex_string = hex_string_in

    ret_string = "".join(f" {HEX_BIN_DICT[c]}" for c in hex_string)
    return ret_string[1:]


def bin_to_dec(binary: str) -> int:
    return int(binary, 2)


if __name__ == "__main__":
    print(f"{bin_to_hex_old('01 1100')=}")
    print(f"{bin_to_hex('01 1100')=}")
    print(f"{bin_to_hex('0')=}")
    # print(f'{dec_to_base(38, 2)=}', f'{38:b}')
    # print(f'{dec_to_base(13, 3)=}')
