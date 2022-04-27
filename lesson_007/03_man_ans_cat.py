# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код


class Man:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.money = 50
        self.food = 0

    def __str__(self):
        return "Я - {}, сытность - {}, денег - {}".format(self.name, self.satiety, self.money)

    def work(self):
        print("{}, пошел на работу".format(self.name))
        self.money += 150
        self.satiety -= 50

    def play_DOTA_2(self):
        print("{}, играл в DOTA целый день".format(self.name))
        self.satiety -= 20

    def shopping(self):
        print("{}, покупал еду".format(self.name))
        self.food += 50
        self.money -= 50
        self.satiety -= 10

    def eat(self):
        print("{}, покушал".format(self.name))
        self.satiety += 50

    def bogdan_act(self):
        if self.satiety <= 0:
            print("{}, RIP".format(self.name))
        elif self.satiety <= 20:
            self.eat()
        elif self.food <= 50:
            self.shopping()
        elif self.money <= 50:
            self.work()
        else:
            self.play_DOTA_2()



class Cat:
    def __init__(self, name):
        self.food = 0
        self.dirt = 0
        self.home = None
        self.name = name

    def sleep(self):
        print("{}, спит".format(self.name))
        self.food -= 10

    def eat(self):
        print("{}, кушает".format(self.name))



    def drat_oboi(self):
        print("{}, подрал обои".format(self.name))
        self.food -= 10
        self.dirt += 5


ppl = Man(name="Богдан")


for day in range(365):
    print('====================== {} day ======================'.format(day))
    ppl.bogdan_act()
    print('====================== в конце дня ======================')























# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
