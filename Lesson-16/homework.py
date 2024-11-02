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
                return ""
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
print(fibonacci(10))

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
authenticated = False

def requires_auth(func):
    def decorator(*args, **kwargs):
        if authenticated:
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен: пользователь не аутентифицирован")

    return decorator

@requires_auth
def secret_function():
    print("Секретная информация")

secret_function()

authenticated = True
secret_function()


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
def call_counter(func):
    def decorator(*args, **kwargs):
        decorator.call_count += 1
        print(f"Функция {func.__name__} вызвана {decorator.call_count} раз(а).")
        return func(*args, **kwargs)

    decorator.call_count = 0
    return decorator


@call_counter
def greet(name):
    print(f"Привет, {name}!")
#
greet("Алиса")
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
greet("Боб")
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!
greet("Игорь")


# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА
def to_upper(func):
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return decorator

@to_upper
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алиса"))

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
def limit_calls(max_call):
    def decorator(func):
        i = 0
        def wrapper(*args, **kwargs):
            nonlocal  i
            if i < max_call:
                i += 1

                return func (*args, **kwargs)

            else:
                print(f"Ошибка. Количество вызовов не может быть больше {max_call}-х.")

        return wrapper
    return decorator
@limit_calls(3)
def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Алиса")
# Вывод: Привет, Алиса!
say_hello("Боб")
# Вывод: Привет, Боб!
say_hello("Чарли")
# Вывод: Привет, Чарли!
say_hello("Дейв")
# Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз