# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
print('\n\nЗадача 1.')
tmp_list = ['яблоко', 'банан', 'киви', 'арбуз']
for ind, itm in enumerate(tmp_list):
    print(str(ind + 1) + '.', itm.format().rjust(10))

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print('\n\nЗадача 2.')
tmp_list1 = ['яблоко', 'банан', 'киви', 'арбуз']
tmp_list2 = ['банан', 'дыня', 'груша', 'мандарин', 'тыква', 'яблоко']
print('Первый список: {}.'.format(tmp_list1))
print('Второй список: {}.'.format(tmp_list2))
for itm2 in tmp_list2:
    for itm1 in tmp_list1:
        if itm1 == itm2:
            tmp_list1.remove(itm1)
print('Первый список после удаления элементов вторго списка: {}.'.format(tmp_list1))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print('\n\nЗадача 3.')
tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Cписок: {}.'.format(tmp_list))
for ind, itm in enumerate(tmp_list):
    if itm%2 == 0:
        tmp_list[ind] = itm / 4
    else:
        tmp_list[ind] = itm * 2
print('Cписок: {}.'.format(tmp_list))