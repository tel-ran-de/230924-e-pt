# Тема: map, filter, zip

# Задача 1: Применение функции map для преобразования чисел
# Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
square_number = map(square, numbers)
print(list(square_number))
# Ожидаемый результат: [1, 4, 9, 16, 25]
print('================================')

# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))
# Ожидаемый результат: [2, 4, 6, 8, 10]
print('================================')

# Задача 3: Применение функции zip для объединения списков
# У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# и выведите результат.
#

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combo = zip(names, ages)
print(list(combo))
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
print('================================')

# Задача 4: Применение функции map для преобразования строк в числа
# Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# и выведите результат.
#
def to_int(x):
    return int(x)
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = map(int, str_numbers)
print(list(int_numbers))
# Ожидаемый результат: [1, 2, 3, 4, 5]
print('================================')

# Задача 5: Применение функции filter для отбора слов длиннее 4 символов
# Напишите функцию `longer_than_four`, которая принимает строку и возвращает `True`,
# если длина строки больше 4 символов, и `False` в противном случае. Используйте функцию `filter`,
# чтобы отобрать слова длиной больше 4 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
#
def longer_than_four(word):
    return len(word) > 4
words = ["apple", "kiwi", "banana", "pear"]
filtered_words = list(filter(longer_than_four, words))
print(filtered_words)
# Ожидаемый результат: ["apple", "banana"]
print('================================')

# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numbers = (x for x in range(1, 21))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
print('================================')
# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
numbers = iter(range(1, 6))
squares = iter(x ** 2 for x in range(1, 6))

zipp_number = zip(numbers, squares)
formatted_output = list(map(lambda pair: f"{pair[0]}: {pair[1]}", zipp_number))
print(formatted_output)
print('================================')
# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

file_path = "text_files/example.txt"
filtered_lines = filter(lambda line: "Python" in line, read_lines(file_path))
filtered_uppercase = map(lambda line: line.upper(), filtered_lines)

result = list(filtered_uppercase)
print(result)
print('================================')
# Тема: Дополнительная практика

# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]
def celsius_generator():
    for celsius in range(-10, 11):
        yield celsius

celsius_temps = celsius_generator()
fahrenheit_temps = map(lambda c: c * 9 / 5 + 32, celsius_temps)
print(list(fahrenheit_temps))
print('================================')
# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']
strings = ["hello", "world", "python", "is", "awesome"]

filtered_strings = filter(lambda s: len(s) > 5, strings)

print(list(filtered_strings))
print('================================')
# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']
def numbers_generator():
    for i in range(1, 4):
        yield i

def cubes_generator():
    for i in range(1, 4):
        yield i ** 3

numbers = numbers_generator()
cubes = cubes_generator()
zipp_data = zip(numbers, cubes)

format_data = map(lambda x: f"{x[0]}: {x[1]}", zipp_data)
print(list(format_data))
print('================================')
# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.
def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def contains_digit(line):
    for char in line:
        return char.isdigit()


file_path = 'text_files/data.txt'
lines = read_file_lines(file_path)

filtered_lines = filter(contains_digit, lines)

numbers = list(map(lambda line: int(''.join(filter(lambda char: char.isdigit(), line))), filtered_lines))
print(numbers)
print('================================')
# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".
def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file1_path = 'text_files/file1.txt'
file2_path = 'text_files/file2.txt'

file1_lines = read_lines_from_file(file1_path)
file2_lines = read_lines_from_file(file2_path)

zipped_lines = zip(file1_lines, file2_lines)

formatted_lines = map(lambda x: f"{x[0]} - {x[1]}", zipped_lines)

for line in formatted_lines:
    print(line)
