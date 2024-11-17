# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы
import re
# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
# def number_generator(n):
#     numb =1
#     while numb <= n:
#         yield numb
#         numb +=1
# try:
#     gen = number_generator(5)
#     while True:
#         print(next(gen))
# except StopIteration:
#     print("Итерация завершена")

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration

# squer_gen = (i*i for i in range(11))
# try:
#     for i in squer_gen:
#         print(i)
# except StopIteration:
#      print("Итерация завершена")



# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
# def word_gen(text):
#     words = text.split()
#     for word in words:
#         yield word
# try:
#     text = "Hello Python this is Yuliia"
#     gen = word_gen(text)
#     while True:
#         word = next(gen)
#         print(word)
# except  StopIteration:
#     print("Все слова были возвращены.")



# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
#
# def number_generator(n):
#     for i in range(1,n+1):
#      if i%2 == 0:
#          i*= 2
#      yield i
# gen = number_generator(10)
# print(set(gen))
# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
# def number_generator(n):
#     for i in range(1,n+1):
#      if i%3 == 0:
#       yield i
# gen = number_generator(20)
# print(sum(gen))
# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
# def func(sentence):
#     for i in sentence.split():
#         yield len(i)
# gen = func(sentence)
# print(min(gen))
# gen = func(sentence)
# print(max(gen))

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
# def read_file(n):
#     with open(n, 'r') as file:
#         for line in file:
#             if x_word.lower() in line.lower():
#                 yield line
# n = 'text_files/data.txt'
# gen = read_file(n)
# x_word = 'this'
# for line in gen :
#     print(line)



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
# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             if re.search(r'\d', line):
#                 yield line.strip()
# file_path = 'text_files/data.txt'
# gen = read_file(file_path)
# for line in gen:
#     print(line)
