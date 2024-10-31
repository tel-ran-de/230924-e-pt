# Дополнительная практика
#
#
# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА
print("--------------------------------------------------------------")
def to_upper(func):
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return decorator

@to_upper
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алиса"))
print("--------------------------------------------------------------")
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
                print(f"Ошибка: функция {func.__name__} может быть вызвана не более {max_call} раз")
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