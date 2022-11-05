# Здесь только логика должна остаться, view выводит на экран

import model
import view



def controller_menu():
    while True:
        choice = view.main_menu()
        match (choice):
            case 0:
                view.printPhoneBook()
            case 1:
                open_file()
            case 2:
                save_file()
            case 3:
                view.input_contact()
                save_file()
            case 4:
                view.input_change()
                save_file()     
            case 5:
                view.remove_contact()
                save_file()
            case 6:
                contacts = view.find_contact()
                print(contacts)
            case 7:
                break



def start():
    controller_menu()



def open_file():
    with open(model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        model.phonebook = contacts_list

def save_file():
    with open(model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(model.phonebook)))