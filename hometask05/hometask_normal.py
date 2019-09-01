# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from hometask_easy import create_dir, remove_dir, list_all, getcwd, path
from os import chdir

def action(var):
    if  int(var) == 1:
        print('В какую папку необходимо перейти?\n')
        folder = input()
        curr_path = getcwd()
        if path.isdir(curr_path+'\\'+folder):
            print('Директория {} существует.'.format(curr_path+'\\'+folder))
            chdir(curr_path + '\\' + folder)
            print('Успешно выполнен переход в директорию {}.'.format(getcwd()))
        else:
            print('Невозможно выполнить переход.\nДиректория {} не существует.'.format(curr_path+'\\'+folder))
    elif int(var) == 2:
        print('Содержимое текущей директории:\n')
        list_all()
    elif int(var) == 3:
        print('Какую папку вы хотите удалить?\n')
        folder = input()
        remove_dir(folder)
    elif int(var) == 4:
        print('Какую папку вы хотите создать?\n')
        folder = input()
        create_dir(folder)
    elif int(var) == 5:
        print('Завершение программы.\n')
    else:
        print('Вы ввели некорректное значение.\n')

choice = input(
'Пожалуйста, сделайте выбор:\n\
1: Перейти в папку;\n\
2: Просмотреть содержимое текущей папки;\n\
3: Удалить папку;\n\
4: Создать папку;\n\
5: Завершить программу.\n')
try:
    action(choice)
except:
    print('Вы ввели некорректное значение.')
