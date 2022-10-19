#  Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import random

len_list = int(input("Введите длину списка: "))
user_list = []
for i in range(len_list):
    new_num = int(random()*10)
    user_list.append(new_num)
print(user_list)

sum_n = 0
for i in range(1, len(user_list), 2):
    sum_n += user_list[i]
print(f'Сумма элементов списка, стоящих на нечётной позиции {sum_n}')