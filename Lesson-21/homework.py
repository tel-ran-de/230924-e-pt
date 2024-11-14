# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
def number_iterator(n):
    return iter(range(1, n + 1))

try:
    iterator = number_iterator(5)
    while True:
        print(next(iterator))
except StopIteration:
    print("Итерация завершена.")

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
squares = (x ** 2 for x in range(11))

try:
    while True:
        print(next(squares))
except StopIteration:
    print("Итерация завершена.")


# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
def word_generator(sentence):
    words = sentence.split()
    for word in words:
        yield word

try:
    generator = word_generator("Это пример предложения для генератора")
    while True:
        print(next(generator))
except StopIteration:
    print("Итерация завершена.")

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def double_even_generator():
    for num in range(1, 11):
        if num % 2 == 0:
            yield num * 2
        else:
            yield num

# Преобразуем результат генератора в множество и выводим его
result_set = set(double_even_generator())
print(result_set)


# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
def multiples_of_three():
    for num in range(1, 21):
        if num % 3 == 0:
            yield num

# Используем sum() для подсчета суммы чисел, возвращаемых генератором
result = sum(multiples_of_three())
print("Сумма чисел от 1 до 20, кратных 3:", result)


# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
def word_lengths(sentence):
    for word in sentence.split():
        yield len(word)

# Заданное предложение
sentence = "Write a generator that returns word lengths from a given sentence"

# Применяем min() и max() к генератору
lengths = word_lengths(sentence)
min_length = min(lengths)
max_length = max(word_lengths(sentence))  # Повторно вызываем генератор, так как он исчерпан при первом использовании

print("Минимальная длина слова:", min_length)
print("Максимальная длина слова:", max_length)


# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
def filter_lines_by_keyword(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            # Проверяем, содержит ли строка ключевое слово, игнорируя регистр
            if keyword.lower() in line.lower():
                yield line.strip()  # Возвращаем строку без лишних пробелов и переводов строки

# Заданное ключевое слово
x_word = 'this'
filename = 'text_files/data.txt'

# Используем генератор для фильтрации строк
for line in filter_lines_by_keyword(filename, x_word):
    print(line)

# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
def count_lines_in_chunks(filename, chunk_size):
    with open(filename, 'r') as file:
        chunk = file.read(chunk_size)
        while chunk:
            # Подсчитываем количество строк в текущем фрагменте
            line_count = chunk.count('\n')
            yield line_count  # Возвращаем количество строк
            chunk = file.read(chunk_size)  # Читаем следующий фрагмент

# Задаем размер фрагмента и имя файла
filename = 'text_files/data.txt'
chunk_size = 50  # Размер фрагмента в байтах

# Используем генератор для подсчета строк в каждом фрагменте
for i, line_count in enumerate(count_lines_in_chunks(filename, chunk_size), start=1):
    print(f"Часть {i}: {line_count} строк(и)")


# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
import re

def filter_lines_with_numbers(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Проверяем, содержит ли строка хотя бы одно число
            if re.search(r'\d', line):  # \d - соответствует любому числу
                yield line.strip()  # Возвращаем строку без лишних пробелов и переводов строки

# Заданный файл
filename = 'text_files/data.txt'

# Используем генератор для фильтрации строк
for line in filter_lines_with_numbers(filename):
    print(line)
