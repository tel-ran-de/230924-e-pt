# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
"""
def generation_n_numbers(n):
    counter = 1
    while counter <= n:
        yield counter
        counter += 1
n = 5
gen = generation_n_numbers(n)

for i in range(n+1):
    try:
        print(next(gen))
    except StopIteration:
        print('Итерация закончилась')

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
gen_squares = (x ** 2 for x in range(11))
for i in range(12):
    try:
        print(next(gen_squares))
    except StopIteration:
        print('Итерация закончилась')

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
sentence = 'Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному'
def words_generator(sent):
    for word in sent.split():
        yield word

word_gen = words_generator(sentence)
for i in range(len(sentence.split())+1):
    try:
        print(next(word_gen))
    except StopIteration:
        print('Итерация закончилась')

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def generator_tusk1():
    for num in range(1, 11):
        if num % 2 == 0:
            num *= 2
        yield num

print(set(generator_tusk1()))

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.

generator_tusk2 = (x for x in range(1, 21) if x % 3 == 0)
print(sum(generator_tusk2))

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.

sentence = "Write a generator that returns word lengths from a given sentence"
def generator_tusk3(sntence):
    for word in sntence.split():
        yield len(word)
test_list =  list(generator_tusk3(sentence))
print(max(test_list))
print(min(test_list))
# sentence = "Write a generator that returns word lengths from a given sentence"

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
FILE_PATH = 'text_files/data.txt'
x_word = 'this'
def filter_by_word(filename = FILE_PATH, filter_word = x_word):
    with open(filename, 'r') as file:
        for line in file.readlines():
            if filter_word.lower() in line.lower():
                yield line

gen =  filter_by_word()
for i in range(len(list(filter_by_word()))+1):
    try:
        print(next(gen))
    except StopIteration:
        print('Конец итерации')
# Файл: data.txt

x_word = 'this'"""

# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt

import os
from idlelib.pyshell import restart_line

FILE_PATH = 'text_files/data.txt'
file_stats = os.stat(FILE_PATH)
print(file_stats.st_size)


def lines_counter(filename = FILE_PATH, chunk_size = 60):
    with open(filename, 'r') as file:
        counter = 0
        rest_line =''
        while True:

            chunk = file.read(chunk_size)
            if not chunk:
                break
            print(chunk)
            processing_text =  rest_line + chunk
            print(processing_text)
            lines = processing_text.strip().split('\n')

            if processing_text[-1] != '\n':
                n = len(lines) -1
                counter += chunk_size - len(lines[-1])
                rest_line = lines[-1]
                yield n
                #file.seek(counter)
            else:
                n = len(lines)
                counter += chunk_size
                rest_line = ''
                yield n
                counter += chunk_size-len(lines[-1])
                #file.seek(counter)
gen = lines_counter()
for i in range(15):
    print(next(gen))
"""for item in range(len(list(lines_counter())) + 1):
    try:
        print(next(gen))
    except StopIteration:
        print("Конец итерации")"""

# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt

"""def digit_finder(filename = FILE_PATH):
    with open(filename, 'r') as file:
        for line in file.readlines():
            if any(char.isdigit() for char in line):
                yield line
gen = digit_finder()
for i in range(len(list(digit_finder())) + 1):
    try:
        print(next(gen))
    except StopIteration:
        print("Конец итерации")
"""