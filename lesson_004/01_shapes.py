# -*- coding: utf-8 -*-

import simple_draw as sd
resolution = (1200, 800)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
point = sd.get_point(200, 200)



def triangle_v1(point, angle, length):
    if angle > 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 120
    new_length = length + 0
    triangle_v1(new_point, new_angle, new_length)

# triangle_v1(point, 0, 100)

def square(point, angle, length):
    if angle > 359:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 90
    new_length = length + 0
    square(new_point, new_angle, new_length)

# square(point, 0, 100)

def pentagon(point, angle, length):
    if angle > 359:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 72
    new_length = length + 0
    pentagon(new_point, new_angle, new_length)

# pentagon(point, 0, 100)

def hexagon(point, angle, length):
    if angle > 359:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    new_point = v1.end_point
    new_angle = angle + 60
    new_length = length + 0
    hexagon(new_point, new_angle, new_length)

hexagon(point, 0, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
