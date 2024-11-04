# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#from hashlib import algorithms_available
print("------------------------Задача 1: Анализ чисел.----------------------------------")
def analyze_numbers(numbers):
    sum_numbers = sum(numbers)
    average_num = sum_numbers / len(numbers)
    count_of_even = sum(1 for num in numbers if num % 2 ==0)
    return sum_numbers, average_num, count_of_even
numbers = [1, 2, 3, 4, 5, 6]
print(analyze_numbers(numbers))

# Вывод функции: (21, 3.5, 3)
# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
print("------------------------Задача 2: Работа со строками.----------------------------")
def analyze_strings(strings):
    long_str = max(strings, key=len)
    short_str = min(strings, key=len)
    count_str_with_a = sum(1 for string in strings if 'a' in string)
    return long_str, short_str, count_str_with_a
strings = ["apple", "banana", "cherry", "date"]
print(analyze_strings(strings))
# Вывод функции: ('banana', 'date', 3)


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
print("------------------------Задача 3: Обработка словаря сотрудников.-----------------")
def analyze_salaries(employees):
    average_salary = sum(employees.values()) / len(employees)
    max_salary = max(employees.values())
    max_salary_employee = max(employees, key=employees.get)
    return average_salary, max_salary, max_salary_employee
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
print(analyze_salaries(employees))
# Вывод функции: (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
print("------------------------Задача 4: Фильтрация списка.-----------------------------")
def filter_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_numbers(numbers))
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
print("------------------------Задача 5: Генерация словаря.-----------------------------")
def create_dict(keys, values):
    return dict(zip(keys, values))
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(keys, values))
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print("------------------------Задача 6: Подсчет символов в строке.---------------------")
def count_characters(string):
    return {char: string.count(char) for char in string}
string = "Hellooh Worldd"
print(count_characters(string.lower()))


# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)
print("------------------------Задача 7: Обработка произвольного числа аргументов.------")
def sum_positive_negative(*args):
    pos_sum = sum(num for num in args if num > 0)
    neg_sum = sum(num for num in args if num < 0)
    return pos_sum, neg_sum

print(sum_positive_negative(17, -8, 3, -4, 11))
# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York
print("------------------------Задача 8: Генерация строки из именованных аргументов.----")
def generate_string(**kwargs):
    separation = ' | '
    return separation.join(f"{key}={value}" for key, value in kwargs.items())
print(generate_string(name="Alice", age=30, city="New York"))

print("------------------------Управление инвентарем в интернет-магазине.---------------")
# Проект: Перепишите проект из урока 7 в функциональном стиле.
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определенной стоимости.
# 7. Вывести список товаров меньше определенного количества.

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]


def check_input(product, product_list=inventory):
    product_name_list = [item['product'].lower() for item in product_list]
    if product.lower() not in product_name_list:
        print(f'Продукт: {product} - отсутствует в списке продуктов')
        result = False
    else:
        result = True
    return result


def print_products(product_list = inventory):
    print("---------------------------")
    columns = list(product_list[0].keys())
    print('|', end='')
    for item in columns:
        print(f' {item} ', end='|')
    print()
    print("---------------------------")
    for product in product_list:
        vals = list(product.items())
        print('|', end='')
        for val in vals:
            print(f' {val[1]:{len(val[0]) + 1}}', end='|')
        print()
        print("---------------------------")


def add_product(product_list = inventory):
    new_product = input("Введите название товара: ")
    if not check_input(new_product, product_list):
        np_price = int(input("Введите цену товара: "))
        np_count = int(input("Введите количество товара: "))
        product_list.append({'product': new_product,
                             'price': np_price,
                             'count': np_count
                             })
    else:
        print(f'Товар есть в списке.')
    print_products(product_list)


def delete_product(product_list=inventory):
    product_to_delete = input('Введите наименование, удаляемого товара: ')
    if check_input(product_to_delete, product_list):
        for item in product_list:
            if item['product'] == product_to_delete:
                product_list.remove(item)
        print(f'Продукт: {product_to_delete} - удален из списка товаров.')
    else:
        print(f'Удалить можно товар из списка.')
    print_products(product_list)


def update_product(product_list = inventory):
    product_to_update = input("Введите название обновляемого товара: ")
    if check_input(product_to_update, product_list):
        article_to_update = input(f'Если хотите обновить название продукта выберите 1\n'
                                  f'Если хотите обновить цену продукта выберите 2\n'
                                  f'Если хотите обновить количество продукта выберите 3: \n')
        if article_to_update == '1':
            new_product = input("Введите новое название товара: ")
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['product'] = new_product.title()
                    print_products([item])
            print(f'Название продукта "{product_to_update}" изменено на "{new_product}" ')
        elif article_to_update == '2':
            new_price = int(input("Введите новую цену товара: "))
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['price'] = new_price
                    print_products([item])
            print(f'Новая цена продукта: {product_to_update} изменена на {new_price} ')
        elif article_to_update == '3':
            new_count = int(input("Введите новое количество товара: "))
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['count'] = new_count
                    print_products([item])
            print(f'Новое количество продукта: {product_to_update} изменена на {new_count} ')
        else:
            print("Выбор действия неверен.")
    else:
        print(f'Обновлять можно только продукт из списка товаров.')
    print_products(product_list)


def find_product_name(product_list = inventory):
    product_to_search = input("Введите название товара: ")
    if check_input(product_to_search, product_list):
        print_products([product_to_search])
    else:
        print("Запрашиваемый товар не найден.")


def find_product_price(product_list = inventory):
    max_price = int(input("Введите максимальную цену товара: "))
    search_list = []
    for item in product_list:
        if item['price'] <= max_price:
            search_list.append(item)
    print("-------------------------------------------------")
    print(f'Товары с ценой меньшей или равной - {max_price}:')
    print_products(search_list)


def find_product_count(product_list = inventory):
    max_count = int(input("Введите максимальное количество товара: "))
    search_list = []
    for item in product_list:
        if item['count'] <= max_count:
            search_list.append(item)
    print(f'Товары количеством меньшим или равным {max_count}:')
    print_products(search_list)

while True:
    print("     М Е Н Ю:")
    print("---------------------------------------------------------------------------------")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить название товара, стоимость или количество.")
    print("5. Найти товар по названию.")
    print("6. Вывести список товаров меньше определённой стоимости.")
    print("7. Вывести список товаров меньше определенного количества.")
    print("0. Выйти из программы.")
    print("---------------------------------------------------------------------------------")
    choice = input("Выберите действие: ")

    if choice == '1':
        print_products()
    elif choice == '2':
        add_product()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        find_product_name()
    elif choice == '6':
        find_product_price()
    elif choice == '7':
        find_product_count()
    elif choice == '0':
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод. Выберите действие от 1 до 7 из меню.")
        print("---------------------------------------------------------------------------------")