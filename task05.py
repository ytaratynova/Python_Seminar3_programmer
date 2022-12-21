# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Введите натуральное число: '))

def Fibonachi(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1   
    else:
        return Fibonachi(n-1)+Fibonachi(n-2)
    
fibonachi_list = []
for i in range(-number + 1, number):
    if i < 0:
        fibonachi_list.append(round(((-1)**(i - 1))*Fibonachi(-i)))
    else:
        fibonachi_list.append(Fibonachi(i))
   
print(f'Негафибоначчи U Фибоначчи: {fibonachi_list}')


