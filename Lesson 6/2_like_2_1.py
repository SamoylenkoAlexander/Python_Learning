# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = input('Введите х = ')
# sum = 0
# for i in x:
#     sum += int(i)
# print(sum)

print(len(x))

for i, num in enumerate(x, start=1):
    print(f'i{i} = {num}')

result = sum([int(i) for i in str(x)])
print(result)