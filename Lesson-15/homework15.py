### Тема: Рекурсия
from functools import total_ordering


# 1. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# def is_palindrome(s):
#     if len(s)<=1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False

# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False


# 2. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9
# lst=[]
# def find_max(*lst):
#     res = lst[0]
#     for i in lst[1:]:
#         if i > res:
#             res = i
#     return res
#
# print(find_max(1, 5, 3, 9, 2))

# 3. Напишите функцию `find_min`, которая возвращает минимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1

# lst=[]
# def find_min(lst):
#     res = lst[0]
#     for i in lst[1:]:
#         if i < res:
#             res = i
#     return res
#
# print(find_min([4, 2, 8, 1, 5]))

# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_of_digits(n // 10)
# print(sum_of_digits(12345))  # Вывод: 15


# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:])+s[0]
# print(reverse_string("hello"))  # Вывод: "olleh"


# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# def list_length(lst):
#     if lst == []:
#         return 0
#     else:
#         return 1+ list_length(lst[1:])
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5


# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# def multiply_all(*args):
#     total_num= 1
#     for num in args:
#         total_num *= num
#     return total_num
#
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24


# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]


# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1


# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
# args = (1, 2, 3)
# kwargs = {"name": "Alice", "age": 30}
# show_info(*args, **kwargs)
# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
