from utils import benchmark


@benchmark(10)
def rocket_rent(list_day: list) -> bool:
    """
    Функция вычисляет возможность аренды в заданные интервалы времени одной ракеты

    :param list_day: входной список заявок с интервалами времени аренды
    :return: True, если интервалы времени в заявке не пересекаютcя и одной ракеты хватает, в противном False
    """

    new_list = []
    for i in range(len(list_day)):
        [new_list.append(k) for k in range(list_day[i][0], list_day[i][1])]
    if len(set(new_list)) != len(new_list):
        return False
    else:
        return True


if __name__ == "__main__":

    list_day1 = [(10, 12), (12, 15), (17, 19), (19, 23), (7, 10), (16, 17)]
    list_day2 = [(10, 12), (12, 15), (17, 19), (19, 23), (7, 10), (16, 17), (13, 14), (18, 23)]
    print(rocket_rent(list_day1))
    print(rocket_rent(list_day2))
