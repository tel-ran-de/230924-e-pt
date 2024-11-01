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
    def wrapper(*args, **kwargs):
        # Шаг 3. Проверка аргументов
        if all(isinstance(arg, (int, float)) and arg > 0 for arg in args):
            return func(*args, **kwargs)
        else:
            return "Ошибка: все аргументы должны быть положительными числами"
    return wrapper
@validate
def add(a, b):
    return a + b

# Тестовые вызовы
print(add(5, 3))  # Ожидаемый результат: 8
print(add(-1, 3))  # Ожидаемый результат: "Ошибка: все аргументы должны быть положительными числами"


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
    cache_dict = {}  # Словарь для хранения результатов

    def wrapper(*args):
        # Проверяем, есть ли результат в кэше для данных аргументов
        if args in cache_dict:
            print(f"Использование кеша для аргументов {args}")
            return cache_dict[args]

# Если результата нет в кэше, вызываем функцию и сохраняем результат
        result = func(*args)
        cache_dict[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Тестирование функции с использованием кеша
print(fibonacci(10))  # Вывод: 55
print(fibonacci(10))  # Вывод: 55 (использует кеш)


# Дополнительная практика

# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
#
# authenticated = False
#
# @requires_auth
# def secret_function():
#     print("Секретная информация")
#
# secret_function()
# Вывод: Доступ запрещен: пользователь не аутентифицирован
#
# authenticated = True
# secret_function()
# Вывод: Секретная информация
# Глобальная переменная для проверки аутентификации
authenticated = False

# Декоратор для проверки флага аутентификации
def requires_auth(func):
    def wrapper(*args, **kwargs):
        # Проверяем, установлен ли флаг authenticated в True
        if authenticated:
            return func(*args, **kwargs)
        else:
            return "Доступ запрещен: пользователь не аутентифицирован"
    return wrapper

@requires_auth
def secret_function():
    print("Секретная информация")

# Тестовые вызовы
print(secret_function())  # Ожидаемый вывод: Доступ запрещен: пользователь не аутентифицирован

authenticated = True
print(secret_function())  # Ожидаемый вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
#
# @call_counter
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Алиса")
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
# greet("Боб")
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!


# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА
def call_counter(func):
    # Счетчик вызовов, создается при каждом новом декорировании функции
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count  # Указываем, что мы будем изменять внешнюю переменную count
        count += 1  # Увеличиваем счетчик при каждом вызове функции
        print(f"Функция {func.__name__} вызвана {count} раз(а)")
        return func(*args, **kwargs)  # Вызываем оригинальную функцию

    return wrapper

@call_counter
def greet(name):
    print(f"Привет, {name}!")

# Тестовые вызовы
greet("Алиса")  # Ожидаемый вывод: Функция greet вызвана 1 раз(а)
# Привет, Алиса!

greet("Боб")    # Ожидаемый вывод: Функция greet вызвана 2 раз(а)
# Привет, Боб!

def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        if isinstance(result, str):     # Проверяем, что результат строка
            return result.upper()       # Преобразуем результат в верхний регистр
        return result                   # Возвращаем как есть, если не строка

    return wrapper

@to_upper
def get_greeting(name):
    return f"Привет, {name}"

# Тестовый вызов
print(get_greeting("Алиса"))  # Ожидаемый вывод: ПРИВЕТ, АЛИСА


# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
# @limit_calls(3)
# def say_hello(name):
#     print(f"Привет, {name}!")
#
# say_hello("Алиса")
# # Вывод: Привет, Алиса!
# say_hello("Боб")
# # Вывод: Привет, Боб!
# say_hello("Чарли")
# # Вывод: Привет, Чарли!
# say_hello("Дейв")
# # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз
def limit_calls(max_calls):
    # Декоратор принимает параметр max_calls для ограничения количества вызовов
    def decorator(func):
        count = 0  # Счетчик вызовов функции

        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:  # Проверяем, меньше ли текущий счетчик max_calls
                count += 1
                return func(*args, **kwargs)  # Вызываем функцию, если лимит не превышен
            else:
                print(f"Ошибка: функция {func.__name__} может быть вызвана не более {max_calls} раз")

        return wrapper

    return decorator

# Пример использования
@limit_calls(3)
def say_hello(name):
    print(f"Привет, {name}!")

# Тестовые вызовы
say_hello("Алиса")  # Вывод: Привет, Алиса!
say_hello("Боб")    # Вывод: Привет, Боб!
say_hello("Чарли")  # Вывод: Привет, Чарли!
say_hello("Дейв")   # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз
