# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

from email import message
from itertools import count
import random
from random import randint, choice

def game_1(a, b, pl, mes):
    count = chose_first_move()
    print(f'\nПервый ход игрока {pl[count % 2]}')
    while a > 0:
        print(f'\n{pl[count % 2]}, {random.choice(mes)}')
        move = int(input())
        if move < 1 or move > b:
            print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
            attempt = 3
            while attempt > 0:
                if move <= a and move <= b and move > 1:
                    break
                print(f'Попробуй еще раз, у вас {attemp} попыток')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Жаль, не осталось попыток. Конец игры')
        a -= move
        if a > 0:
            print(f'Осталось конфет {a}')
        else:
            print('Не осталось конфет')
        count += 1
    return pl[not count % 2]

def game_bot(a, b, pl, mes):
    count = chose_first_move()
    print(f'\nПервый ход игрока {pl[count % 2]}')
    while a > 0:
        if count % 2:
            move = randint(1, b)
            print(f'\nБот забирает {move}')
        else:
            print(f'\n{pl[0]}, {choice(mes)}')
            move = int(input())
            if move < 1 or move > b:
                print(f'Можно взять не более {b}, осталось {a}')
                attempt = 3
                while attempt > 0:
                    if move <= a and move <= b and move > 0:
                        break
                    print(f'Попробуй еще раз, у вас {attemp} попыток')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Жаль, не осталось попыток. Конец игры')
        a -= move
        if a > 0:
            print(f'Осталось конфет {a}')
        else:
            print('Не осталось конфет')
        count += 1
    return pl[not count % 2]

def choose_first_move():
    return randint(0, 1)

def introduce_player(d):
    if d == 0:
        player1 = input("\n Введите имя: ")
        player2 = input("\n Введите имя: ")
        return [player1, player2]
    else:
        player1 = input("\n Введите имя: ")
        player2 = 'Бот'
        print(f'\nИгрок {player2}')
        return [player1, player2]
    
def game(d):
    if d == 0:
        winner = game_1
    elif d == 1:
        winner = game_bot
        
    if not winner:
        print('Нет победителя')
    else:
        print(f'Победил {winner}')
        
greeting = ('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.' 
            '\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. '
            '\nВсе конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому '
            '\nигроку, чтобы забрать все конфеты у своего конкурента?')

messages = ['Ваша очередь', 'Смелее берите', 'Ваша ход']

print(greeting)

n = int(input('Введите количество розыгрываеммых конфет: '))
m = int(input('Максимальное кол-во конфет за ход: '))
lv1 = int(input('Выберите уровень сложности: '
                '\n 0 - player vs player'
                '\n 1 - player vs bot'))

players = introduce_player(lv1)
winner = game(lv1)