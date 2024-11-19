# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию-генератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
def number_generator(n):
    current = 1
    while current <= n:
        yield current
        current += 1
    # for i in range(1, n + 1):
    #     yield i

try:
    gen = number_generator(16)
    while True:
        print(next(gen))
except StopIteration:
    print("Итерация завершена")



# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
squares = (x * x for x in range(11))

try:
    for square in squares:
        print(square)
except StopIteration:
    print("Итерация завершена")

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration


