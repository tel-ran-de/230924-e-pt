# Тема: map, filter, zip

# Задача 1: Применение функции map для преобразования чисел
# Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5]
# Ожидаемый результат: [1, 4, 9, 16, 25]
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
square_number = map(square, numbers)
print(list(square_number))
# Ожидаемый результат: [1, 4, 9, 16, 25]


# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: [2, 4, 6, 8, 10]
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# Задача 3: Применение функции zip для объединения списков
# У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# и выведите результат.
#
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combo = zip(names, ages)
print(list(combo))

# Задача 4: Применение функции map для преобразования строк в числа
# Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# и выведите результат.
#
# str_numbers = ["1", "2", "3", "4", "5"]
# Ожидаемый результат: [1, 2, 3, 4, 5]
def to_int(x):
    return int(x)
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = map(int, str_numbers)
print(list(int_numbers))

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

word_filter = filter(longer_than_four, words)
print(list(word_filter))

# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numbers = filter(lambda x: x % 2 == 0, (x for x in range(1,21)))
print(list(numbers))

# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
numbers = iter(range(1,6))
squared_numbers = iter(i ** 2 for i in range(1,6))
zip_number = zip(numbers, squared_numbers)

format_number = list(map(lambda i: f"{i[0]}: {i[1]}", zip_number))
print(format_number)


# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
file_path = "text_files/example.txt"
lines = file_reader(file_path)
filtered_lines = filter(lambda line: 'Python' in line, lines)
upper_lines = map(lambda line: line.upper(), filtered_lines)
print(list(upper_lines))

# Тема: Дополнительная практика

# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]
temperatur = (temp for temp in range(-10, 11))
far_temp = list(map(lambda c: c * 9/5 + 32, temperatur))
print(far_temp)

# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']
iters_words = iter(["hello", "world", "python", "is", "awesome"])
filter_words = list(filter(lambda word: len(word) > 5, iters_words))
print(filter_words)

# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']
numbers = (x for x in range(1,4))
squared_numbers = (i ** 3 for i in range(1,4))
zip_number = zip(numbers, squared_numbers)

format_number = list(map(lambda i: f"{i[0]}: {i[1]}", zip_number))
print(format_number)

# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
file_path = "text_files/data.txt"
lines = file_reader(file_path)
filtered_lines = filter(lambda line: any([char.isdigit()  for char in line]), lines)
integers = map(int, filtered_lines)
print(list(integers))

# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".
gen1 = file_reader("text_files/file1.txt")
gen2 = file_reader("text_files/file2.txt")

lins_list = list(zip(gen1, gen2))
map_list = map(lambda x: f"{x[0]}-{x[1]}", lins_list)
print(list(map_list))
