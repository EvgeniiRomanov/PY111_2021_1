from utils import benchmark
# Аренда ракет (что бы отрезки не пересекались между собой)
# Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде:
# (час_начала, час_конца), (час_начала, час_конца), ...
# Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова
# (т.е. час_начала может начинаться с Х).
# Дано: список заявок на использование ракет
# Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день

# т.к. час старта может совпадать с окончанием предыдущей аренды, то час окончания не пишем в список

list_day = [[10, 12], [12, 15], [17, 19], [19, 24], [7, 10], [16, 17]]   # случай аренда проходит
#list_day = [[10, 12], [12, 15], [17, 19], [19, 24], [7, 10], [16, 17], [13, 14], [18,23]]   # случай последнее значение входит в list_day[1]
new_list = []
#dict1 = {}

# формируем список чисел
for i in range(len(list_day)):    # с вложенным даст O(N**2)
     [new_list.append(k) for k in range(list_day[i][0], list_day[i][1])]

if len(set(new_list)) != len(new_list):
     print("Не хватает одной ракеты")
else:
     print("Хватает одной ракеты")

print(new_list)

# Реализация через ключи в словаре
# for _ in range(len(new_list)):          # O(N)
#      res = new_list.pop(0)             # O(1)
#      print(res)
#      if dict1.get(res) == None:
#           dict1[res] = 1
#      else:
#           print(f"Ключ {res} уже есть ")

# либо сравнить длину пересечение листа и множества

print(dict1)
#print(new_list)
#print(new_list1)
# for index, elem in enumerate(list_day):
#      new_list.append(elem)
#      #list_day[i] = [k for k in range(list_day[i][0], list_day[i][1])]
#
# print(new_list)
     #
     # if len(new_list) == 0:
     #      new_list.append(list_day[i])
     # else:
     #      if list_day[i].issubset(new_list):
     #           print(f"Но")
     #      else:
     #           new_list.append(list_day[i])
     #print(list_day)


#print(f"Финишный {list_day}")

# def check_brackets(brackets_row: list) -> bool:
#     brackets_open = "("
#     brackets_closed = ")"
#     stack = []                  # стэк для входа-выхода скобок
#
#     for index, elem in enumerate(brackets_row):
#         if elem in brackets_open:
#             stack.append(elem)
#
#         if elem in brackets_closed:
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#
#         if index == len(brackets_row) - 1:
#             if len(stack) > 0:
#                 return False
#
#     return True