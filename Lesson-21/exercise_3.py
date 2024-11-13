# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

# def read_files(file_path, x_word):
#     with open(file_path, 'r') as file:
#         for line in file:
#             if x_word.lower() in line.lower():
#                 yield line.strip()
#
# x_word = 'this'
# я
# try:
#     generator = read_files("text_files/data.txt", x_word)
#     for line in generator:
#         print(line)
# except StopIteration:
#     print("Чтение файла завершено")




# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt

def read_file_in_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def count_lines_in_chunks(file_path, chunk_size):
    for chunk in read_file_in_chunks(file_path, chunk_size):
        lines = chunk.split('\n')
        line_count = len(lines) - 1  # Учитываем, что последняя строка может быть неполной
        if chunk.endswith('\n'):
            line_count += 1
        yield line_count

file_path = 'text_files/data.txt'
chunk_size = 50

line_count_generator = count_lines_in_chunks(file_path, chunk_size)
for line_count in line_count_generator:
    print(f"Количество строк в части: {line_count}")



# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
