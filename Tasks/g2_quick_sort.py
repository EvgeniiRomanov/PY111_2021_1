from typing import List


def sort(container: List[int], start: int, end: int) -> List[int]:
    """
    Sort input container with quick sort

    :param end:
    :param start:
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def partition(array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            # Если текущее значение, на которое мы смотрим, больше, чем точка поворота
            # он в нужном месте (справа от точки поворота), и мы можем двигаться влево,
            # к следующему элементу.
            # Нам также нужно убедиться, что мы не превзошли нижний указатель, так как
            # указывает, что мы уже переместили все элементы на правильную сторону от оси
            while low <= high and array[high] >= pivot:
                high = high - 1

            # Процесс, противоположный предыдущему
            while low <= high and array[low] <= pivot:
                low = low + 1

            # Мы либо нашли значения как для максимума, так и для минимума, которые не соответствуют порядку
            # или low выше high, в этом случае выходим из цикла
            if low <= high:
                array[low], array[high] = array[high], array[low]
                # Продолжаем цикл
            else:
                # Выходим из цикла
                break

        array[start], array[high] = array[high], array[start]

        return high

    if start >= end:
        return

    p = partition(container, start, end)
    sort(container, start, p - 1)
    sort(container, p + 1, end)

    return container
