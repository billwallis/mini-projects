"""
Replicate character encoding logic.

https://youtu.be/jeIBNn5Y5fI
"""

from .base_representations import HEX_BIN_DICT, bin_to_hex, hex_to_bin

###
# UTF-8 encoding
###
#
# uft-8 1 byte:  0 - 127 (7 significant bits)
#    0xxxxxxx
#
# utf-8 2 bytes: 128 - 2047 (8 - 11 significant bits)
#    110xxxxx 10xxxxxx
#
# utf-8 3 bytes: 2048 - 65,535 (12 - 16 significant bits)
#    1110xxxx 10xxxxxx 10xxxxxx
#
# utf-8 4 bytes: 65,536 - 2,097,152 (17 - 21 significant bits)
#    11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
###


BYTE_COUNT_0 = 0
BYTE_COUNT_1 = 1
BYTE_COUNT_2 = 2
BYTE_COUNT_3 = 3
BYTE_COUNT_4 = 4
MAX_SIGNIFICANT_DIGITS = {
    BYTE_COUNT_0: 0,
    BYTE_COUNT_1: 7,
    BYTE_COUNT_2: 11,
    BYTE_COUNT_3: 16,
    BYTE_COUNT_4: 21,
}


def _get_utf8_bytes_required(sig_digits: int) -> int:
    return next(
        (
            x
            for x in MAX_SIGNIFICANT_DIGITS
            if sig_digits <= MAX_SIGNIFICANT_DIGITS[x]
        ),
        0,
    )


def _parse_to_byte(sig_bin_string: str, utf8_bytes: int) -> str:
    parse_string = sig_bin_string.zfill(MAX_SIGNIFICANT_DIGITS[utf8_bytes])
    if utf8_bytes == BYTE_COUNT_1:
        return f"0{parse_string}"
    if utf8_bytes == BYTE_COUNT_2:
        return f"110{parse_string[:5]} 10{parse_string[5:11]}"
    if utf8_bytes == BYTE_COUNT_3:
        return f"1110{parse_string[:4]} 10{parse_string[4:10]} 10{parse_string[10:16]}"
    if utf8_bytes == BYTE_COUNT_4:
        return f"11110{parse_string[:3]} 10{parse_string[3:9]} 10{parse_string[9:15]} 10{parse_string[15:21]}"

    raise ValueError(f"Unexpected number of UTF-8 bytes: {utf8_bytes}")


def bin_to_utf8(bin_string: str) -> str:
    sig_bin = bin_string.replace(" ", "").lstrip("0")
    utf8_bytes = _get_utf8_bytes_required(len(sig_bin))

    return "" if utf8_bytes < 1 else _parse_to_byte(sig_bin, utf8_bytes)


def bin_to_utf8_hex(bin_string: str) -> str:
    return bin_to_hex(bin_to_utf8(bin_string))


def _check_digits(string: str) -> int:
    return next((-1 for i in string if i not in HEX_BIN_DICT), 0)


def unicode_hex_to_utf8_hex(unicode_hex: str) -> str:
    hex_string = unicode_hex
    if unicode_hex[:2].upper() in ("U+", "\\X", "0X", "H&"):
        hex_string = unicode_hex[2:]
    if _check_digits(hex_string) != 0:
        raise ValueError(f"Unexpected character in the hex string {hex_string}")

    return bin_to_utf8_hex(hex_to_bin(hex_string))
