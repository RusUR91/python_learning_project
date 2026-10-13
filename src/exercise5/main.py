mydict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}

def valid_number(num):
    if not num:
        return False

    # Обработка знака
    start = 0
    if num[0] in ('+', '-'):
        start = 1

    if start >= len(num):
        return False

    # Проверка, что остальные символы — цифры или точка
    has_digit = False
    dot_count = 0
    for i in range(start, len(num)):
        ch = num[i]
        if ch == '.':
            dot_count += 1
            if dot_count > 1:
                return False
        elif ch not in mydict:
            return False
        else:
            has_digit = True

    if not has_digit:
        return False

    return True


num = input().strip()
if not valid_number(num):
    print('Invalid input')
else:
    result = 0
    negative = False
    decimal_places = 0

    # Обработка знака
    start = 0
    if num[0] == '-':
        negative = True
        start = 1
    elif num[0] == '+':
        start = 1

    num = num[start:]

    # Обработка целой части
    for char in num:
        if char == '.':
            break
        result = result * 10 + mydict[char]

    # Обработка дробной части
    if '.' in num:
        decimal_part = num.split('.')[1]
        for char in decimal_part:
            result = result * 10 + mydict[char]
            decimal_places += 1

    if decimal_places > 0:
        result /= 10 ** decimal_places

    if negative:
        result = -result

    # Вывод с тремя знаками после точки
    print(f"{result * 2:.3f}") 
