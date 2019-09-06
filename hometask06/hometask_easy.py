# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

# Координаты А1(х1, у1), А2(x2 ,у2), А3(x3 , у3)
class calculations:
    def __init__(self, side):
        self.x1 = side[0]
        self.y1 = side[1]
        self.x2 = side[2]
        self.y2 = side[3]
        self.x3 = side[4]
        self.y3 = side[5]

    def square(self):
        return (1/2)*((self.x1 - self.x3)*(self.y2 - self.y3) -\
                          (self.x2 - self.x3)*(self.y1 - self.y3))

    def height(self):
        return abs((self.y2 - self.y3)*self.x1 + (self.x3 - self.x2)*self.y1 + (self.x2*self.y3 - self.x3*self.y2))/\
               sqrt((self.y2 - self.y3)**2 + (self.x3 - self.x2)**2)

    def perimeter(self):
        return sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2) +\
               sqrt((self.x2 - self.x3)**2 + (self.y2 - self.y3)**2) +\
               sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)

print('\nТреугольник.\n')
triangle = calculations((1, 1, 4, 3, 5, 1))
print('Координаты треугольника А1({},{}), А2({},{}), А3({},{}).'.format(triangle.x1, triangle.y1,\
                                                                            triangle.x2, triangle.y2,\
                                                                            triangle.x3, triangle.y3))
print('Площадь треугольника S = {}.'.format(round(abs(triangle.square()),2)))
print('Высота треугольника H = {}.'.format(round(abs(triangle.height()),2)))
print('Периметр треугольника P = {}.'.format(round(abs(triangle.perimeter()),2)))



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Координаты А1А2(х1, у1), А2А3(x2 ,у2), А3А4(x3 , у3), А4А1(x4 , у4)
class calculations:
    def __init__(self, side):
        self.x1 = side[0]
        self.y1 = side[1]
        self.x2 = side[2]
        self.y2 = side[3]
        self.x3 = side[4]
        self.y3 = side[5]
        self.x4 = side[6]
        self.y4 = side[7]

        # Находим уникальные значения y-координат
        # Если только два y-значения уникальны, значит основания считаем по x-координатам
        # В обратном случае, основания считаем по y-координатам

        self.x_list = sorted([self.x1, self.x2, self.x3, self.x4])
        self.cnt_x = len(set(self.x_list))

        self.y_list = sorted([self.y1, self.y2, self.y3, self.y4])
        self.cnt_y = len(set(self.y_list))

        if self.cnt_y == 2:
            self.A1A2 = abs(self.x1 - self.x2)
            self.A3A4 = abs(self.x3 - self.x4)
            self.H = abs(self.y3 - self.y1)
        # Найдем расстояния от высоты до границ большего основания
        # А далее, имея длины этих отрезков, боковые стороны можно найти
        # как гипотенузы прямоугольных треугольников

        # K - расстояние от высоты до левой границы большего основания
            self.K = (abs(self.x_list[0] - self.x_list[1]))
            self.A4A1 = round(sqrt(self.K**2 + self.H**2))
        # M - расстояние от высоты до правой границы большего основания
            self.M = (abs(self.x_list[2] - self.x_list[3]))
            self.A2A3 = round(sqrt(self.M**2 + self.H**2))
        else:
        # Расчеты, аналогичные описанным выше, если основания параллельны оси ординат
            self.A1A2 = abs(self.y1 - self.y2)
            self.A3A4 = abs(self.y3 - self.y4)
            self.H = abs(self.x3 - self.x1)

            self.K = (abs(self.y_list[0] - self.y_list[1]))
            self.A4A1 = round(sqrt(self.K**2 + self.H**2))

            self.M = (abs(self.y_list[2] - self.y_list[31]))
            self.A2A3 = round(sqrt(self.M**2 + self.H**2))

    def ifIsosceles(self):
        if self.A2A3 == self.A4A1:
            return True
        else:
            return False

    def perimeter(self):
        return self.A4A1 + self.A1A2 + self.A2A3 + self.A3A4

    def square(self):
        return (1/2)*(self.A1A2 + self.A3A4)*self.H

print('\nТрапеция 1.\n')
trapeze = calculations((3, 2, 5, 2, 9, 6, 6, 6))
print('Координаты трапеции А1({},{}), А2({},{}), А3({},{}), А4({},{}).'.format(trapeze.x1, trapeze.y1,\
                                                                                     trapeze.x2, trapeze.y2,\
                                                                                     trapeze.x3, trapeze.y3,\
                                                                                     trapeze.x4, trapeze.y4))
print('Равнобедренная ли трапеции: {}.'.format(trapeze.ifIsosceles()))
print('Площадь трапеции S = {}.'.format(round(abs(trapeze.square()),2)))
print('Периметр трапеции P = {}.'.format(round(abs(trapeze.perimeter()),2)))

print('\nТрапеция 2.\n')
trapeze = calculations((1, 1, 6, 1, 5, 3, 2, 3))
print('Координаты трапеции А1({},{}), А2({},{}), А3({},{}), А4({},{}).'.format(trapeze.x1, trapeze.y1,\
                                                                                     trapeze.x2, trapeze.y2,\
                                                                                     trapeze.x3, trapeze.y3,\
                                                                                     trapeze.x4, trapeze.y4))
print('Равнобедренная ли трапеции: {}.'.format(trapeze.ifIsosceles()))
print('Площадь трапеции S = {}.'.format(round(abs(trapeze.square()),2)))
print('Периметр трапеции P = {}.'.format(round(abs(trapeze.perimeter()),2)))