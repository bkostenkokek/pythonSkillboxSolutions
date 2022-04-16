#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
print(my_favorite_movies[0:10])
print(my_favorite_movies[11:25])
print(my_favorite_movies[26:33])
print(my_favorite_movies[34:40])
print(my_favorite_movies[41:])