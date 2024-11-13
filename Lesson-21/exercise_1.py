# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration

def create_iterator(n):
    # for i in range(1, n+1):
    #     yield i
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

squares_engine = (x * x for x in range(0, 11))
try:
    for elem in squares_engine:
        print(elem)
except StopIteration:
    print("Iteration complete")

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration

def sentence_engine(sentence):
    words = sentence.split()
    for word in words:
        yield word
try:
    for word1 in sentence_engine("What a sunny day innit?"):
        print(word1)
except StopIteration:
    print("Iteration complete")
