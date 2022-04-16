# -*- coding: utf-8 -*-

# (определение функций)
from lesson_004 import simple_draw as sd

sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x, y, color):
    center_position = sd.get_point(x, y)
    sd.circle(center_position=center_position, radius=50, color=color, width=2)
    sd.line(sd.get_point(x - 20, y - 5), sd.get_point(x - 10, y - 20), color, 2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, 2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 20, y - 5), color, 2)
    sd.line(sd.get_point(x - 15, y + 20), sd.get_point(x - 15, y + 5), color, 2)
    sd.line(sd.get_point(x + 15, y + 20), sd.get_point(x + 15, y + 5), color, 2)


for i in range(10):
    point = sd.random_point()
    x = point.x
    y = point.y
    color = sd.random_color()
    smile(x, y, color)

sd.pause()
