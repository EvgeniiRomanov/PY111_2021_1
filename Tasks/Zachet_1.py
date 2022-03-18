# from utils import benchmark
#
#
# @benchmark(10)
def rocket_rent(list_day: list) -> bool:
    """
    Функция вычисляет возможность аренды в заданные интервалы времени одной ракеты

    :param list_day: входной список заявок с интервалами времени аренды от 1 часа в промежутке с 0 до 24 часов
    :return: True, если интервалы времени в заявке не пересекаютcя и одной ракеты хватает для аренды, в противном False
    """

    new_list = []
    for i in range(len(list_day)):
        [new_list.append(k) for k in range(list_day[i][0], list_day[i][1])]

    if len(set(new_list)) != len(new_list):
        return False
    else:
        return True


if __name__ == "__main__":

    list_day1 = [(10, 12), (12, 15), (17, 19), (19, 23), (7, 10), (16, 17), (0, 6), (23, 24)]
    list_day2 = [(10, 12), (12, 15), (17, 19), (19, 23), (7, 10), (16, 17), (13, 14), (18, 23)]
    print(rocket_rent(list_day1))
    print(rocket_rent(list_day2))


    # Федеральный закон от 03.06.2011 N 107-ФЗ (ред. от 22.12.2020) "Об исчислении времени"
    # http://www.consultant.ru/document/cons_doc_LAW_114656/8edcfce37976126566bba2b8f93d3b3b773936b8/