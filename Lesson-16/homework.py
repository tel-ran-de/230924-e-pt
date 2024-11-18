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


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
# def cache(func):
#     cached_results = {}
#
#     def wrapper(*args, **kwargs):
#         key = (args, tuple(kwargs.items()))
#         if key in cached_results:
#             return cached_results[key]
#         result = func(*args, **kwargs)
#         cached_results[key] = result
#         return result
#
#     return wrapper
#
#
# @cache
# def fibonacci(n):
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(10))
# Вывод: 55

# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
# authenticated = False
# def requires_auth(func):
#     def wrapper(*args, **kwargs):
#         if authenticated:
#             return func(*args, **kwargs)
#         else:
#             print("Доступ запрещен: пользователь не аутентифицирован")
#     return wrapper
# @requires_auth
# def secret_function():
#     print("Секретная информация")
#
# secret_function()
# # Вывод: Доступ запрещен: пользователь не аутентифицирован
# authenticated = True
# secret_function()
# # Вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
# def call_counter(func):
#     def wrapper(*args, **kwargs):
#         wrapper.count_call += 1
#         print(f"Функция {func.__name__} вызвана {wrapper.count_call} раз(а)")
#         return func(*args, **kwargs)
#     wrapper.count_call = 0  # Инициализация счетчика вызовов
#     return wrapper
#
# @call_counter
# def greet(name):
#     print(f"Привет, {name}!")
#
# # Пример использования функции
# greet("Алиса")   # Вывод: Функция greet вызвана 1 раз(а), Привет, Алиса!
# greet("Боб")     # Вывод: Функция greet вызвана 2 раз(а), Привет, Боб!


# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
# def to_upper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.upper()
#         return result
#     return wrapper
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА


# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
# def limit_calls(max_calls):
#     def decorator(func):
#         func.calls = 0  # Инициализация счетчика вызовов функции
#
#         def wrapper(*args, **kwargs):
#             if func.calls < max_calls:
#                 func.calls += 1
#                 return func(*args, **kwargs)
#             else:
#                 print(f"Ошибка: функция {func.__name__} может быть вызвана не более {max_calls} раз")
#
#         return wrapper
#     return decorator
#
# @limit_calls(3)
# def say_hello(name):
#     print(f"Привет, {name}!")
#
# # Пример использования функции
# say_hello("Алиса")   # Вывод: Привет, Алиса!
# say_hello("Боб")     # Вывод: Привет, Боб!
# say_hello("Чарли")   # Вывод: Привет, Чарли!
# say_hello("Дейв")    # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз

