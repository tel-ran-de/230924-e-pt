# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))

# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
def combine_lists(*args):
    res_list = []
    for el in args:
        res_list= res_list+el
    return res_list

print(combine_lists([1,2], [3, 4], [5, 6]))


# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.
def print_details(name, age):
    print(f'name: {name}, age: {age}')

person = {'name': 'Alice', 'age': 32,}

print_details(**person)

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.

def filter_numbers(*args):
    res_list = []
    for element in args:
        if element > 10:
            res_list.append(element)
    return res_list

print(filter_numbers(1,11, 12, 3, 32, 5))