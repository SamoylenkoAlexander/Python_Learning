# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

n = int(input('Введите N '))
print(list(range(-n, n+1)))