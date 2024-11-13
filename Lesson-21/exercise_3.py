# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
def read_file(n):
    with open(n, 'r') as file:
        for line in file:
            if x_word.lower() in line.lower():
                yield line
n = 'text_files/data.txt'
gen = read_file(n)
x_word = 'this'
for line in gen :
    print(line)





# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
# def read_file(n,chunk_size=50):
#     with open(n, 'r') as file:
#         while True :
#             chunk = file.read(chunk_size)
#             if not chunk:
#                 break
#             line_count = chunk.count('\n')
#             yield line_count
# n = 'text_files/data.txt'
# chunk_gen = read_file(n)
# for line_count in read_file(n, chunk_size = 50):
#     print(f"Количество строк в части: {line_count}")


# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
