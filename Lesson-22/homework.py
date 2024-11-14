# Тема: map, filter, zip
print("---------------Тема: map, filter, zip-----------------")
# Задача 1: Применение функции map для преобразования чисел
# Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5]
# Ожидаемый результат: [1, 4, 9, 16, 25]
def square(num):
    return num ** 2
numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))

# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: [2, 4, 6, 8, 10]
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(is_even, numbers)))

# Задача 3: Применение функции zip для объединения списков
# У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# и выведите результат.
#
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
print(list(zip(names, ages)))

# Задача 4: Применение функции map для преобразования строк в числа
# Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# и выведите результат.
#
# str_numbers = ["1", "2", "3", "4", "5"]
# Ожидаемый результат: [1, 2, 3, 4, 5]
def to_int(string):
    return int(string)

str_numbers = ["1", "2", "3", "4", "5"]
print(list(map(to_int, str_numbers)))

# Задача 5: Применение функции filter для отбора слов длиннее 4 символов
# Напишите функцию `longer_than_four`, которая принимает строку и возвращает `True`,
# если длина строки больше 4 символов, и `False` в противном случае. Используйте функцию `filter`,
# чтобы отобрать слова длиной больше 4 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
#
# words = ["apple", "kiwi", "banana", "pear"]
# Ожидаемый результат: ["apple", "banana"]
def longer_than_four(word):
    return len(word) > 4

words = ["apple", "kiwi", "banana", "pear"]
print(list(filter(longer_than_four, words)))

# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями
print("--Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями---")
# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def number_generator():
    for i in range(1, 21):
        yield i

print(list(filter(lambda x: x % 2 == 0, number_generator())))

# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
numbers = (i for i in range(1, 6))
squares = (i ** 2 for i in range(1, 6))

combined = list(zip(numbers, squares))
print(list(map(lambda x: f"{x[0]}: {x[1]}", combined)))

# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

filtered_lines = filter(lambda line: "Python" in line, read_file_lines("text_files/example.txt"))
uppercased_lines = map(lambda line: line.upper(), filtered_lines)

for line in uppercased_lines:
    print(line)

# Тема: Дополнительная практика
print("---------------------------------Задача 1-------------------------------------")
# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]
def temperature_generator():
    for temp in range(-10, 11):
        yield temp

celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(list(map(celsius_to_fahrenheit, temperature_generator())))

# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']
print("---------------------------------Задача 2-------------------------------------")
string_iterator = iter(["hello", "world", "python", "is", "awesome"])
print(list(filter(lambda s: len(s) > 5, string_iterator)))

# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']
print("---------------------------------Задача 3-------------------------------------")
def number_generator():
    for i in range(1, 4):
        yield i

def cube_generator():
    for i in range(1, 4):
        yield i ** 3

combined = list(zip(number_generator(), cube_generator()))
formatted_result = list(map(lambda x: f"{x[0]}: {x[1]}", combined))
print(formatted_result)

# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.
print("---------------------------------Задача 4-------------------------------------")
def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

filter_lines = filter(lambda line: any(char.isdigit() for char in line), read_file("text_files/data.txt"))
convert_num = map(lambda line: int(line), filter_lines)

for number in convert_num:
    print(number)

# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".
print("---------------------------------Задача 5-------------------------------------")
def read_file1(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def read_file2(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

main_lines = zip(read_file1("text_files/file1.txt.txt"), read_file2("text_files/file2.txt"))
format_result = list(map(lambda x: f"{x[0]} - {x[1]}", main_lines))

for line in format_result:
    print(line)