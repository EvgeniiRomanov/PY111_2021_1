def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    brackets_open = "("
    brackets_closed = ")"

    stack = []                  # стэк для входа-выхода скобок
    count_in = 0                # счётчик входных скобок
    count_out = 0               # счётчик выходных скобок

    for index, elem in enumerate(brackets_row):
        if elem in brackets_open:
            count_in += 1
            stack.append(elem)
            print(f"Вход: {stack}, {count_in}")
        if elem in brackets_closed:
            count_out += 1
            print(f"Выходят: {stack}, вх:{count_in}, вых: {count_out}")
            if len(stack) == 0:
                return False
            elif count_out > count_in:
                return False
            stack.pop()
            count_in -= 1
            count_out -= 1

        print(f"Прошли шаг: {stack}, вх:{count_in}, вых: {count_out}")
        if index == len(brackets_row) - 1:
            if len(stack) > 0:
                return False

    return True

