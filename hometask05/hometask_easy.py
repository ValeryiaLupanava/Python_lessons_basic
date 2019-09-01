# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

from os import getcwd, path, mkdir, rmdir

def create_dir(new_dir):
    curr_path = getcwd()
    if path.isdir(curr_path+'\\'+new_dir):
        print('Невозможно создать файл.\nДиректория {} уже существует.'.format(curr_path+'\\'+new_dir))
    else:
        mkdir(curr_path+'\\'+new_dir)
        print('Успешно создана директория {}.'.format(curr_path+'\\'+new_dir))

def remove_dir(new_dir):
    curr_path = getcwd()
    if path.isdir(curr_path+'\\'+new_dir):
        rmdir(curr_path+'\\'+new_dir)
        print('Успешно удалена директория {}.'.format(curr_path+'\\'+new_dir))
    else:
        print('Невозможно удалить файл.\nДиректория {} не существует.'.format(curr_path+'\\'+new_dir))

# create_dir('dir_1')
# create_dir('dir_9')
# remove_dir('dir_1')
# remove_dir('dir_9')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

from os import listdir, getcwd, walk
# Вывод папок и файлов
def list_all():
    curr_path = getcwd()
    if len(listdir(curr_path)) == 0:
        print('Невозможно вывести объекты директории: {}.\nВ директории нет содержимого.'.format(listdir(curr_path)))
    else:
        print('Успешно выведено содержимое директории: {}.\n'.format(listdir(curr_path)))

# list_all()

# Вывод только папок
def list_folders():
    curr_path = walk(getcwd())
    for ind, itm in enumerate(curr_path):
        if ind != 0:
            print('Успешно выведены папки директории: {}.\n'.format(itm))

# list_folders()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
from os import path, getcwd, remove, listdir
from shutil import copyfile
from sys import argv

script = path.basename(argv[0])
copy_script = 'copy_'+script
if path.isfile(getcwd()+'\\'+copy_script):
    remove(copy_script)
    copyfile(script, copy_script)
    print('Копия файла {} пересоздана.\nФайлы директории: {}.'.format(script, listdir(getcwd())))
else:
    copyfile(script, copy_script)
    print('Копия файла {} создана.\nФайлы директории: {}.'.format(script, listdir(getcwd())))
