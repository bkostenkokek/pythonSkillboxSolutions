# -*- coding: utf-8 -*-
import simple_draw as sd

resolution = (1800, 1800)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
color_user = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
              sd.COLOR_PURPLE)


def triangle_v1(point, angle, length, color):
    if angle > 360:
        return
    v1 = sd.Vector(start_point=point, direction=angle, length=length)
    v1.draw(color=color, width=2)
    new_point = v1.end_point
    new_angle = angle + 120
    new_length = length + 0
    triangle_v1(new_point, new_angle, new_length, color)

def square(point, angle, length, color):
    if angle > 359:
        return
    v1 = sd.Vector(start_point=point, direction=angle, length=length)
    v1.draw(color=color, width=2)
    new_point = v1.end_point
    new_angle = angle + 90
    new_length = length + 0
    square(new_point, new_angle, new_length, color)

def pentagon(point, angle, length, color):
    if angle > 359:
        return
    v1 = sd.Vector(start_point=point, direction=angle, length=length)
    v1.draw(color=color, width=2)
    new_point = v1.end_point
    new_angle = angle + 72
    new_length = length + 0
    pentagon(new_point, new_angle, new_length, color)

def hexagon(point, angle, length, color):
    if angle > 359:
        return
    v1 = sd.Vector(start_point=point, direction=angle, length=length)
    v1.draw(color=color, width=2)
    new_point = v1.end_point
    new_angle = angle + 60
    new_length = length + 0
    hexagon(new_point, new_angle, new_length, color)



print('0: RED')
print('1: ORANGE')
print('2: YELLOW')
print('3: GREEN')
print('4: CYAN')
print('5: COLOR_BLUE')
print('6: PURPLE')

user_input = input('Выберите номер цвета >>>')
user = int(user_input)
colors = color_user[user]


point = sd.get_point(50, 50)
triangle_v1(point=point, angle=0, length=100, color=colors)
square(point=point, angle=0, length=100, color=colors)
pentagon(point=point, angle=0, length=100, color=colors)
hexagon(point=point, angle=0, length=100, color=colors)
sd.pause()
