### Тема: Рекурсия

# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15

print('======================================')
# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
def is_palindrome(s):
    if s <= ' ':
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

print(is_palindrome("radar"))  # Вывод: True
print(is_palindrome("hello"))  # Вывод: False

print('======================================')
# 3. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = find_max(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max

print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9
print('======================================')

# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))  # Вывод: 15
print('======================================')

# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Вывод: "olleh"
print('======================================')

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
def list_length(lst):
    if lst == [ ]:
        return 0
    return 1 + list_length(lst[:-1])


print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5
print('======================================')

# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
def multiply_all(*args):
    if not args:
        return 1
    numbers = 1
    for num in args:
        numbers *= num
    return numbers

print(multiply_all(1, 2, 3, 4))  # Вывод: 24
print('======================================')

# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
def merge_dicts(**kwargs):
    all_dicts = {}
    for key, value in kwargs.items():
        all_dicts[key] = value
    return all_dicts


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('======================================')

# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
def make_flatten():
    def flatten(make_flatten):
        flat_list = []
        for num in make_flatten:
            if isinstance(num, list):
                flat_list.extend(flatten(num))
            else:
                flat_list.append(num)
        return flat_list
    return flatten

flatten = make_flatten()
print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]
print('======================================')

# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_min = find_min(lst[1:])
        return lst[0] if lst[0] < sub_min else sub_min


print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1

print('======================================')
# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
def show_info(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

args = (1, 2, 3)
kwargs = {"name": "Alice", "age": 30}
show_info(*args, **kwargs)
# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
