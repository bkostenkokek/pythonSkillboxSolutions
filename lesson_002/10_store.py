#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп
# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.


# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


# TODO здесь ваш код
Table_code = goods['Стол']
Table_item = (store[Table_code][1])
Table_quantity = Table_item['quantity']
Table_price = Table_item['price']
Table_cost = Table_quantity * lamps_price
print('Стол -', Table_quantity, 'шт, стоимость', Table_cost, 'руб')

Sofa_code = goods['Диван']
Sofa_item = store[Sofa_code][1]
Sofa_quantity = Sofa_item['quantity']
Sofa_price = Sofa_item['price']
Sofa_cost = Sofa_quantity * Sofa_price
print('Диван -', Sofa_quantity, 'шт, стоимость', Sofa_cost, 'руб')

Chair_code = goods['Стул']
Chair_item = store[Chair_code][1]
Chair_quantity = Chair_item['quantity']
Chair_price = Chair_item['price']
Chair_cost = Chair_quantity * Chair_price
print('Стул -', Chair_quantity, 'шт, стоимость', Chair_cost, 'руб')




