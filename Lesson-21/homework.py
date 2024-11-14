# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration

<<<<<<< HEAD
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
=======

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
>>>>>>> bbf0bdd0267ecbf6806792698267368374953364


# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
<<<<<<< HEAD
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
=======

>>>>>>> bbf0bdd0267ecbf6806792698267368374953364

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
<<<<<<< HEAD
def generator_tusk1():
    for num in range(1, 11):
        if num % 2 == 0:
            num *= 2
        yield num

print(set(generator_tusk1()))
=======

>>>>>>> bbf0bdd0267ecbf6806792698267368374953364

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.

<<<<<<< HEAD
generator_tusk2 = (x for x in range(1, 21) if x % 3 == 0)
print(sum(generator_tusk2))
=======
>>>>>>> bbf0bdd0267ecbf6806792698267368374953364

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
<<<<<<< HEAD
sentence = "Write a generator that returns word lengths from a given sentence"
def generator_tusk3(sntence):
    for word in sntence.split():
        yield len(word)
test_list =  list(generator_tusk3(sentence))
print(max(test_list))
print(min(test_list))
=======
# sentence = "Write a generator that returns word lengths from a given sentence"
>>>>>>> bbf0bdd0267ecbf6806792698267368374953364


# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
<<<<<<< HEAD
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
=======
# Файл: data.txt

x_word = 'this'
>>>>>>> bbf0bdd0267ecbf6806792698267368374953364


# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
<<<<<<< HEAD
import os

file_stats = os.stat(FILE_PATH)

print(f'File Size in Bytes is {file_stats.st_size}')

def lines_counter(filename = FILE_PATH, chunk_size = 50):
    with open(filename, 'r') as file:
        k = 0
        while k < file_stats.st_size/chunk_size + 1:
            text = file.read(chunk_size)
            yield sum(1 for char in text if char == '\n' )+1
            k += 1
gen = lines_counter()
for i in range(10):
    try:
        print(next(gen))
    except StopIteration:
        print("Конец итерации")
=======

>>>>>>> bbf0bdd0267ecbf6806792698267368374953364

# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
<<<<<<< HEAD

def digit_finder(filename = FILE_PATH):
    with open(filename, 'r') as file:
        for line in file.readlines():
            if any([True for char in line if char.isdigit()]):
                yield line
gen = digit_finder()
for i in range(len(list(digit_finder())) + 1):
    try:
        print(next(gen))
    except StopIteration:
        print("Конец итерации")
=======
>>>>>>> bbf0bdd0267ecbf6806792698267368374953364
