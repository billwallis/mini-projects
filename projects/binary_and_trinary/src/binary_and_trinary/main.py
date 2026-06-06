"""
https://pythonguides.com/convert-decimal-numbers-to-binary-in-python/
"""


def decimal_to_binary(decimal: int) -> int:
    if decimal == 0:
        return 0
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return int(binary)


def decimal_to_trinary(decimal: int) -> int:
    if decimal == 0:
        return 0
    binary = ""
    while decimal > 0:
        binary = str(decimal % 3) + binary
        decimal //= 3
    return int(binary)


if __name__ == "__main__":
    for i in range(10):  # pragma: no cover
        n = i**2  # pragma: no cover
        b = decimal_to_binary(n)  # pragma: no cover
        t = decimal_to_trinary(n)  # pragma: no cover
        print(f"{i:4}  {n:4}  {t:8}  {b:8}")  # pragma: no cover
