# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом
import random
from utils import benchmark
from time import perf_counter
from typing import List


#@benchmark(10)
def my_sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param end:
    :param start:
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        pivot = container[len(container) // 2]

        less = []
        greater = []
        equal = []

        for i in container:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return my_sort(less) + equal + my_sort(greater)
    else:
        return container


if __name__ == '__main__':
    arr = [random.randint(-10000, 10000) for _ in range(10000)]

    start = perf_counter()
    my_sort(arr)
    print(perf_counter() - start)