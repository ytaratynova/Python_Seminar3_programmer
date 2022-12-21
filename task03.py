# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов,
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def FillTheList(length):
    list_of_numbers = []
    for i in range(length):
        index = random.randint(0, 2)
        list_of_numbers.append(round(random.uniform(-100, 100), index))
    return list_of_numbers

def FractionalPartList(list_of_numbers):
    frac_part = []
    for i in range(len(your_list)):
        if round((abs(your_list[i]) % 1), 2) != 0:
            frac_part.append(round((abs(your_list[i]) % 1), 2))
    return frac_part

len_of_list = int(input("Введите количество элементов списке: "))
your_list = FillTheList(len_of_list)
print(f'Ваш список случайных чисел: {your_list}')

print(f'Масимальная дробная часть чисел в списке: {max(FractionalPartList(your_list))}')
print(f'Минимальная дробная часть чисел в списке, отличная от "0": {min(FractionalPartList(your_list))}')
print(f'Разница между максимальной и минимальной дробной частью: {round((max(FractionalPartList(your_list)) - min(FractionalPartList(your_list))), 2)}')
