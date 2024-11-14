# Тема: Дополнительная практика
# from curses.ascii import isdigit


# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]
def temp_gen():
    for x in range(-10, 11):
        yield x

print(list(map(lambda x: (x * 9/5) + 32, temp_gen())))


# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']

list_wort = ["hello", "world", "python", "is", "awesome"]
wort_list = iter(list_wort)
print(list(filter(lambda x: len(x) > 5, wort_list)))


# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']
def numbers_gen():
    for i in range (1, 4):
        yield i

def cube_num():
    for i in range (1, 4):
        yield i ** 3

print(list(map(lambda x: f"{x[0]}: {x[1]}", (zip(numbers_gen(), cube_num())))))


# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.

def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# def sim_string():
#     for char in line:
#         return char.isdigit()

filter_lines = filter(lambda line: any(char.isdigit() for char in line), file_reader("text_files/data.txt"))
int_lines = map(lambda line: int(line), filter_lines)
for line in filter_lines:
    print(line)

# filter_lines = filter(lambda line: any(char.isdigit() for char in line), file_reader("text_files\data.txt"))
# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".
def file_1(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def file_2(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

date_file = zip(file_1("text_files/file1.txt"), file_2("text_files/file2.txt"))

result = list(map(lambda x: f"{x[0]} - {x[1]}", date_file))

for line in result:
    print(line)