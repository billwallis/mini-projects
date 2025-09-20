"""
Examples of how to sum two binary arrays of floats.
"""


def get_bin_array_0_1(bin_len: int) -> list[int]:
    bin_list = []
    for i in range(bin_len + 1):
        if i == 0 or i % 4 not in [0, 3]:
            bin_list.append(0)
        else:
            bin_list.append(1)

    return bin_list


def get_bin_array_0_2(bin_len: int) -> list[int]:
    bin_list = []
    for i in range(bin_len + 1):
        if i % 4 in [2, 3]:
            bin_list.append(1)
        else:
            bin_list.append(0)

    return bin_list


def get_bin_value_array(bin_len: int) -> list[float]:
    factor = 10 ** (bin_len - 1)
    bin_list = [(0.5**i) * factor for i in range(bin_len)]
    bin_list.pop(0)

    return bin_list


def write_array(bin_list: list[int]) -> str:
    return_string = "0."
    for i in bin_list:
        return_string += str(i)

    return return_string


if __name__ == "__main__":
    run_length = 64
    binary_values = get_bin_value_array(run_length)
    array_01 = get_bin_array_0_1(run_length)
    array_02 = get_bin_array_0_2(run_length)

    product_01 = [a * b for a, b in zip(array_01, binary_values, strict=False)]
    product_02 = [a * b for a, b in zip(array_02, binary_values, strict=False)]

    sum_products = sum(product_01) + sum(product_02)

    print(f"{sum_products:32f}")
    # print(write_array(array_01))
    # print(write_array(array_02))
    # print(binary_values)
    # print(product_01)
    # print(product_02)
