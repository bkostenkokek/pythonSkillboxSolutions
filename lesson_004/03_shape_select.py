# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

def triangle_v1(point, angle, length):
    if angle > 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 120
    new_length = length + 0
    triangle_v1(new_point, new_angle, new_length)

def square(point, angle, length):
    if angle > 359:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 90
    new_length = length + 0
    square(new_point, new_angle, new_length)

def pentagon(point, angle, length):
    if angle > 359:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 72
    new_length = length + 0
    pentagon(new_point, new_angle, new_length)

def hexagon(point, angle, length):
    if angle > 359:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 60
    new_length = length + 0
    hexagon(new_point, new_angle, new_length)

print('1: треугольник')
print('2: квадрат')
print('3: пятиугольник')
print('4: шестиугольник')
user = input('Выберите фигуру >> ')
users = int(user)


point = sd.get_point(300, 300)
if users == 1:
    triangle_v1(point=point, angle=0, length=100)
elif users == 2:
    square(point=point, angle=0, length=100)
elif users == 3:
    pentagon(point=point, angle=0, length=100)
elif users == 4:
    hexagon(point=point, angle=0, length=100)
else:
    print('Выбрана неверная фигура')
sd.pause()
