# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.central_street.house1 import room1 as cs_r1, room2 as cs_r2
from district.central_street.house2 import room1 as cs_r1_1, room2 as cs_r2_1
from district.soviet_street.house1 import room1 as ss_r1, room2 as ss_r2
from district.soviet_street.house2 import room1 as ss_r1_2, room2 as ss_r2_2

print('На районе central_street живут -', ', '.join(cs_r1.folks), ', '.join(cs_r2.folks), ', '.join(cs_r1_1.folks),
      ', '.join(cs_r2_1.folks))

print('На районе soviet_street живут -', ', '.join(ss_r1.folks), ', '.join(ss_r2.folks), ', '.join(ss_r1_2.folks),
      ', '.join(ss_r2_2.folks))
