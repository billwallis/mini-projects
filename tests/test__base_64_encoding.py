import base64

import pytest

from src.base_64_encoding import (
    b64_encode,
    bit_pattern,
    chunkify,
    index_lookup,
)


def stdlib_b64_encode(string_to_encode: str) -> str:
    return base64.b64encode(string_to_encode.encode("UTF-8")).decode()


def test__strings_can_be_converted_to_bit_patterns():
    """
    Strings can be converted to bit patterns.
    """

    assert bit_pattern("Man") == "010011010110000101101110"


def test__bit_patterns_can_be_chunkified():
    """
    Bit patterns can be chunkified.
    """

    assert chunkify("010011010110000101101110") == [
        "010011",
        "010110",
        "000101",
        "101110",
    ]


def test__chunkified_bit_patterns_can_be_indexed():
    """
    Chunkified bit patterns can be indexed to produce base-64 encoded strings.
    """

    assert index_lookup(["010011", "010110", "000101", "101110"]) == "TWFu"


@pytest.mark.parametrize(
    "string_to_encode",
    ["foo", "fooBarBaz", "abcd-1234", "IAmBill:P4ssw0rd"],
)
def test__b64_encode(string_to_encode: str):
    """
    My ``b64_encode`` function produces the same output as the
    ``base64.b64encode`` function.
    """

    assert b64_encode(string_to_encode) == stdlib_b64_encode(string_to_encode)
