# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            None


class Air:
    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            None


class Fire:
    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if isinstance(other, Earth):
            return Magma()
        else:
            None


class Earth:
    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Magma()
        else:
            None


class Storm:
    def __str__(self):
        return "Шторм"


class Vapor:
    def __str__(self):
        return "Пар"


class Dirt:
    def __str__(self):
        return "Грязь"


class Lightning:
    def __str__(self):
        return "Молния"


class Dust:
    def __str__(self):
        return "Пыль"


class Magma:
    def __str__(self):
        return "Лава"


water = Water()
air = Air()
earth = Earth()
fire = Fire()

print(water + air)
print(water + earth)
print(water + fire)


# element_user_1 = input("Введите елемент №1: ")
# element_user_2 = input("Введите елемент №2: ")
# if element_user_1 == "Water" and element_user_2 == "Air":
#     print("Вы создали Шторм")
# else:
#     print("Вы ввели неверные елементы")
#
#



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
