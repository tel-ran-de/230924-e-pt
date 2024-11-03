# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
# def validate(func):
#     def wrapper(*args):
#         for i in args:
#             if i <= 0:
#                 return "Ошибка"
#         return func(*args)
#     return wrapper
#
#
#
#
# @validate
# def add(a, b):
#     return a + b
#
# print(add(3, 5))
# Вывод: 8
#
# print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
def cache(func):
    lst = {}
    def wrapper(*args):
        if args not in lst:
            print("Не использует кеш")
            lst[args]=func(*args)
        return lst [args]
    return wrapper




@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# Вывод: 55
print("---")
print(fibonacci(10))
# Вывод: 55 (использует кеш)

