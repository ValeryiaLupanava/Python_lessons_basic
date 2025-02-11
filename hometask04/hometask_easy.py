# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

int_list = [1, 2, 4, 0]
sqr_list = [itm**2 for itm in int_list]
print('Исходный список с целыми числами {}.'.format(int_list))
print('Второй список с квадратами исходного списка {}.\n'.format(sqr_list))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

frt_list1 = ['дыня', 'мандарин', 'слива', 'манго', 'арбуз']
frt_list2 = ['арбуз', 'яблоко', 'груша', 'дыня', 'слива']
frt_list3 = [itm for itm in frt_list1 for itmx in frt_list2 if itm == itmx]
print('Первый список фруктов {}.'.format(frt_list1))
print('Второй список фруктов {}.'.format(frt_list2))
print('Набор фруктов из обоих списков {}.\n'.format(frt_list3))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
tmp_list1 = [random.randint(-100, 100) for i in range(20)]
tmp_list2 = [itm for itm in tmp_list1 if itm%3 == 0 and itm > 0 and itm%4 != 0]
print('Первый список, заполненный произвольными числами {}.'.format(tmp_list1))
print('Второй список, удовлетворяющий условия задания {}.'.format(tmp_list2))