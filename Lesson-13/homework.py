# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
def analyze_numbers(numbers):
    sum_numbers = sum(numbers)
    average_numbers = sum(numbers) / len(numbers)
    even_numbers = sum(1 for i in numbers if i % 2 == 0)
    return sum_numbers, average_numbers, even_numbers

numbers = [1, 2, 3, 4, 5, 6]
print(analyze_numbers(numbers))
# Вывод функции: (21, 3.5, 3)


# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..

def analyze_strings(strings):
    long_str = max(strings, key=len)
    short_str = min(strings, key=len)
    count_str = sum(1 for i in strings if 'a' in i)
    return long_str, short_str, count_str

strings = ["apple", "banana", "cherry", "date"]
print(analyze_strings(strings))
# Вывод функции: ('banana', 'date', 3)


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.

def analyze_salaries(employees):
    salaries = list(employees.values())
    average_salary = sum(salaries) / len(employees)
    max_salary = max(salaries)
    max_name_employer_salary = max(employees, key=employees.get)

    return average_salary, max_salary, max_name_employer_salary

employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
print(analyze_salaries(employees))
# Вывод функции: (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
def filter_numbers(numbers):
    even_num = [num for num in numbers if num % 2 ==0]
    odd_num = [num for num in numbers if num % 2 != 0]
    return even_num, odd_num
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_numbers(numbers))
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
def create_dict(keys, values):
    return dict(zip(keys, values))
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(keys, values))
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
def count_characters(string):
    return {char: string.count(char) for char in string}

string = 'My name is Aleksej'
print(count_characters(string))
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print('=======================================')

# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
def sum_positive_negative(*args):
    positive_nums = 0
    negative_nums = 0
    for num in args:
            if num >= 0:
                positive_nums += num
            else:
                negative_nums += num
    return positive_nums, negative_nums


result = sum_positive_negative(1, -2, 3, -4, 5)
print(result)
# Вывод функции: (9, -6)
print('=======================================')

# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
def generate_string(**kwargs):
    return ', '.join(f'{key}={value}' for key , value in kwargs.items())

print(generate_string(name="Alice", age=30, city="New York"))

# Вывод функции: name=Alice, age=30, city=New York
print('=======================================')

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
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]

inventory = [
     {'product': "Laptop", 'price': 10, 'count': 13},
     {'product': "Mouse", 'price': 50, 'count': 1},
     {'product': "Keyboard", 'price': 30, 'count': 33},
     {'product': "Monitor", 'price': 20, 'count': 10}
 ]
def show_inventory():
    print('\nСписок товаров:')
    for item in inventory:
        print(f'Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}')

def add_item():
    product_name = input('Введите название товара: ')
    price_item = input('Введите цену: ')
    count_item = input('введите количество:')
    inventory.append({'product': product_name, 'price': price_item, 'count': count_item})
    print(f'product: {product_name}, price: {price_item}, count: {count_item} добавлен в список товаров.')

def delete_items():
    delete_item = input('Какой товар вы хотите удалить: ')
    for item in inventory:
        if item['product'] == delete_item:
            inventory.remove(item)
            print(f'product: {delete_item} удален!')
            return
    print('Продукт не найден.')

def update_item():
    name_item = input('Введите название товара для обновления: ')
    for item in inventory:
        if item['product'] == name_item:
            items = input("Что вы хотите обновить: product, price, count ")
            if items == 'product':
                item['product'] = input('Введите новое название товара; ')
            elif items == 'price':
                item['price'] = float(input('Введите новую цену товара: '))
            elif items == 'count':
                item['count'] = int(input('Введите новое количество товара: '))
                break
            else:
                 print('Продукт не найден.')

def find_item():
    name_item = input('Введите название товара для поиска: ')
    for item in inventory:
        if item['product'] == name_item:
            print(f'Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}')
            break
    else:
        print('Продукт не найден.')

def below_price():
    below_item_price = float(input('Введите определенную стоимость: '))
    print(f'\nТовары меньше {below_item_price} стоимости:')
    for item in inventory:
        if item['price'] < below_item_price:
            print(f'Товар: {item['product']}')

def below_count():
    below_item_count = int(input('Введите определенное количество: '))
    print(f'\nТовары меньше количества {below_item_count}')
    for item in inventory:
        if item['count'] < below_item_count:
            print(f'Товар: {item['product']}')


while True:
    print('\nМеню:')
    print('1. Показать список товаров.')
    print('2. Добавить товар.')
    print('3. Удалить товар.')
    print('4. Обновить название товара, стоимость или количество.')
    print('5. Найти товар по названию.')
    print('6. Вывести список товаров меньше определенной стоимости.')
    print('7. Вывести список товаров меньше определенного количества.')
    print('8. Выйти.')

    choice = input('Выберите действие: ')
    if choice == '1':
        show_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        delete_items()
    elif choice == '4':
        update_item()
    elif choice == '5':
        find_item()
    elif choice == '6':
        below_price()
    elif choice == '7':
        below_count()
    elif choice == '8':
        print('Программа завершена')
        break
    else:
        print('Неверный набор.')
