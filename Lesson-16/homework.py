# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
print('Тема: Декораторы. Задача 1')
def validate(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                return 'Ошибка: все аргументы должны быть положительными числами'
        return func(*args, **kwargs)

    return wrapper


#
@validate
def add(a, b):
     return a + b

print(add(5, 3))
# Вывод: 8
#
print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
print('Тема: Декораторы. Задача 2')


def cache(func):
  cache_box = {}
  def wrapper(*args):
    if args in cache_box:
        print(f'{cache_box[args]}  используется кэш')
        return cache_box[args]
    else:
      result = func(*args)
      cache_box[args] = result
      print(f'{result}   вычисляется')
      return result
  return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
         return n
    return fibonacci(n - 1) + fibonacci(n - 2)
#

fibonacci(10)
# # Вывод: 55
print()
fibonacci(10)
# # Вывод: 55 (использует кеш)




# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
print('Тема2: Задача 1')

def requires_auth(func):
    def wrapper(*args, **kwargs):
        if not authenticated:
            print(f'Доступ запрещен: пользователь не аутентифицирован')
        else:
            return func(*args, **kwargs)
    return wrapper



#
@requires_auth
def secret_function():
     print("Секретная информация")
#
authenticated = False
secret_function()
#Вывод: Доступ запрещен: пользователь не аутентифицирован
#
authenticated = True
secret_function()
# Вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
#
print('Тема: 2. Задача 2')
def call_counter(func, counter = 0):
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f'Функция {func.__name__} вызвана {counter} раз(а)')
        return func(*args, **kwargs)
    return wrapper

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

print('Тема: 3. Задача 1')
# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
def to_upper(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return wrapper

@to_upper
def get_greeting(name):
     return f"Привет, {name}"
#
print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА

print('Тема: 3. Задача 2')
# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
def limit_calls(number):
    def limit_calls_decorator(func, counter = 0):
        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            if counter > number:
               print(f'Ошибка: функция {func.__name__} может быть вызвана не более {number} раз')
            else:
                return func(*args, **kwargs)
        return wrapper
    return limit_calls_decorator

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
