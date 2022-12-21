# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

def FillTheList(length):
    list_of_numbers = []
    for i in range(length):
        list_of_numbers.append(random.randint(-10, 10))
    return list_of_numbers

def MultiplicationOfPairs(list_of_numbers):
    multiplication_list = []
    if len(list_of_numbers) % 2 == 0:
        for i in range(len(list_of_numbers)//2):
            multiplication_list.append(list_of_numbers[i] * list_of_numbers[(len(list_of_numbers))-i-1])
    else:
        for i in range((len(list_of_numbers)//2) + 1):
            multiplication_list.append(list_of_numbers[i] * list_of_numbers[(len(list_of_numbers))-i-1])
    return multiplication_list

len_of_list = int(input("Введите количество элементов списке: "))
your_list = FillTheList(len_of_list)
print(f'Ваш список случайных чисел: {your_list}')
print(f'Произведение пар элементов: {MultiplicationOfPairs(your_list)}')