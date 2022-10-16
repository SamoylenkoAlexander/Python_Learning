# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


nuber_input = int(input('Введите N = '))
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
for i in range(1, nuber_input + 1):
    print(factorial(i), end=' ')