# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности

arr = list(map(int, input("Введите числа через пробел:\n").split()))

res = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        res.append(arr[i])
print(res)