__author__ = 'Лупанова Валерия Александровна'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

a = int(input("Введите, пожалуйста, любое число больше 999999.\n"))

while a < 999999:
    if a < 999999:
        print("Вы ввели слишком маленькое значение.")
        a = int(input("Введите, пожалуйста, любое число больше 999999.\n"))
    else:
        print("Ваше число %s." % a)

print(bool(a) == bool(a ** 2))
print(bool(a) == bool(a * 2))
print(bool(a > 9999))