# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input("Введите натуральное число: "))

binary_number = []
while number >= 1:
    if number % 2 == 0:
        binary_number.append(0)
    else:
        binary_number.append(1)
    number = number // 2
print('В двоичной системе это: ', end = '')
print(*reversed(binary_number))