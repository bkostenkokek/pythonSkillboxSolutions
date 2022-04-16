# -*- coding: utf-8 -*-

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


import simple_draw as sd

width = 1200
hight = 800

sd.resolution = (1200, 800)

# TODO здесь ваш код

point_list = []
snowfallAmount = 25
for _ in range(snowfallAmount):
    point_list.append([sd.random_number(100, width), sd.random_number(300, hight), sd.random_number(10, 100)])

while True:
    sd.start_drawing()
    for i, (x, y, length) in enumerate(point_list):
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length, color=sd.background_color)
        point_list[i][0] += sd.random_number(-20, 20)
        point_list[i][1] -= sd.random_number(2, 10)
        point = sd.get_point(point_list[i][0], point_list[i][1])
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
        if point_list[i][1] <= 25:
            point_list[i][1] = sd.random_number(hight, hight)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


