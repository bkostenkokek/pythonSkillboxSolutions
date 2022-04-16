# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
# point = sd.get_point(600, 5)


# def draw_branches(point, angle, lenght):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=lenght)
#     v1.draw()
#     return v1.end_point

# next_point = draw_branches(point=point, angle=90, lenght=100)
# draw_branches(point=next_point, angle=90-30, lenght=100)
# draw_branches(point=next_point, angle=90+30, lenght=100)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# def branch(point, angle, lenght):
#     if lenght < 10:
#         return
#     vector_1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
#     vector_1.draw()
#     next_point = vector_1.end_point
#     next_lenght = lenght * .75
#     branch(point=next_point, angle=angle-30, lenght=next_lenght)
#     branch(point=next_point, angle=angle+30, lenght=next_lenght)
#
# branch(point=point, angle=90, lenght=150)

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# TODO здесь ваш код



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
# Пригодятся функции


sd.pause()
