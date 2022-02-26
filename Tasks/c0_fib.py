from typing import Iterator

def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    if n in (0, 1):
        return n

    # if n in (1, 2):     # это когда мы 0 заведомо не рассматриваем
    #     return 1
    return fib_recursive(n-1) + fib_recursive(n-2)




def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b

    return a


def fib_generator(n: int) -> Iterator[int]:

    # a, b = 0, 1
    # while n > 0:
    #     yield a
    #     a, b = b, a + b
    #     n -= 1

    a, b = 0, 1
    yield a
    yield b
    for i in range(0, n):
        a, b = b, a + b
        yield a

print(fib_recursive(8))
print(fib_iterative(8))
print(list(fib_generator(8)))