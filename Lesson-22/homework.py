# Тема: map, filter, zip
from curses.ascii import isdigit
from tkinter.font import names

# Задача 1: Применение функции map для преобразования чисел
# Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
## def square(x):
#     return x * x
#
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# print(squared_numbers)
# print(list(squared_numbers))

# Ожидаемый результат: [1, 4, 9, 16, 25]


# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#

# Ожидаемый результат: [2, 4, 6, 8, 10]
# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(is_even, numbers)
# print(even_numbers)
# print(list(even_numbers))

# Задача 3: Применение функции zip для объединения списков
# У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# и выведите результат.
#
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# print(list(zip(names,ages)))
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]


# Задача 4: Применение функции map для преобразования строк в числа
# Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# и выведите результат.
# def to_int(x):
#     return  int(x)
# str_numbers = ["1", "2", "3", "4", "5"]
# print(list(map(to_int,str_numbers)))
# Ожидаемый результат: [1, 2, 3, 4, 5]


# Задача 5: Применение функции filter для отбора слов длиннее 4 символов
# Напишите функцию `longer_than_four`, которая принимает строку и возвращает `True`,
# если длина строки больше 4 символов, и `False` в противном случае. Используйте функцию `filter`,
# чтобы отобрать слова длиной больше 4 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
# def longer_than_four(x):
#     return len(x) > 4
# words = ["apple", "kiwi", "banana", "pear"]
# print(list(filter(longer_than_four,words)))


# Ожидаемый результат: ["apple", "banana"]


# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# def numb_generator():
#     for i in range(1,21):
#         yield i
# print(list(filter(lambda x:x % 2 == 0,numb_generator())))

# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
# numbers = (i for i in range(1,6))
# squar_numb = (i*i for i in range(1,6))
# print(list(map(lambda x : f"{x[0]}:{x[1]}",(zip(numbers,squar_numb)))))

# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
# def file_reader(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line.strip()
#
# filter_lines = filter(lambda  line : "Python",file_reader("text_files/example.txt"))
# for line in filter_lines:
#     print(line)
# Тема: Дополнительная практика

# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]
# def temp_generator():
#     for x in range(-10,11):
#         yield x
# print(list(map(lambda x : (x * 9/5)+32,temp_generator())))

# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']

# list_wort=["hello", "world", "python", "is", "awesome"]
# wort_list = iter(list_wort)
# print(list(filter(lambda x : len(x) > 5,wort_list)))
# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']

# def num_gen():
#     for i in range(1,4):
#         yield i
# def cub_gen():
#     for i in range(1,4):
#         yield i **3
# print(list(map(lambda x : f"{x[0]}:{x[1]}",(zip(num_gen(),cub_gen())))))
# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.
# def file_reader(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line.strip()
#
#
# file_path = "text_files/data.txt"
# lines_generator = file_reader(file_path)
# filtered_lines = filter(lambda line: any(char.isdigit() for char in line), lines_generator)
# mapped_lines = map(lambda line: int(line), filtered_lines)
# print(list(mapped_lines))


# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".

def read_file_lines(file_path):

    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file1_path = 'file1.txt'
file2_path = 'file2.txt'

file1_lines = read_file_lines(file1_path)
file2_lines = read_file_lines(file2_path)

combined_lines = zip(file1_lines, file2_lines)

formatted_lines = map(lambda pair: f"{pair[0]} - {pair[1]}", combined_lines)

for line in formatted_lines:
    print(line)