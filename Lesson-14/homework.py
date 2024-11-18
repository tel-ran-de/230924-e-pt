# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **
<<<<<<< HEAD
from gettext import textdomain


# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
print('Тема 1, задача 1')
def sum_all(*args):
    return sum(args)
print(sum_all(1,4,35,17))

# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
print('Тема 1, задача 2')
def combine_lists(*args):
    res_list = []
    for el in args:
       res_list += el
    return res_list

print(combine_lists([1,2], [3, 4], [5, 6]))

# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.
print('Тема 1, задача 3')
def print_details(name, age):
    print(f'name: {name}, age: {age}')

person = {'name': 'Alice', 'age': 32,}

print_details(**person)

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.
print('Тема 1, задача 4')
def filter_numbers(*args):
    return [element for element in args if element >10 ]

print(filter_numbers(1,11, 12, 3, 32, 5))

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.


# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.


# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.


# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.


# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.

# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2

print('Тема 2, задача 1')
counter = 0
def increment_global():
    global counter
    counter += 1
    return counter
increment_global()
print(counter)
increment_global()
print(counter)

print('Тема 2, задача 2')



# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter = outer()
print(counter())
print(counter())
print(counter()

# Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15

print('Тема 2, задача 3')
def make_multiplier(factor):
    def multiplier(n):
        return n * factor
    return multiplier

mult_by_2 = make_multiplier(2)
print(mult_by_2(5))  # Вывод: 10
mult_by_3 = make_multiplier(3)
print(mult_by_3(5))  # Вывод: 15


# 4. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob

print('Тема 2, задача 4')
def make_prefixer(prefix):
    def prefixer(string):
        return f'{prefix}{string}'
    return prefixer

add_hello = make_prefixer("Hello, ")
print(add_hello("Alice"))
print(add_hello("Bob"))



# Тема: Дополнительная практика

# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.

print('Тема 3, задача 1')
def create_user(username, email, **kwargs):
    kwargs['username'] = username
    kwargs['email'] = email
    return kwargs

info = {'age': 34, 'city': 'Berlin'}
print(create_user('Alice', 'alice@mail.com', **info))


# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple

print('Тема 3, задача 2')
def make_replacer(old, new):
    def replacer(text):
        return text.replace(old, new)
    return replacer
replace_a_with_o = make_replacer("a", "o")
print(replace_a_with_o("banana"))  # Вывод: bonono
print(replace_a_with_o("apple"))   # Вывод: opple


# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!

print('Тема 3, задача 3')
def make_suffixer(suffix):
    def suffixer(text):
        return text + suffix
    return suffixer
add_exclamation = make_suffixer("!")
print(add_exclamation("Hello"))  # Вывод: Hello!
print(add_exclamation("Wow"))    # Вывод: Wow!


# 4. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world

print('Тема 3, задача 4')
def make_case_changer(case):
    def case_changer(text):
        func = getattr(str, case)
        return func(text)
    return case_changer

to_upper = make_case_changer("upper")
print(to_upper("hello"))  # Вывод: HELLO
to_lower = make_case_changer("lower")
print(to_lower("WORLD"))  # Вывод: world


# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel

# print(trim_to_3("World"))  # Вывод: Wor
print('Тема 3, задача 5')
def make_trimmer(length):
    def trimmer(text):
        return text[:length]
    return trimmer
trim_to_3 = make_trimmer(3)
print(trim_to_3("Hello"))  # Вывод: Hel
print(trim_to_3("World"))  # Вывод: Wor

# print(trim_to_3("World"))  # Вывод: Wor

