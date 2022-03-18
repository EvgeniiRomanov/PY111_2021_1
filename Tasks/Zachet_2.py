# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом
import random
from time import perf_counter
from typing import List
import g0_bubble_sort
import g1_merge_sort
import g2_quick_sort


def count_sort_1(container: List[int]) -> List[int]:
    """
    Sort input container [13, 26] with count sort
    :param container: list of in elements to be sorted
    :return: container sorted in ascending order
    """
    tmp_list = [0] * 26
    result_list = []

    for value in container:
        tmp_list[value] += 1

    for index, value in enumerate(tmp_list):
        if value > 0:
            result_list += [index] * value

    return result_list


def count_sort_2(container: List[int]) -> List[int]:
    """
    Sort input container [13, 26] with count sort
    :param container: list of int elements to be sorted
    :return: container sorted in ascending order
    """
    tmp_list = [elem for elem in range(13, 26)]
    result_list = []

    for elem in tmp_list:
        k = container.count(elem)
        result_list += [elem] * k

    return result_list


if __name__ == '__main__':
    arr = [random.randint(13, 25) for _ in range(100)]
    # arr = [random.randint(13, 25) for _ in range(1000000)]

    # Bubble sort
    arr2 = arr.copy()
    start = perf_counter()
    g0_bubble_sort.sort(arr2)
    print(f"Bubble sort: {perf_counter() - start}")
    arr2.clear()

    # Quick sort
    arr2 = arr.copy()
    start = perf_counter()
    g2_quick_sort.sort(arr2)
    print(f"Quick sort: {perf_counter() - start}")
    arr2.clear()

    # Merge sort
    arr2 = arr.copy()
    start = perf_counter()
    g1_merge_sort.sort(arr2)
    print(f"Merge sort: {perf_counter() - start}")
    arr2.clear()

    # Inner List sort
    arr2 = arr.copy()
    start = perf_counter()
    arr2.sort()
    print(f"Inner List sort: {perf_counter() - start}")
    arr2.clear()

    # Count_sort_1
    arr2 = arr.copy()
    start = perf_counter()
    count_sort_1(arr2)
    print(f"Count sort 1: {perf_counter() - start}")
    arr2.clear()

    # Count_sort_2
    arr2 = arr.copy()
    start = perf_counter()
    count_sort_2(arr2)
    print(f"Count sort 2: {perf_counter() - start}")
    arr2.clear()