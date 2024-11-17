# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
def nam_iterator(n):
    return iter(range(1, n + 1))
try:
    iterator = nam_iterator(5)
    while True:
        print(next(iterator))
except StopIteration:
    print("finisch")

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
squares = (x * x for x in range(11))

# Обработка исключения StopIteration
while True:
    try:
        print(next(squares))
    except StopIteration:
        print("Итерация завершена")
        break

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
def word_generator(sentence):
    words = sentence.split()
    for word in words:
        yield word


sentence = "Это пример предложения для генератора"
gen_words = word_generator(sentence)

while True:
    try:
        print(next(gen_words))
    except StopIteration:
        print("Итерация завершена")
        break


# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def wort_generator():
    for num in range(1, 11):
        if num % 2 == 0:
            yield num * 2
        else:
            yield  num
result_set = set(wort_generator())
print(result_set)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
def wort_generator():
    for num in range(1, 21):
        if num % 3 == 0:
            yield num

result_set = sum(wort_generator())
print(result_set)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
def words_generator(sentence):
    for word in sentence.split():
        yield len(word)
sentence = "Write a generator that returns word lengths from a given sentence"
lengs = words_generator(sentence)
word_max = max(lengs)
word_min = min(words_generator(sentence))

print(word_min)
print(word_max)

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
def filter_lines_by_keyword(file_name, x_word):
    x_word = x_word.lower()
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if x_word in line.lower():
                    yield line.strip()
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден!")
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")


file_name = 'text_files/data.txt'
x_word = 'Some'

for line in filter_lines_by_keyword(file_name, x_word):
    print(line)


# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
def read_file(file_path, chunk_size):
    with open(file_path, 'r', encoding="utf-8") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk
def count_lines_in_chunk(chunk):
    return chunk.count('\n')

file_path = 'text_files/data.txt'
chunk_size = 80
# Использование генератора
chunk_generator = read_file(file_path, chunk_size)

for chunk in chunk_generator:
    line_count = count_lines_in_chunk(chunk)
print(f"Часть: {chunk}")
print(f"Количество строк в части: {line_count}")


# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
def contains_digit(s):
    for char in s:
        if char.isdigit():
            return True
    return False

def filter_lines_with_numbers(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if contains_digit(line):
                    yield line.strip()
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден!")
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")


file_name = 'text_files/data.txt'

for line in filter_lines_with_numbers(file_name):
    print(line)
