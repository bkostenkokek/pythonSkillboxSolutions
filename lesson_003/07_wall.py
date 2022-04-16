# -*- coding: utf-8 -*-

# (цикл for)
from lesson_004 import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

for y in range(0, 1001, 50):
    pointa = simple_draw.Point(0, y)
    pointb = simple_draw.Point(1000, y)
    simple_draw.line(pointa, pointb)


for y in range(0, 1001, 50):
    for x in range(0, 1001, 100):
        if y % 100 == 0:
            a = x + 50
        else:
            a = x
        pointa = simple_draw.Point(a, y)
        pointb = simple_draw.Point(a, y + 50)
        simple_draw.line(pointa, pointb)
simple_draw.pause()

# simple_draw.pause()
