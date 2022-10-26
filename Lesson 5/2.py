# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

from random import randint

def check_input(data: str):
    while not data.isdigit():
        data = input('Введено неверное значение. Повторите ввод\n')
    return data

def another_round():
    if input('Хотите сыграть еще? yes / no\n') == 'yes':
        return True
    else:
        return False

game_is_on = True
while game_is_on:
    print('Добро пожаловать в игру!\n Правила игры следующие: На столе лежит 150 конфета.Первый ход определяется жеребьёвкой.\n\
        За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход игроку.')
    game_mode = input('Выберите режим игры: 1 - игрок против игрока, 2 - игрок против компьютера, 3 - игрок против "умного" компьютера\n\
        exit - выход из игры\n')

    if game_mode == '1':
        stash = 150
        coin = randint(1, 2)
        if coin == 1:
            print('Первым ходит игрок 1')
            player1, player2 = True, False
        else:
            print('Первым ходит игрок 2')
            player1, player2 = False, True
        while stash > 0:
            if player1:
                move = int(check_input(input('Ход игрока 1\n Сколько конфет вы возьмете?\n')))
                if stash > 28:
                    while not 0 < move <= 28:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                elif stash <= 28:
                    while not 0 < move <= stash:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                stash -= move
                player1, player2 = player2, player1
                print(f'Игрок 1 взял {move} конфет. Осталось {stash} конфет')
            else:
                move = int(check_input(input('Ход игрока 2\n Сколько конфет вы возьмете?\n')))
                if stash > 28:
                    while not 0 < move <= 28:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                elif stash <= 28:
                    while not 0 < move <= stash:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                stash -= move
                player1, player2 = player2, player1
                print(f'Игрок 2 взял {move} конфет. Осталось {stash} конфет')
        if player1:
            print('Последний ход сделал Игрок 2, все конфеты достаются ему\n Конец игры')
        else:
            print('Последний ход сделал Игрок 1, все конфеты достаются ему\n Конец игры')
        game_is_on = another_round()

    elif game_mode == '2':
        stash = 150
        coin = randint(1, 2)
        if coin == 1:
            player, bot = True, False
            print('Первым ходит Игрок')
        else:
            player, bot = False, True
            print('Первым ходит компьютер')
        while stash > 0:
            if player:
                move = int(check_input(input('Ваш ход. Сколько конфет вы возьмете?\n')))
                if stash > 28:
                    while not 0 < move <= 28:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                elif stash <= 28:
                    while not 0 < move <= stash:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                stash -= move
                player, bot = bot, player
                print(f' Вы взяли {move} конфет. Осталось {stash} конфет')
            else:
                if stash > 28:
                    move = randint(1, 28)
                    stash -= move
                    player, bot = bot, player
                    print(f'Компьютер берет {move} конфет. Осталось {stash} конфет')
                elif stash <= 28:
                    move = randint(1, stash)
                    stash -= move
                    player, bot = bot, player
                    print(f'Компьютер берет {move} конфет. Осталось {stash} конфет')
        if player:
            print('Машины оказались умнее, поэтому последний ход сделал компьютер и забрал себе все конфеты\n Конец игры')
        else:
            print('Поздравляю, Пользватель! Вы сделали последний ход, и все авации компьютерного мира достаются Вам!\nКонец игры')
        game_is_on = another_round()

    elif game_mode == 'exit':
        print('Увидимся в следующий раз, Пользователь!')
        game_is_on = False