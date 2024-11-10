### Тема: Рекурсия
from xml.sax.saxutils import escape


# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:
# print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15
print("------------------------------Рекурсия. Задание 1.---------------------------")
def sum_list(lst):
    if not lst:
        return 0
    else:
        result = lst[0] + sum_list(lst[1:])
    return result
print(sum_list([1, 2, 3, 4, 5]))

# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False
print("------------------------------Рекурсия. Задание 2.---------------------------")
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1: -1])

print(is_palindrome("radar"))  # Вывод: True
print(is_palindrome("hello"))  # Вывод: False
print(is_palindrome("raddar"))
print(is_palindrome("raaddar"))
# 3. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))

print(find_max([16, 5, 3, 9, 21]))

# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# print(sum_of_digits(12345))  # Вывод: 15
print("------------------------------Рекурсия. Доп. задание 1.---------------------------")
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(12345))

# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# print(reverse_string("hello"))  # Вывод: "olleh"
print("------------------------------Рекурсия. Доп. задание 2.---------------------------")
def reverse_string(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello"))

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5
print("------------------------------Рекурсия. Доп. задание 3.---------------------------")
def list_length(lst):
    if not lst:
        return 0
    else:
        return 1 + list_length(lst[1:])
print(list_length([1, 2, 3, 4, 5, 6, 7, 8]))

# Тема: Дополнительная практика на функции
print("------------------------------Функции. Доп. задание 1.---------------------------")
# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24
def multiply_all(*args):
    count_num = 1
    for num in args:
        count_num *= num
    return count_num
print(multiply_all(1, 2, 3, 4))

# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("------------------------------Функции. Доп. задание 2.---------------------------")
def merge_dicts(**kwargs):
    all_dict = {}
    for key, value in kwargs.items():
        all_dict[key] = value
    return all_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dicts(**dict1, **dict2))

# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]
print("------------------------------Функции. Доп. задание 3.---------------------------")
def make_flatten():
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result
    return flatten

flatten = make_flatten()
print(flatten([1, [2, [3, 4], 5], 6]))   # Вывод: [1, 2, 3, 4, 5, 6]

# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1
print("------------------------------Функции. Доп. задание 4.---------------------------")
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], find_min(lst[1:]))
print(find_min([4, 2, 8, 7, 5]))

# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
# args = (1, 2, 3)
# kwargs = {"name": "Alice", "age": 30}
# show_info(*args, **kwargs)
# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
print("------------------------------Функции. Доп. задание 5.---------------------------")
def show_info(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

args = (1, 2, 3)
kwargs = {"name": "Alice", "age": 30}
show_info(*args, **kwargs)
