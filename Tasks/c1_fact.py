def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError

    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)



def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    result = 1
    while n > 1:
        result *= n
        n -=1

    return result

def factorial_generator(n):
    if n < 0:
        raise ValueError
    f = 1
    for _ in range(1, n + 1):
        f *= _
    yield f
