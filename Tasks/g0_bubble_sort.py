from typing import List
from random import randint
from Tasks.utils import benchmark

@benchmark(10)
def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    lenght = len(container)
    for i in range(lenght - 1):             # количество итераций
        for j in range(0, lenght - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j+1] = container[j+1], container[j]
    return container

# if __name__ == '__main__':
#     print(sort([-5, 1, 4, 2, 10, 8, 0]))

arr = [randint(-1000, 1000) for _ in range(1000)]
sort(arr)