# Дополнительная практика
from itertools import count
from pstats import count_calls

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
# Вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
def call_counter(count_call):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if decorator != 0:
                count += 1
                print(f"Функция {func.__name__} вызвана {count} раз")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@call_counter(count)
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



