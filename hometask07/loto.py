#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import copy

class card:
    def __init__(self, player, initial_card):
        pass

    @staticmethod
    def gen_numbers(start, end, amount):
        tmp_lst = []
        tmp_set = set()
        for i in range(amount):
            x = random.randint(start, end)
            while x in tmp_set:
                x = random.randint(start, end)
            tmp_set.add(x)
            tmp_lst.append(x)
        return tmp_lst

    @staticmethod
    def gen_card():
        initial_card = [['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
        row_numbers = []
        tmp_lst = card.gen_numbers(1, 90, 15)
        for i in range(0,3):
            if i == 0:
                row_numbers.append(copy.deepcopy(sorted(tmp_lst[0:5])))
            elif i == 1:
                row_numbers.append(copy.deepcopy(sorted(tmp_lst[5:10])))
            elif i == 2:
                row_numbers.append(copy.deepcopy(sorted(tmp_lst[10:15])))
            row_indexes = sorted(card.gen_numbers(0, 8, 5))
            for ind, itm in enumerate(row_numbers[i]):
                initial_card[i][row_indexes[ind]] = itm
        return initial_card

def number_check(barrel_num, user_lst):
    is_found = 0
    for i in range(0, len(user_lst)):
        for ind, itm in enumerate(user_lst[i]):
            if itm == barrel_num:
                is_found += 1
            else:
                is_found += 0
    return is_found

def number_remove(barrel_num, user_lst):
    for i in range(0, len(user_lst)):
        for ind, itm in enumerate(user_lst[i]):
            if itm == barrel_num:
                user_lst[i].remove(itm)

computer_card = card.gen_card()
person_card = card.gen_card()
computer_counter = 15
person_counter = 15
print('\nНачинаем игру.\nВ игре 2 игрока: пользователь и компьютер.\nКаждому в начале выдается случайная карточка.')
print('Карточка компьютера: {}.'.format(computer_card))
print('Карточка игрока: {}.'.format(person_card))

barrel_bag = [itm for itm in range(1, 91)]
while len(barrel_bag) > 0:
    print('Мешочек с бочонками содержит {} бочонков.\n'.format(len(barrel_bag)))
    barrel = random.choice(barrel_bag)
    print('На карточке компьютера осталось {} цифр(ы).'.format(computer_counter))
    print('На карточке игрока осталось {} цифр(ы).'.format(person_counter))
    if person_counter == 0 and computer_counter == 0:
        print('Ничья.')
        break
    elif person_counter > 0 and computer_counter == 0:
        print('\nКомпьютер победил. Игрок проиграл.')
        break
    elif person_counter == 0 and computer_counter > 0:
        print('\nИгрок победил. Компьютер проиграл.')
        break
    else:
        pass
    print('Выбираем один случайный бочонок: {}.\n'.format(barrel))
    print('Карточка компьютера: {}.'.format(computer_card))
    print('Карточка игрока: {}.'.format(person_card))
    answer = input('Продолжить игру? (Да/Нет)')
    if answer.lower() == 'да':
        print('Игра продолжается.')
        answer = input('Зачеркнуть цифру? (Да/Нет)')
        if answer.lower() == 'да':
            check = number_check(barrel, person_card)
            if check == 1:
                print('Цифра {} найдена на карточке игрока.\n'.format(barrel))
                number_remove(barrel, person_card)
                person_counter += -1
                check = number_check(barrel, computer_card)
                if check == 1:
                    number_remove(barrel, computer_card)
                    computer_counter += -1
                    print('Цифра {} найдена на карточке компьютера.\nИгра продолжается.\n'.format(barrel))
                else:
                    print('Цифра {} не найдена на карточке компьютера. Игрок ведет.\nИгра продолжается.\n'.format(barrel))
            else:
                check = number_check(barrel, computer_card)
                if check == 1:
                    print('Цифра {} найдена на карточке компьютера.\n'.format(barrel))
                    number_remove(barrel, computer_card)
                    computer_counter += -1
                    print('Компьютер победил. Игрок проиграл.')
                    break
                else:
                    print('Игрок указал неверный выбор.\nИгрок проиграл, хотя цифра {} отсутствует на обеих карточках.\n'.format(barrel))
                    break
        else:
            print('\nИгрок пропускает ход.')
            check = number_check(barrel, computer_card)
            if check == 1:
                number_remove(barrel, computer_card)
                computer_counter += -1
                print('Цифра {} найдена на карточке компьютера.\nИгра продолжается.\n'.format(barrel))
            else:
                print('Цифра {} не найдена на карточке компьютера.\nИгра продолжается.\n'.format(barrel))
    else:
        print('Игрок проиграл.\n')
        break
    barrel_bag.remove(barrel)


