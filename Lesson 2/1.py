# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = input('Введите х = ')
sum = 0
for i in x:
    sum += int(i)
print(sum)