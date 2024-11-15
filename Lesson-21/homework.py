# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
print("------------------Задание 1------------------------")
def create_iterator(n):
    current = 1
    while current <= n:
        yield current
        current += 1

try:
    result = create_iterator(9)
    while True:
        print(next(result))
except StopIteration:
    print("Iteration complete")

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
print("------------------Задание 2------------------------")
squares_engine = (x * x for x in range(0, 11))
try:
    for elem in squares_engine:
        print(elem)
except StopIteration:
    print("Iteration complete")

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
print("------------------Задание 3------------------------")
def sentence_engine(sentence):
    words = sentence.split()
    for word in words:
        yield word
try:
    for word1 in sentence_engine("What a sunny day innit?"):
        print(word1)
except StopIteration:
    print("Iteration complete")


# Тема: Генераторы и встроенные функции
print("-----------------Тема: Генераторы и встроенные функции. Задание 1---------------------")
# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.

def num_gen():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i * 2
        else:
            yield i
result = set(num_gen())
print("Множество чисел: ", result)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
print("------------------Задание 2------------------------")
def gen_num3():
    for i in range(1, 21):
        if i % 3 == 0:
            yield i
result_sum = sum(gen_num3())
print("Сумма чисел, кратные 3: ", result_sum)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
print("------------------Задание 3------------------------")
def word_gen(sentence):
    words = sentence.split()
    for word in words:
        yield len(word)
sentence = "Write a generator that returns word lengths from a given sentence"
word_len = list(word_gen(sentence))
min_len = min(word_len)
max_len = max(word_len)
print(min_len)
print(max_len)

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