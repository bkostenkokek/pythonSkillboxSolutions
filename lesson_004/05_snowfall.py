 -*- coding: utf-8 -*-

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

class Snowlake:
    x = 0
    y = 0
    size = 0

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def move(self)
        self.x += sd.random_number(-20, 20)
        self.y -= sd.random_number(2, 10)

width = 1200
height = 800
sd.resolution = (width, height)

#create snoflakes
snowflakes = []
snowflakeAmount = 25
for _ in range(snowflakeAmount):
    snowflakes.append(Snowflake(
                        sd.random_number(100, width),
                        sd.random_number(300, height),
                        sd.random_number(10, 100))

while True:
    sd.start_drawing()

    for sf in snowflakes:
        point = sd.get_point(sf.x, sf.y)
        sd.snowflake(center=point, length=size, color=sd.background_color)
        sf.move()
        point = sd.get_point(sf.x, sf.y)
        sd.snowflake(center=point, length=size, color=sd.COLOR_WHITE)
        if sf.y <= 25:
            sf.y = sd.random_number(height, height)

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


