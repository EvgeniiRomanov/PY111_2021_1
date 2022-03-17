# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом
import random
#from utils import benchmark
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


def merge_sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:

        # Ищем середину
        mid = len(container) // 2

        # Делим массив
        L = container[:mid]

        # на две части
        R = container[mid:]

        # Сортируем левую часть
        merge_sort(L)

        # Сортируем правую часть
        merge_sort(R)

        i = j = k = 0

        # Копируем данные из временных массивов
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                container[k] = L[i]
                i += 1
            else:
                container[k] = R[j]
                j += 1
            k += 1

        # Проверяем где должен находится элемент
        # из левой части
        while i < len(L):
            container[k] = L[i]
            i += 1
            k += 1

        # из правой
        while j < len(R):
            container[k] = R[j]
            j += 1
            k += 1

    return container


if __name__ == '__main__':
    arr = [random.randint(13, 25) for _ in range(1000000)]

    start = perf_counter()
    my_sort(arr)
    print(f"Quick sort: {perf_counter() - start}")

    start = perf_counter()
    merge_sort(arr)
    print(f"Merge sort: {perf_counter() - start}")

    start = perf_counter()
    arr.sort()
    print(f"List sort: {perf_counter() - start}")