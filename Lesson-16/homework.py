# Тема: Декораторы

# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
#
def validate(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                print('Ошибка: все аргументы должны быть положительными числами')
                return f'{arg} отрицательное число!'
        return func(*args)
    return wrapper


@validate
def add(a, b):
    return a + b
#
print(add(5, 3))
# Вывод: 8
#
print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами
print('===============================================')

# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
def cache(func):
    cache_dick = {}
    def wrapper(*args):
        if args in cache_dick:
            return cache_dick[args]
        result = func(*args)
        cache_dick[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
#
print(fibonacci(10))
# # Вывод: 55
#
print(fibonacci(10))
# # Вывод: 55 (использует кеш)

print('===============================================')
# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
#
authenticated = False


def requires_auth(func):
    def wrapper(*args, **kwargs):
        if not authenticated:
            print('Доступ запрещен: пользователь не аутентифицирован')
            return
        return func(*args, **kwargs)
    return wrapper()


@requires_auth
def secret_function():
    print("Секретная информация")

#secret_function()
# Вывод: Доступ запрещен: пользователь не аутентифицирован
#
#authenticated = True
#secret_function()
# Вывод: Секретная информация
print('===============================================')

# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
#
def call_counter(funk):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {funk.__name__} вызвана {count} раз')
        return funk(*args, **kwargs)
    return wrapper


@call_counter
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
greet("Боб")
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!
greet("Aleksej")
print('===============================================')
# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
def to_upper(func):
    def wrapper(*args, **kwargs):
        upper_args = func(*args, **kwargs)
        if isinstance(upper_args, str):
            return upper_args.upper()
    return wrapper


@to_upper
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА
print('===============================================')

# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
def limit_calls(max_calls):
    def limit_calls(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_calls:
                print(f'Вывод: Ошибка: функция {func.__name__} может быть вызвана не более {max_calls}')
                return
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return limit_calls



@limit_calls(3)
def say_hello(name):
     print(f"Привет, {name}!")
#
say_hello("Алиса")
# # Вывод: Привет, Алиса!
say_hello("Боб")
# # Вывод: Привет, Боб!
say_hello("Чарли")
# # Вывод: Привет, Чарли!
say_hello("Дейв")
# # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз
