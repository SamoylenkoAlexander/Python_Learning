# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input("Введите число: "))
sequence_list = {i:round((1+ 1 / i)**i) for i in range(1, num+1)}
print(sequence_list, "Сумма значений: ", sum(sequence_list.values()))