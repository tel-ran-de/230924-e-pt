### Тема: Рекурсия

# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:
# print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15



def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

"Пример"

print(sum_list([1, 2, 3, 4, 5])),  # 15






# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# print(is_palindrome("radar")),  # Вывод: True
# print(is_palindrome("hello")),  # Вывод:  False



def is_palindrome(s):
    s = s.replace(" ", "").lower()

    "Базовый случай: если строка пустая или состоит из одного символа"
    if len(s) <= 1:
        return True

    "совпадают ли первый и последний символ"
    if s[0] != s[-1]:
        return False

    "для подстроки без первого и последнего символа"
    return is_palindrome(s[1:-1])


"Пример"

print(is_palindrome("radar")),True
print(is_palindrome("hello")),False
print(is_palindrome("A man a plan a canal Panama")),True






# 3. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9



def find_max(lst):

    if len(lst) == 1:
        return lst[0]

    "максимальный элемент в части списка"
    max_of_rest = find_max(lst[1:])

    "первый элемент с максимальным из оставшейся части"
    return lst[0] if lst[0] > max_of_rest else max_of_rest


"Пример"

print(find_max([1, 5, 3, 9, 2])),          # 9
print(find_max([-1, -5, -3, -9, -2])),     # -1






####################################################################################################
# Тема: Дополнительная практика на рекурсию
####################################################################################################






# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# print(sum_of_digits(12345))  # Вывод: 15



def sum_of_digits(n):
    # Приводим число к положительному, если оно отрицательное
    n = abs(n)

    "если n равно 0, возвращаем 0"
    if n == 0:
        return 0

    "последнюю цифру и добавляем к сумме оставшихся цифр"
    return n % 10 + sum_of_digits(n // 10)


"Пример"

print(sum_of_digits(12345)),  # 15
print(sum_of_digits(-987)),   # 24






# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# print(reverse_string("hello"))  # Вывод: "olleh"



def reverse_string(s):
    "если строка пустая, возвращаем пустую строку"
    if s == "":
        return s

    "последний символ и добавляем его к результату реверсированной подстроки"
    return s[-1] + reverse_string(s[:-1])


"Пример"

print(reverse_string("hello")),   # "olleh"
print(reverse_string("Python")),  # "nohtyP"







# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5])) # Вывод: 5



def list_length(lst):
    "если список пустой, длина равна 0"
    if not lst:
        return 0

    " 1 (текущий элемент) + длина оставшейся части списка"
    return 1 + list_length(lst[1:])


"Пример"

print(list_length([1, 2, 3, 4, 5])),   # 5
print(list_length([])),                # 0





###################################################################################################
# Тема: Дополнительная практика на функции
###################################################################################################




# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24




def multiply_all(*args):
    product = 1

    for num in args:
        product *= num
    return product


"Пример"

print(multiply_all(1, 2, 3, 4)),   # 24
print(multiply_all(5, 6, 7)),     # 210
print(multiply_all()),    # 1 (пустые возвращают 1)







# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}




def merge_dicts(**kwargs):
    merged_dict = {}
    "объединённый словарь"
    for d in kwargs.values():
        merged_dict.update(d)

    return merged_dict


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dicts(dict1=dict1, dict2=dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}






# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]




def make_flatten():
    def flatten(nested_list):
        result = []

        "Рекурсивная функция"

        def flatten_helper(lst):
            for item in lst:
                if isinstance(item, list):
                    flatten_helper(item),    "обрабатываем вложенные списки"
                else:
                    result.append(item),     "Добавляем элементы в результат"

        flatten_helper(nested_list)
        return result

    return flatten


"Пример"

flatten = make_flatten()
print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]







# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1



def find_min(lst):
    if len(lst) == 1:
        return lst[0]

    min_of_rest = find_min(lst[1:])

    return lst[0] if lst[0] < min_of_rest else min_of_rest



"Пример"

print(find_min([4, 2, 8, 1, 5])),         # 1
print(find_min([-5, -2, -8, -1, -3])),    # -8







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
    print("Args:", args)
    print("Kwargs:", kwargs)

"Пример"

args = (1, 2, 3)
kwargs = {"name": "Alice", "age": 30}
show_info(*args, **kwargs)

"пример"

show_info(4, 5, name="Bob", city="New York")





################################################################################################
################################################################################################
################################################################################################