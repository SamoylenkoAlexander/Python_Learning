#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите № четверти: '))

options = {
    1: "x>0 и y>0",
    2: "x<0 и y>0",
    3: "x<0 и y<0",
    4: "x>0 и y<0"
}
if 0<x<5: print(options[x])
else: print(f"Значение {x} не является четвертью")