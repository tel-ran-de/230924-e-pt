# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
def numbers_iterator(n):
    for i in range(1, n + 1):
        yield i

try:
    numbers_it = numbers_iterator(7)
    while True:
        print(next(numbers_it))
except StopIteration:
    print("Итератор завершил работу.")
print('================================')
# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
squares = (x ** 2 for x in range(11))

try:
    for square in squares:
        print(square)
except StopIteration:
    print("Итератор завершил работу.")
print('================================')
# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
def words_generator(sentence):
    words = sentence.split()
    for word in words:
        yield word

try:
    sentence = ("This is a test file.")
    gen_sentence = words_generator(sentence)
    while True:
        print(next(gen_sentence))
except StopIteration:
    print("Итератор завершил работу.")

print('================================')

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def num_generator():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i * 2
        else:
            yield i

result_num = set(num_generator())
print(result_num)
print('================================')
# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
def num_generator():
    for i in range(1, 21):
        if i % 3 == 0:
            yield i


result_num = sum(num_generator())
print(result_num)
print('================================')
# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
def word_len(sentence):
    for word in sentence.split():
        yield len(word)

sentence = "Write a generator that returns word lengths from a given sentence"
min_len_word = min(word_len(sentence))
max_len_word = max(word_len(sentence))

print(f"Минимальная длина слова: {min_len_word}")
print(f"Максимальная длина слова: {max_len_word}")
print('================================')
# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
def filter_lines(file_path, word):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if word.lower() in line.lower():
                yield line.strip()

x_word = 'this'
file_path = 'text_files\data.txt'
for f_lines in filter_lines(file_path, x_word):
    print(f"Строка: {f_lines} содержащие слово: {x_word}")
print('================================')
# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
def read_file_in_chunks(file_path, chunk_size):
    with open(file_path) as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def line_gen_for_chunk(file_path, chunk_size):
    buffer = ""
    for chunk in read_file_in_chunks(file_path, chunk_size):
        chunk = buffer + chunk
        lines = chunk.split("\n")
        buffer = lines.pop()
        yield len(lines)
    if buffer:
        yield 1

file_path = 'text_files\data.txt'
chunk_size = 50

for part_number, line_count in enumerate(line_gen_for_chunk(file_path, chunk_size), start=1):
    print(f"Количество строк в части {part_number}: {line_count}")

print('================================')
# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
def lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def num_in_lines(file_path):
    for line in lines_generator(file_path):
        for char in line:
            if char.isdigit():
                yield line

file_path = 'text_files\data.txt'

numbered_lines = list(num_in_lines(file_path))
for line in numbered_lines:
    print(f"Строка: {line} содержит числа.")