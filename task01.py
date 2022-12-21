#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
#  Пример:
#  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def FillTheList(length):
    list_of_numbers = []
    for i in range(length):
        list_of_numbers.append(random.randint(-100, 100))
    return list_of_numbers

def SummOddElements(length, list_of_numbers):
    sum = 0
    for i in range(length):
        if (i % 2) != 0:
            sum += list_of_numbers[i]
    return sum
    
len_of_list = int(input("Введите количество элементов списке: "))
your_list = FillTheList(len_of_list)
print(f'Ваш список случайных чисел: {your_list}')
print(f'Сумма элеметов на нечетных позициях списка: {SummOddElements(len_of_list, your_list)}')




