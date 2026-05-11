"""
Replicate the base64 encoding logic.

https://www.base64encode.org/
https://www.lifewire.com/base64-encoding-overview-1166412
"""

import string


def bit_pattern(text: str) -> str:
    """
    Convert the string of characters into a string of 0s and 1s representing
    the binary of the original string.

    For example, the string "Man" would map to the ASCII 77 (M), 97 (a), and
    110 (n). In binary, these ASCII decimals map to 01001101 (77), 01100001
    (97), and 01101110 (110). This functions concatenates and returns these
    binary representations as the string "010011010110000101101110".
    """

    return "".join([bin(ord(_)).replace("b", "").rjust(8, "0") for _ in text])


def chunkify(text: str) -> list[str]:
    """
    Convert a string into chunks, each of size 6.

    For example, the binary string "010011010110000101101110" would be split
    into the list:

        ["010011", "010110", "000101", "101110"]
    """

    return [text[i : (i + 6)] for i in range(0, len(text), 6)]


def index_lookup(chunks: list[str]) -> str:
    """
    Convert a list of strings representing binary into their corresponding
    decimal, and then replace each of them with the character that has the
    index of that decimal in the base-64 character set (index starts at 0).

    The base-64 character set used in this function is the MIME Base64
    implementation which uses A-Z, a-z, and 0-9 for the first 62 characters,
    with "+" and "\\" for the last two:

        ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+\\

    For example, the list of strings

        ["010011", "010110", "000101", "101110"]

    would first map to the decimals

        [19, 22, 5, 110]

    which then map to the characters

        ['T', 'W', 'F', 'u']

    in the base-64 character set, hence a return value of 'TWFu'.
    """

    char_lookup = (
        string.ascii_uppercase + string.ascii_lowercase + string.digits + "+\\"
    )
    pre_padding = "".join(
        [char_lookup[int(chunk.ljust(6, "0"), 2)] for chunk in chunks]
    )
    final_chunk_len = len(chunks[-1])
    if final_chunk_len not in {2, 4, 6}:
        raise ValueError("Unexpected number of bits in final byte.")

    return pre_padding + ["", "==", "="][(final_chunk_len // 2) % 3]


def b64_encode(string_to_encode: str) -> str:
    return index_lookup(chunkify(bit_pattern(string_to_encode)))


def main() -> None:
    credential_string = "IAmBill:P4ssw0rd"
    print(b64_encode(credential_string))


if __name__ == "__main__":
    main()
