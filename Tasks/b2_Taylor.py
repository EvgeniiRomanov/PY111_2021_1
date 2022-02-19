"""
Taylor series
"""
import math
from typing import Union
from itertools import *

EPSILON = 0.0001

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    def get_item(n):
        return x ** n / math.factorial(n)

    sum_ = 0
    for i in count(0,1):
        cur_item =get_item(i)
        sum_ += cur_item

        if cur_item < EPSILON:
            break

    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    # sum_ = 0
    # n = 0
    #
    # while (x**(2*n-1)) / math.factorial(n) < EPSILON:
    #     x = x * ((-x**2) / (2*n*(n+1))
    #     sum_ = sum_ + x
    #     n = n + 1

    sinx_ = 0
    delta = 0.0001
    for n in count(0, 1):
        sin_x_n = (((-1) ** n) / math.factorial((2 * n) +1)) * (x ** ((2 * n) +1))
        sinx_ += sin_x_n
        if abs(sin_x_n) < delta:
            break

    return sinx_
