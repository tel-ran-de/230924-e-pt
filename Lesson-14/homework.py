# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **
from itertools import count


# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
print("-------------Задание 1.---------------")
def sum_all(*args):
    return sum(args)
print(sum_all(13, 2, 4, 5))

# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
print("-------------Задание 2.---------------")
def combine_lists(*args, **kwargs):
    return [i for j in args for i in j]
print(combine_lists([1, 2, 3],['a', 'b', 'c'],[1,'a', 4]))



# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.
print("-------------Задание 3.---------------")
def print_details(**kwargs):
    return kwargs
print(print_details(name="Viktor", age = 43))

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.
print("-------------Задание 4.---------------")
def filter_numbers(*args):
    return [i for i in args if i > 10]
print(filter_numbers(12, 10.2, 3, 17, 21))
# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.
print("-------------Глобальные и локальные переменные. Задание 1.---------------")
# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2
counter = 0
def increment_global():
    global counter
    counter += 1
    return counter
increment_global()
increment_global()
increment_global()
increment_global()
print(increment_global())
print(increment_global())
print(increment_global())
print(increment_global())


# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2
print("-------------Задание 2.---------------")
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter1 = outer()  #замыкание
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())

# 3. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15
print("-------------Задание 3.---------------")
def make_multiplier(factor):
    def multiplier(num):
        return factor*num
    return multiplier
mult_by_2 = make_multiplier(6)
print(mult_by_2(11))  # Вывод: 10
mult_by_3 = make_multiplier(10)
print(mult_by_3(45))  # Вывод: 15

# 4. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob
print("-------------Задание 4.---------------")
def make_prefixer(prefix):
    def prefixer(str):
        return prefix+str
    return prefixer
add_hello = make_prefixer("Hello, ")
print(add_hello("Alice"))
print(add_hello("Bob"))

# Тема: Дополнительная практика
print("-------------Доп. Задание 1.---------------")
# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.

def create_user(**kwargs):
    return kwargs
print(create_user(username="Nikita", email="ttt", age=30, height=100))


print("-------------Доп. Задание 2.---------------")
# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple

def make_replacer(old, new):
    def replacer(lst):
        return lst.replace(old, new)
    return replacer

replace_a_with_o = make_replacer("a", "o")
print(replace_a_with_o("baanaanaa"))  # Вывод: bonono
print(replace_a_with_o("aapplae"))   # Вывод: opple

# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!
print("-------------Доп. Задание 3.---------------")
def make_suffixer(suffix):
    def suffixer(str):
        return str + suffix
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
print("-------------Доп. Задание 4.---------------")

def make_case_changer(case):
    def case_changer(str):
        if case == "upper":
            return str.upper()
        else:
            return str.lower()
    return case_changer

to_upper = make_case_changer("upper")
print(to_upper("hellO"))  # Вывод: HELLO
to_lower = make_case_changer("lower")
print(to_lower("WORLD"))  # Вывод: world


# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor
print("-------------Доп. Задание 5.---------------")

def make_trimmer(length):
    def trimmer(str):
        return str[:length]
    return trimmer

trim_to_3 = make_trimmer(3)
print(trim_to_3("Hello"))
print(trim_to_3("World"))