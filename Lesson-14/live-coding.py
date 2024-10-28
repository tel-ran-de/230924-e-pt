# Продемонстрируйте и объясните в режиме live-coding:
# - Упаковку аргументов с args для списков и кортежей
# - Упаковку аргументов с kwargs для словарей
# - Распаковку с операторами * и **

print('# - Упаковку аргументов с args для списков и кортежей')
# def sum_squares(a, b, c, d):
#     return a*a + b*b + c*c + d*c
#
# def sum_squares_args(*args):
#     print(type(args))
#     return sum([i ** 2 for i in args])
#
# print(sum_squares_args(1, 2, 3, 10, 11, 12, -2, 11))  # Вывод: 504


# Упаковка именованных аргументов с **kwargs
print('# Упаковка именованных аргументов с **kwargs')
def show_info(**kwargs):
    separator = '\n'
    if 'separator' in kwargs:
        separator = kwargs.get('separator')
        del kwargs['separator']
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=separator)

show_info(name="Alice", age=30, separator=' - ')
# name: Alice
# age: 30
print()
print()
show_info(name="Alice", age=30, city='New York', salary=5000)
# name: Alice
# age: 30
# city: New York
# salary: 5000

# - Распаковка с операторами * и **
print()
print('# - Распаковка с операторами * и **')
l1 = [1, 2, True, 'value', 17, 9]
x, y, *z = l1
print(x)
print(y)
print(z)

print()
*x, y, z = l1
print(x)
print(y)
print(z)

print()
x, *y, z = l1
print(x)
print(y)
print(z)

print()
print(*l1, sep=' - ')


# Распаковка словаря с помощью **
print('# Распаковка словаря с помощью **')
data = {"name": "Bob", "age": 25}
def print_info(name, age):
    return f"Name: {name}, Age: {age}"

print(print_info(**data))
# Вывод: Name: Bob, Age: 25










# Продемонстрируйте в режиме live-coding и объясните работу:
# - Глобальных и локальных переменных
# - Ключевых слов global и nonlocal
# В- ложенных функций
# - Замыкания

