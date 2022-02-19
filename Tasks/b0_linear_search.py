"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(in_arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    # Можно простыми методами
    ind = in_arr.index(min(in_arr))
    return ind

    # Можно разложить, если есть задача углубиться

    # min_index = 0
    # min_value = in_arr[min_index]
    #
    # for index, cur_value in enumerate(in_arr):
    #     if cur_value < min_value:
    #         min_value = cur_value
    #         min_index = index
    # return min_index

# arr = [10, 15, 35, -4, 8]
#
# print(min_search(arr))