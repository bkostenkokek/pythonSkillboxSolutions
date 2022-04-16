# -*- coding: utf-8 -*-

from lesson_004 import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код+
# point = sd.get_point(200, 200)
# radius = 40
# for i in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
# def circle(point, step):
#     radius = 40
#     for i in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius)

# point = sd.get_point(200, 200)
# circle(point=point, step=5)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# for x in range(100, 1105, 120):
#     point = sd.get_point(x, 100)
#     radius = 40
#     circle(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# for x in range(100, 1105, 120):
#     for y in range(100, 350, 120):
#         point = sd.get_point(x, y)
#         circle(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
# for i in range(100):
#     point = sd.random_point()
#     circle(point=point, step=5)


sd.pause()
