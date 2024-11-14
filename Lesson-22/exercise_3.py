# Тема: Дополнительная практика

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


string_iterator = iter(["hello", "world", "python", "is", "awesome"])

print(list(filter(lambda s: len(s) > 5, string_iterator)))

# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']
# Генератор для чисел от 1 до 3
def number_generator():
    for i in range(1, 4):
        yield i

def cube_generator():
    for i in range(1, 4):
        yield i ** 3

combined = list(zip(number_generator(), cube_generator()))
print(combined)

formatted_result = list(map(lambda x: f"{x[0]}: {x[1]}", combined))
print(formatted_result)


# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.


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
