### Тема: Рекурсия

# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:
# print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15

print('Тема: Рекурсия. Задача 1.')
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))



# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False
print('Тема: Рекурсия. Задача 2.')
def is_palindrome(s):
   if not s:
       return True
   elif s[0] != s[-1]:
       return False
   else:
       is_palindrome(s[1:-1])
   return True
print(is_palindrome("radar"))
print(is_palindrome("hello"))

def ispalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return ispalindrome(s[1:-1])

# 3. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9
print('Тема: Рекурсия. Задача 3.')
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] > lst[-1]:
            lst = lst[:-1]
        else:
            lst = lst[1:]
    return find_max(lst)

print(find_max([1, 5, 3, 9, 2]))

def findmax(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        maxrest = findmax(lst[1:])
        return lst[0] if lst[0] > maxrest else maxrest

# Тема: Дополнительная практика на рекурсию
print('Тема: Дополнительная практика на рекурсию. Задача 1.')

# Тема: Дополнительная практика на рекурсию
# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# print(sum_of_digits(12345))  # Вывод: 15

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(123456))

# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# print(reverse_string("hello"))  # Вывод: "olleh"
print('Тема: Дополнительная практика на рекурсию. Задача 2.')
def reverse_string(s):
    if not s:
        return ''
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5
print('Тема: Дополнительная практика на рекурсию. Задача 3.')
def list_length(lst):
    if not lst:
        return 0
    else:
        return 1 + list_length(lst[1:])

print(list_length([1, 2, 3, 4, 5]))


# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24
print('Тема: Дополнительная практика на функции. Задача 1.')
def multiply_all(*args):
    if len(args) == 0:
        return 1
    else:
        return args[0] * multiply_all(*args[1:])

print(multiply_all(1, 2, 3, 4))

# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('Тема: Дополнительная практика на функции. Задача 2.')
def merge_dicts(**kwargs):
        return dict(zip(kwargs.keys(), kwargs.values()))

def mergedicts(**kwargs):
    return {key: value for key, value in kwargs.items()}

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print(merge_dicts(**dict1, **dict2))

# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]
print('Тема: Дополнительная практика на функции. Задача 3.')
def flatten(lst):
    flatten_list = []
    for item in lst:
        if isinstance(item, list):
            flatten_list.extend(flatten(item))
        else:
            flatten_list.append(item)
    return flatten_list

print(flatten([1, [2, [3, 4], 5], 6]))

# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1
print('Тема: Дополнительная практика на функции. Задача 4.')
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] < lst[-1]:
            lst = lst[:-1]
        else:
            lst = lst[1:]
    return find_min(lst)

print(find_min([4, 2, 8, 1, 5]))

# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
# args = (1, 2, 3)
# kwargs = {"name": "Alice", "age": 30}
# show_info(*args, **kwargs)
print('Тема: Дополнительная практика на функции. Задача 5.')
def show_info(*args, **kwargs):
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')

args = (1, 2, 3)
kwargs = {"name": "Alice", "age": 30}
show_info(*args, **kwargs)

# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}