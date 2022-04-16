# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

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


# TODO здесь ваш код

N = 50
point_list = []
for _ in range(N):
    point_list.append([sd.random_number(100, 1100), sd.random_number(300, 850), sd.random_number(10, 100)])

while True:
    sd.clear_screen()
    for i, (x, y, length) in enumerate(point_list):
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length)
        point_list[i][0] += sd.random_number(-20, 20)
        point_list[i][1] -= sd.random_number(2, 10)
        if y < 10:
            break
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

