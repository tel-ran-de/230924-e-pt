# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.


from itertools import count


# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)
# def analyze_numbers(numbers):
#     summ = sum(numbers)
#     alln = summ / len(numbers)
#     count_ev = []
#     for i in numbers:
#         if i % 2 == 0:
#             count_ev += [i]
#     return summ, alln, len(count_ev)
# print(analyze_numbers(numbers))

# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..

# strings = ["apple", "banana", "cherry", "date"]
# def analyze_strings(strings):
#     count_ev=[]
#     long=max[i]
#     short=min[i]
#     str=len(["a"])
#     return long, short, str
# print(analyze_strings(strings))
# Вывод функции: ('banana', 'date', 3)


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
#
# def analyze_salaries(employees):
#    midl_sal=sum(employees.values())/len(employees)
#    max_sal=max(employees.values())
#    employee_mxsl=max(employees,key=employees.get)
#    return midl_sal, max_sal, employee_mxsl
# print(analyze_salaries(employees))

# Вывод функции: (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def filter_numbers(numbers):
#     cht_numb=[num for num in numbers if num % 2 ==0 ]
#     noncht_num=[num for num in numbers if num % 2 !=0]
#     return cht_numb, noncht_num
# print(filter_numbers(numbers))
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
#
# def create_dict(keys, values):
#    return dict({keys[i]:values[i] for i in range(len(keys))})
#
# print(create_dict(keys, values))

# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# def count_characters(string):
#     return {char: string.count(char) for char in string}
# print(count_characters(string))

# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
#sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)
# def sum_positive_negative(*args):
#
#     pos_sum = sum(i for i in args if i > 0)
#     neg_sum = sum(i for i in args if i < 0)
#     return pos_sum, neg_sum
# print(sum_positive_negative(1, -2, 3, -4, 5))

# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов
# и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# def generate_string(**kwargs):
#     return ", ".join(f"{key}={value}" for key, value in kwargs.items())


# Вывод функции: name=Alice, age=30, city=New York


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
def show_inventory(inventory):
    for item in inventory:
        print(item)
def add_item(inventory, product, price, count):
    inventory.append({'product': product, 'price': price, 'count': count})
def remove_item(inventory, product):
    inventory[:] = [item for item in inventory if item['product'] != product]
def update_item(inventory, product, price=None, count=None):
    for item in inventory:
        if item['product'] == product:
            if price is not None:
                item['price'] = price
            if count is not None:
                item['count'] = count
def find_item(inventory, product):
    return [item for item in inventory if item['product'] == product]
def mx_price(inventory, max_price):
    return [item for item in inventory if item['price'] < max_price]
def mx_count(inventory, max_count):
    return [item for item in inventory if item['count'] < max_count]

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

while True:
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить название товара, стоимость или количество.")
    print("5. Найти товар по названию.")
    print("6. Вывести список товаров меньше определнной стоимости.")
    print("7. Вывести список товаров меньше определенного количества.")
    print("8. Выйти.")
    choice = input("Выберите опцию: ")
    if choice == '1':
        show_inventory(inventory)
    elif choice == '2':
        product = input("Введите название товара: ")
        price = float(input("Введите стоимость товара: "))
        count = int(input("Введите количество товара: "))
        add_item(inventory, product, price, count)
    elif choice == '3':
        product = input("Введите название товара для удаления: ")
        remove_item(inventory, product)
    elif choice == '4':
        product = input("Введите название товара для обновления: ")
        price = input("Введите новую стоимость : ")
        count = input("Введите новое количество : ")
        update_item(inventory, product, float(price) if price else None, int(count) if count else None)
    elif choice == '5':
        product = input("Введите название товара для поиска: ")
        found_items = find_item(inventory, product)
        if found_items:
            for item in found_items:
                print(item)
        else:
            print("Товар не найден.")
    elif choice == '6':
        max_price = float(input("Введите максимальную стоимость: "))
        filtered_items = mx_price(inventory, max_price)
        for item in filtered_items:
            print(item)
    elif choice == '7':
        max_count = int(input("Введите максимальное количество: "))
        filtered_items = mx_count(inventory, max_count)
        for item in filtered_items:
            print(item)
    elif choice == '8':
        break
    else:
        print("Выйти")
