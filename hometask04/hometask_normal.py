# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

import re

print('Решение с помощью re.')
pattern = r'(?<=[A-Z])*[a-z]+'
print('Результат {}.'.format(re.findall(pattern, line)),'\n')

print('Решение без re.')
letters = []
for ind, itm in enumerate(line):
       if itm.isupper():
              letters.append(' ')
       else:
              letters.append(itm)
# Склеиваем буквы в нижнем регистре
# Если до или после буквы не стоят пробелы, значит и до они были в строке рядом
line2 = ''.join(letters)
# Сплитим склеенные наборы, чтобы получить правильные наборы букв
line2 = line2.split(' ')
# Избавляемся от пустых элементов в списке
line = []
for itm in line2:
       if itm != '':
              line.append(itm)
print('Результат {}.'.format(line),'\n')

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

print('Решение с помощью re.')
pattern = r'(?<=[a-z]{2})[A-Z]+(?=[A-Z]{2})'
print('Результат {}.'.format(re.findall(pattern, line_2)),'\n')

line0 = line_2[0]
line1 = []
print('Решение без re.')
# В цикле разделяем наборы элементов с разным регистром запятой
for ind, itm in enumerate(line_2):
       if ind-1>=0 and ind<=len(line_2)-1:
              if (line_2[ind-1].islower() and line_2[ind].isupper()) or (line_2[ind-1].isupper() and line_2[ind].islower()):
                            line0 = line0+','+line_2[ind]
              else:
                            line0 = line0+line_2[ind]

# Сплитим по добавленной запятой для создания списка
line0 = line0.split(',')
# Если рассматриваемый элемнт в верхнем регистре и содержит не менее трех знаков
# (один знак на сам элемент + два после него должно быть в верхнем регистре),
# элемнт до него в нижнем и содержит не менее 2 знаков, то элемент добавляеся в новый массив

for ind, itm in enumerate(line0):
       if ind-1>=0 and ind<=len(line0)-1:
              if len(line0[ind-1]) >= 2 and line0[ind-1].islower() and len(line0[ind]) >= 3 and line0[ind].isupper():
                     line1.append(itm[:-2])
print('Результат {}.'.format(line1),'\n')

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random
with open('hometask_normal_task3.txt','w') as txt:
       for i in range(2500):
              txt.write(str(random.randint(0,9)))
line = []
line2 = ''
line3 = []
with open('hometask_normal_task3.txt','r') as txt:
       line = txt.read()
print('Полученная последовательность сгенерированных чисел:\n{}.'.format(line),'\n')

# Создаем строку по логике:
# если текущий элемент и предыдущий равны, но не равны со следующим, добавляем элемент и ',' (для ситуаций 8899)
# если текущий элемент и предыдущий равны или текущий и последующий равны, добавляем элемент (для ситуаций 7748, 5866)
# в остальных случаях просто добавляем запятую
# очередность условий важна

for ind, itm in enumerate(line):
       if ind>=0 and ind+1<=len(line)-1:
              if line[ind] == line[ind+1] and line[ind] != line[ind-1]:
                     line2 = line2+','+str(line[ind])
              elif line[ind] == line[ind+1] or line[ind] == line[ind-1]:
                     line2 = line2+str(line[ind])
              else:
                     ine2 = line2+','
       elif ind<=len(line)-1 and line[ind] == line[ind-1]:
              line2 = line2+str(line[ind])
print('Промежуточный результат из повторяющихся элементов в виде строки:\n{}.'.format(line2),'\n')
# Создаем список, разделяя элементы по запятой (по логике предыдущей задачи)
line3 = line2.split(',')
print('Промежуточный результат из повторяющихся элементов в виде списка:\n{}.'.format(line3),'\n')

# Создаем словарь, где ключ - последовательность одинаковых цифр,
# значение - количество цифр в этой последовательности
line_dict = {}
for ind, itm in enumerate(line3):
       line_dict[itm]= len(itm)

# Находим максимальное значение в словаре
max_value = max(line_dict.values())
# Находим ключи с максимальным значением
max_items = {k:v for k, v in line_dict.items() if v == max_value}

print('Полученные последовательности:\n{}.'.format(line_dict),'\n')
print('Результат {}.'.format(max_items),'\n')
