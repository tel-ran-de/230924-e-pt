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



