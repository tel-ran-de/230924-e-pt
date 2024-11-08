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
        # Проверяем, являются ли все аргументы положительными числами
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                print("Ошибка: все аргументы должны быть положительными числами")
                return None

        return func(*args, **kwargs)

    return wrapper


@validate
def add(a, b):
    return a + b


"Примеры"

print(add(5, 3))  # Вывод: 8
print(add(-1, 3))  # Вывод: Ошибка: все аргументы должны быть положительными числами
print(add(2, -4))  # Вывод: Ошибка: все аргументы должны быть положительными числами
print(add(1.5, 2.5))  # Вывод: 4.0







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
    results = {}  # Словарь для хранения результатов

    def wrapper(*args):
        if args in results:
            return results[args]  # Возвращаем сохранённый результат
        result = func(*args)  # Вызываем оригинальную функцию
        results[args] = result  # Сохраняем результат
        return result

    return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)# Примеры использования



print(fibonacci(10))  #  55
print(fibonacci(10))  #  55 (использует кеш)
print(fibonacci(5))   #  5





####################################################################################
# Дополнительная практика
###################################################################################





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
    def wrapper(*args, **kwargs):
        if not authenticated:
            print("Доступ запрещен: пользователь не аутентифицирован")
            return
        return func(*args, **kwargs)  # Вызываем оригинальную функцию, если аутентифицирован
    return wrapper

@requires_auth
def secret_function():
    print("Секретная информация")


"Пример"

secret_function()  # Вывод: Доступ запрещен: пользователь не аутентифицирован

# Меняем флаг на True
authenticated = True
secret_function()  # Вывод: Секретная информация







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




def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count  # Используем nonlocal для изменения переменной count из внешней функции
        count += 1
        print(f"Функция {func.__name__} вызвана {count} раз(а)")
        return func(*args, **kwargs)

    return wrapper

@call_counter
def greet(name):
    print(f"Привет, {name}!")


"Пример"

greet("Алиса")

#  greet вызвана 1 раз(а)
# "Привет, Алиса!"

greet("Боб")

#  greet вызвана 2 раз(а)
# "Привет, Боб!"






# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА




def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        return result.upper()  # Преобразуем результат в верхний регистр
    return wrapper

@to_upper
def get_greeting(name):
    return f"Привет, {name}"


"Пример"

print(get_greeting("Алиса")),    #  "ПРИВЕТ, АЛИСА"
print(get_greeting("Боб")),      #  "ПРИВЕТ, БОБ"






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
    def decorator(func):
        count = 0  # Переменная для отслеживания количества вызовов

        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:
                count += 1
                return func(*args, **kwargs)  # Вызываем оригинальную функцию
            else:
                print(f"Ошибка: функция {func.__name__} может быть вызвана не более {max_calls} раз")
                return None

        return wrapper
    return decorator

@limit_calls(3)
def say_hello(name):
    print(f"Привет, {name}!")

"Пример"

say_hello("Алиса"),   "Привет, Алиса!"
say_hello("Боб"),     "Привет, Боб!"
say_hello("Чарли"),   "Привет, Чарли!"
say_hello("Дейв"),    "Ошибка: функция say_hello может быть вызвана не более 3 раз"




################################################################################################
################################################################################################
################################################################################################
