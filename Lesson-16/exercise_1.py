# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
#
# @validate
# def add(a, b):
#     return a + b
#
# print(add(5, 3))
# Вывод: 8
#
# print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами

def validate(func):
    def decorator(*args):
        for arg in args:
            if arg <= 0:
                print(f"Аргумент {arg} должен быть положительным")
                return None
        return func(*args)
    return decorator

@validate
def add(a, b):
    return a + b

print(add(5, 3))
print(add(-1, 3))

# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.

# @cache
# def fibonacci(n):
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(10))
# # Вывод: 55
#
# print(fibonacci(10))
# # Вывод: 55 (использует кеш)

def cache(func):
    dic = {}
    def decorator(*args):
        if args in dic:
            return dic[args]
        result = func(*args)
        dic[args] = result
        return result

    return decorator

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
