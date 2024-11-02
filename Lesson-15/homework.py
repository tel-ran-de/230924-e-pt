### Тема: Рекурсия

# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:
# print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15

def sum_list(lst):
    if not lst: #если список пустой то возвращается 0, т.е. исходная точка ноль наш пустой список и  это базовый случай
        return 0
    return lst[0] + sum_list(lst[1:]) # и реверсивный случай к базе прибавляем следующий элемент по списку, к полученому + следующий и так до последнего, потом идет обратно от последнего до базы и выводю
print(sum_list([1, 2, 3, 4, 5]))

# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))  # Вывод: True
print(is_palindrome("hello"))  # Вывод: False


# 3. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:


def find_max(lst):
     if len(lst) == 1:
        return lst[0]
     sub_max = find_max(lst[1:])
     return lst[0] if lst[0] > sub_max else sub_max

print(find_max([1, 5, 8, 9, 2]))


# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:

def sum_of_digits(n):
    if n < 10:
        return n
    return n %10 + sum_of_digits(n//10)
print(sum_of_digits(12345))


# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# print(reverse_string("hello"))  # Вывод: "olleh"
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello"))

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5


# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_all(1, 2, 3, 4))


# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def merge_dicts(**kwargs):
    merged_dict = {}
    for d in kwargs.values():
        merged_dict.update(d)
    return merged_dict
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dicts(dict1=dict1, dict2=dict2))


# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]
def make_flatten():
    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list
    return flatten


flatten = make_flatten()
print(flatten([1, [2, [3, 4], 5], 6]))

# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    sub_min = find_min(lst[1:])
    return lst[0] if lst[0] < sub_min else sub_min

print(find_min([4, 2, 8, 1, 5]))

# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
# args = (1, 2, 3)
# kwargs = {"name": "Alice", "age": 30}
# show_info(*args, **kwargs)
# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}

def show_info(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

args = (1, 2, 3)
kwargs = {"name": "Alice", "age": 30}
show_info(*args, **kwargs)