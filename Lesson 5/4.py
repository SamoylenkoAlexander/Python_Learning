# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('input_data.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст начальный текст, который необходимо сжать: '))
with open('input_data.txt', 'r') as data:
    string = data.readline()

print (string)

def data_encryption(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


secret = data_encryption(string)

with open('output_data.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{secret}')
print(secret)
