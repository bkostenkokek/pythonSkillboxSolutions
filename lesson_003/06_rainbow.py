# -*- coding: utf-8 -*-

# (цикл for)


from lesson_004 import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)

COLOR_DARK_YELLOW = (127, 127, 0)
COLOR_DARK_ORANGE = (127, 63, 0)
COLOR_DARK_RED = (127, 0, 0)
COLOR_DARK_GREEN = (0, 127, 0)
COLOR_DARK_CYAN = (0, 127, 127)
COLOR_DARK_BLUE = (0, 0, 127)
COLOR_DARK_PURPLE = (127, 0, 127)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

x_start = 50
x_end = 350

for i in range(7):
    x_start += 50
    x_end += 50
    sd.line(sd.Point(x_start, 50), sd.Point(x_end, 450), color=rainbow_colors[i], width=10)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
