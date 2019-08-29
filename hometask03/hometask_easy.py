# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    fix_part = int(number)
    float_part = str(number-int(number))[2:]
    last_digit = int(float_part[ndigits + 1])
    float_part = float_part[:ndigits]
    if last_digit >= 5:
        float_part = str(int(float_part)+1)
    if len(float_part) > ndigits:
        fix_part = fix_part + 1
        float_part = float_part[1:]
    return float(str(fix_part)+'.'+float_part)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    length = len(str(ticket_number))
    sum1 = 0
    sum2 = 0
    if length != 6:
        return 'Номер билета должен быть шестизначным.'
    part1 = str(ticket_number)[0:3]
    part2 = str(ticket_number)[3:6]
    for itm in part1:
        sum1 = sum1 + int(itm)
    for itm in part2:
        sum2 = sum2 + int(itm)
    if sum1 == sum2:
        return part1,part2,sum1,sum2,'Билет счастливый.'
    else:
        return part1,part2,sum1,sum2,'Повезет в другой раз.'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
