# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
print("----------Задача 1: Чтение и фильтрация строк по ключевому слову---------")
def read_files(file_path, x_word):
    with open(file_path, 'r') as file:
        for line in file:
            if x_word.lower() in line.lower():
                yield line.strip()

x_word = 'this'

try:
    generator = read_files("text_files/data.txt", x_word)
    for line in generator:
        print(line)
except StopIteration:
    print("Чтение файла завершено")




# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
print("----------Задача 2: Чтение файла по частям и подсчет строк---------")
def read_and_count_lines_in_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        remaining_data = ''

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            combined_data = remaining_data + chunk
            lines = combined_data.split('\n')
            # Все строки, кроме последней, являются полными строками
            line_count = len(lines) - 1
            # Последняя строка может быть неполной, сохраняем её для следующего чанка
            remaining_data = lines[-1]
            yield line_count
        # Добавляем последнюю строку, если она не пустая
        if remaining_data:
            yield 1
file_path = 'text_files/data.txt'
chunk_size = 50

for line_count in read_and_count_lines_in_chunks(file_path, chunk_size):
    print(f"Lines in this chunk: {line_count}")

# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
# Генератор, который читает строки из файла и возвращает только те строки, которые содержат числа
print("----------Задача 3: Поиск строк, содержащих числа---------")
def read_lines_with_numbers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if any(char.isdigit() for char in line):
                yield line.strip()

file_path = 'text_files/data.txt'

lines_with_numbers = read_lines_with_numbers(file_path)

for line in lines_with_numbers:
    print(line)
