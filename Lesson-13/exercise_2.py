# Задача 1: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
<<<<<<< HEAD
def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(keys,values))
=======
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
>>>>>>> abb1210aa612fd57ba605d8fec7f203be4ab3ead
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
<<<<<<< HEAD
def count_characters(string):
    my_set = set(string)
    my_dict = {}
    def counting(char, m_string):
        res = sum(1 for c in m_string if c == char)
        my_dict[char] = res
    for char in my_set:
        counting(char,string)
    return my_dict
string = "hello world"
print(count_characters(string))

=======
# string = "hello world"
>>>>>>> abb1210aa612fd57ba605d8fec7f203be4ab3ead
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

<<<<<<< HEAD
=======
def sum_positive_negative(*args):

    pos_sum = sum(i for i in args if i > 0)
    neg_sum = sum(i for i in args if i < 0)

    return pos_sum, neg_sum

print(sum_positive_negative(1, -2, 3, -4, 5))
>>>>>>> abb1210aa612fd57ba605d8fec7f203be4ab3ead

# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York
