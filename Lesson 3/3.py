#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

def get_real_nums (n, start, end):
    return [round(uniform(start,end), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    print (f'max = {max(nums)}')
    print (f'min = {min(nums)}')
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
numbers = get_real_nums(n, frst, last)

print (numbers)

print(find_diff(numbers))

# Почему-то в некоторых решениях выдает странные ответы. Например:
# [3.24, 1.29, 2.62, 8.86, 6.93]
# max = 0.93
# min = 0.24
# 0.6900000000000001