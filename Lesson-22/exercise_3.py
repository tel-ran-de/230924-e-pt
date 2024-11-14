# Тема: Дополнительная практика
from sys import intern

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