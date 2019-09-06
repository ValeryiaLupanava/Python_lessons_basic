# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random
class person:
    def __init__ (self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def surname(self):
        return self.surname

    def name(self):
        return self.name

    def patronymic(self):
        return self.patronymic

    def get_full_name(self):
        fio = str(self.surname).strip('[]') + ' ' + str(self.name).strip('[]') + ' ' + str(self.patronymic).strip('[]')
        full_fio = ''.join(str(e) for e in fio).replace('\'', '')
        return full_fio

    def get_all_classes(self):
        all_classes = []
        for i in pupils:
            all_classes.append(i.class_[-2:])
        all_classes = set(all_classes)
        return all_classes

    def get_all_subjects(self):
        all_subjects = []
        for i in pupils:
            all_subjects.append(i.subject[i.subject.find('=') + 2 : ])
        all_subjects = set(all_subjects)
        return all_subjects

    @staticmethod
    def get_short_name(surname, name, patronymic):
        fio = str(surname).strip('[]') + ' ' + str(name).strip('[]')[:2] + '. ' + str(patronymic).strip('[]')[:2] + '.'
        short_fio = ''.join(str(e) for e in fio).replace('\'', '')
        return short_fio

class pupil(person):
    def __init__ (self, surname, name, patronymic, class_, subject, teacher, mother=None, father=None):
        person.__init__(self, surname, name, patronymic)
        self.class_ = '\nКласс = ' + class_
        self.subject = '\nПредмет = ' + subject
        self.teacher = '\nУчитель = ' + teacher
        self.mother = '\nМама = ' + mother
        self.father = '\nПапа = ' + father

class teacher(person):
    def __init__(self, surname, name, patronymic, class_=None, subject=None):
        person.__init__(self, surname, name, patronymic)
        self.class_ = '\nКласс = ' + class_
        self.subject = '\nПредмет = ' + subject

class parent(person):
    def __init__(self, surname, name, patronymic):
        person.__init__(self, surname, name, patronymic)

subjects = ['Математика', 'Русский язык', 'Английский язык', 'История', 'Физкультура']
classes = ['5А', '5Б', '5В']

people = [person(['Поддубный'], ['Алексей'], ['Валерьевич']),
          person(['Дьяконова'], ['Ольга'], ['Алексеевна']),
          person(['Скворцов'], ['Максим'], ['Антонович']),
          person(['Марченко'], ['Анна'], ['Григорьевна'])]

for itm in people:
    teachers = [teacher(itm.surname, itm.name, itm.patronymic, random.choice(classes), random.choice(subjects))]

people = [person(['Кортнева'],['Мария'], ['Григорьевна']),
          person(['Малиновская'], ['Инна'], ['Александровна']),
          person(['Андреева'], ['Светлана'], ['Геннадьевна'])]

for itm in people:
    mothers = [parent(itm.surname, itm.name, itm.patronymic)]

people = [person(['Кортнев'], ['Олег'], ['Андреевич']),
          person(['Малиновский'], ['Александр'], ['Петрович']),
          person(['Адреев'], ['Илья'], ['Александрович'])]

for itm in people:
    fathers = [parent(itm.surname, itm.name, itm.patronymic)]

people = [person(['Кортнев'], ['Алексей'], ['Олегович']),
          person(['Малиновская'], ['Ольга'], ['Александровна']),
          person(['Адреев'], ['Максим'], ['Ильич'])]

for itm in people:
    pupils = [pupil(itm.surname, itm.name, itm.patronymic,\
                    random.choice(classes), random.choice(subjects),\
                    person.get_full_name(random.choice(teachers)),\
                    person.get_full_name(random.choice(mothers)),\
                    person.get_full_name(random.choice(fathers)))]
    for itm in pupils:
        print(person.get_short_name(itm.surname, itm.name, itm.patronymic), itm.class_, itm.subject, itm.teacher, itm.mother, itm.father,'\n')

print('Все классы: {}.'.format(person.get_all_classes(pupils)))
print('Список учеников.')
for itm in pupils:
        print(person.get_short_name(itm.surname, itm.name, itm.patronymic))
print('Все предметы: {}.'.format(person.get_all_subjects(pupils)))

