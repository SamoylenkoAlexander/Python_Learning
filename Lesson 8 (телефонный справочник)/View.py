# Здесь должно быть всё по выводу на экран

import model


def printPhoneBook():
    for i, item in enumerate(model.phonebook):
        print(i , item)

def main_menu():
    print('\nГлавное меню:')
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')
    print('7. Выход')
    choice = int(input('Выберите пункт меню: '))
    return choice

def input_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone}; \n'
    model.phonebook.append(contact)
    return (name, surname, last_name, phone, contact)

def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить?')
    choice = int(input('0 - Имя, 1 - Фамилия, 2 - Отчество, 3 - Телефон: '))
    value = model.phonebook.pop(id).split(';')
    value[choice] = input('Введите изменения: ')
    model.phonebook.insert(id, ';'.join(value))
    return (id, choice, value)

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    model.phonebook.pop(choice)


def find_contact():
    letters = input('Введите имя, фамилию, отчество или номер контакта\n')
    book = model.phonebook
    for i in book:
        if letters in i:
            return(i)
