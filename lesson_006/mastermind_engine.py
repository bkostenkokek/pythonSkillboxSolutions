import random
import string

# def given_number():
#     result = []
#     result.append(random.randrange(1, 10))
#     for i in range(3):
#         result.append(random.randrange(0, 10))
#     return result
#
# given_number()

def given_number():
    result = str(random.randrange(999, 10000))
    print(result)
    return str(result)


def read_number():
    result = ''
    while len(result) != 4:
        print('Enter number: ')
        result = input()
    return result


def count_bulls(result, given, read):
    for i in range(4):
        if given[i] == read[i]:
            result['bulls'] += 1


def count_cows(result, given, read):
    for i in range(4):
        for j in range(4):
            if i != j and given[i] == read[j]:
                result['cows'] += 1


def check_number(given, read):
    result = {'bulls': 0, 'cows': 0}
    count_bulls(result, given, read)
    count_cows(result, given, read)
    return result

