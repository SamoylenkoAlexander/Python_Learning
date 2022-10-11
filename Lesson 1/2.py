# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

number = float(input('Введите число: '))

result = int((number * 10) % 10)
if number - int(number) == 0:
    print('нет')
else:
    print(result)