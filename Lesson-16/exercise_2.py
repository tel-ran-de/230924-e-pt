# Дополнительная практика
from zoneinfo import reset_tzpath


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.


def requires_auth(func):

    def wrapper(*args,**kwargs):

        if not authenticated :
           print( "Доступ запрещен: пользователь не аутентифицирован")
        else:
            return func(*args,**kwargs)
    return wrapper



authenticated = True

@requires_auth
def secret_function():
    print("Секретная информация")

secret_function()
# Вывод: Доступ запрещен: пользователь не аутентифицирован
#
# authenticated = True
# secret_function(authenticated)
# Вывод: Секретная информация


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


