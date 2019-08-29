# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    tmp_list = []
    i = 0
    while n < 1:
        n = n + 1
    tmp_list.append(n)
    while n <= m:
        i = n + (n - 1)
        tmp_list.append(i)
        n = n + 1
    return tmp_list


print(fibonacci(1, 10))
print(fibonacci(0, 15))
print(fibonacci(-5, 5))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    itm = 0
    i = 0
    length = len(origin_list) - 1
    for ind1, itm1 in enumerate(origin_list):
        itm = itm1
        i = ind1
        while i <= length:
            if origin_list[i] < origin_list[ind1]:
                itm = origin_list[ind1]
                origin_list[ind1] = origin_list[i]
                origin_list[i] = itm
            i = i + 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(origin_list, cond):
    filter_list = []
    for ind, itm in enumerate(origin_list):
        if itm == cond:
            filter_list.append(itm)
    origin_list = filter_list
    return origin_list


print(filter_func([2, 10, -12, 2.5, 20, -11, 4, 4, 0], 4))
print(filter_func(['a', 'b', 'c', 'a'], 'a'))
print(filter_func('aasfjkba', 'a'))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math

def par_task(condition):
    a1a2 = math.sqrt((coord['x2'] - coord['x1'])**2 + (coord['y2'] - coord['y1'])**2)
    a2a3 = math.sqrt((coord['x3'] - coord['x2'])**2 + (coord['y3'] - coord['y2'])**2)
    a3a4 = math.sqrt((coord['x4'] - coord['x3'])**2 + (coord['y4'] - coord['y3'])**2)
    a4a1 = math.sqrt((coord['x1'] - coord['x4'])**2 + (coord['y1'] - coord['y4'])**2)
    if a1a2 == a3a4 and a2a3 == a4a1:
        return True
    else:
        return False

coord = {'x1': 3, 'y1': 1,
         'x2': 4, 'y2': 8,
         'x3': 7, 'y3': 8,
         'x4': 6, 'y4': 1}
print(par_task(coord))
