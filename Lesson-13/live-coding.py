# Тема: функции
#
# Покажите в формате live-coding и объясните:
# - Процесс создания и вызова функции.
# - Использование оператора return для возврата значения из функции.
# - Использования именованных аргументов, что делает вызов функции более гибким.

# функция print() ничего не возвращает, она просто печатает значения в консоль
# это значит, что в этой функции нет оператора return
# print('Hello world!')
# x = print('Hello world!')
# print(x)
print('# Объявление и вызов функций')


def greet(name):
    print(f'Hello, {name}')


greet('Alice')  # Hello, Alice
greet(name='Bob')  # Hello, Bob
n = greet('Hanna')  # Hello, Hanna
print(n)  # None


print('\n# оператор return')


def add(a, b):
    return a + b


add_2_3 = add(a=2, b=3)
print(add_2_3)  # 5

add_3_5 = add(a=3, b=5)
print(add_3_5)  # 8


print('\n# параметры по умолчанию')


def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}')


greet('Boris')  # Hello, Boris
greet('Boris', 'Hi')  # Hi, Boris


print('\n# возврат нескольких значений из функции')


def get_square_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube


square_7, cube_7 = get_square_cube(x=7)
print(square_7)  # 49
print(cube_7)  # 343


# Тема: args, kwargs
#
# Покажите в формате live-coding и объясните:
# - Как работать с произвольным числом параметров с помощью args и *kwargs.
