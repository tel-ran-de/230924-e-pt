 Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.

def division_num(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
    except TypeError:
        print("Вводите только числовые значения")
    else:
        return z
print(division_num(4, 0))
print(division_num(8, 4))
print(division_num(8, "a"))

# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.

def quetz_num():
    while True:
        try:
            user_num = int(input("Введите число: "))
            result = user_num ** 2
        except ValueError:
            print("Некорректный ввод.")
        else:
            return result
print(quetz_num())

# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.

def kind_errors():
    try:
        file = open("examples.py", "r", encoding="utf-8")
        content = file.readline()
        print(content)
        file1 = open("C:/Windows/System32/example.txt", "w", encoding="utf-8")
        file1.write("Привет от Виктора!")
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Ошибка: нет доступа к файлу")
    except IOError:
        print("Ошибка ввода-вывода")
    else:
        print('Файл обработан. Файл закрыт.')
        file.close()
    finally:
        print('Операция завершена')
kind_errors()

# Тема: Распространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.

import math

def calculate_square_root(number):
    # Добавьте проверку на отрицательное число и возбуждение исключения
    if number < 0:
        raise ValueError("Число должно быть положительным")

    return math.sqrt(number)

def safe_calculate_square_root(number):
    try:
        result = calculate_square_root(number)
        print(f"Квадратный корень из {number} равен {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
# Тесты функции
safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным


# Задача 2. Допишите код ниже.
def convert_to_number(string):
    # Добавьте проверку на некорректное значение и возбуждение исключения
    if not string.isdigit():
        raise ValueError("Введенное значение не является числом")
    return int(string)

def safe_convert_to_number(string):
    try:
        number = convert_to_number(string)
        print(f"Конвертированное число: {number}")
    except ValueError as e:
        print(f"Ошибка: {e}")
# Тесты функции
safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8, 14, добавив в него обработку ошибок, где это необходимо.
#
# Используйте файл как базу данных проекта.
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

import json
import os
from tabulate import tabulate


# Файл для хранения инвентаря
inventory_file = 'inventory.json'

# Проверка существования файла инвентаря
if not os.path.exists(inventory_file):
    inventory = [
        {'product': "Laptop", 'price': 10, 'count': 13},
        {'product': "Mouse", 'price': 50, 'count': 1},
        {'product': "Keyboard", 'price': 30, 'count': 33},
        {'product': "Monitor", 'price': 20, 'count': 10}
    ]
    with open(inventory_file, 'w', encoding='utf-8') as file:
        json.dump(inventory, file, ensure_ascii=False, indent=4)

# Загрузка инвентаря
def load_inventory():
    try:
        with open(inventory_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError: # Проверка, имеется ли файл в наличии
        print("Ошибка: Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат данных в файле.") # Проверка, в каком виде записан файл
        return []

# Сохранение инвентаря
def save_inventory(inventory):
    try:
        with open(inventory_file, 'w', encoding='utf-8') as file:
            json.dump(inventory, file, ensure_ascii=False, indent=4)
    except Exception as e: # ошибка при сохранении с указанием ее значения
        print(f"Ошибка при сохранении данных: {e}")

# Вывод инвентаря в таблице
def print_inventory():
    inventory = load_inventory()
    if not inventory:
        print("Инвентарь пуст.")
    else:
        headers = ["Название товара", "Цена", "Количество"]
        table = [[item['product'].title(), item['price'], item['count']] for item in inventory]
        print(tabulate(table, headers=headers, tablefmt="grid"))

# Добавление товара
def add_product():
    inventory = load_inventory()
    product = input("Введите название товара: ").strip()
    for item in inventory:
        if item['product'].lower() == product.lower(): # проверяем наличие товара в списке переводим в нижний регистр
            print("Товар уже существует.")
            return
    while True:
        try:
            price = int(input("Введите цену товара: "))
            count = int(input("Введите количество товара: "))
            break
        except ValueError: # исключение ввода, только числовое значение
            print("Ошибка: Цена и количество должны быть числовыми значениями.")
    inventory.append({'product': product, 'price': price, 'count': count})
    save_inventory(inventory)
    print("Товар добавлен.")

# Удаление товара
def delete_product():
    inventory = load_inventory()
    product = input("Введите название товара для удаления: ").strip()

    item_exists = any(item['product'].lower() == product.lower() for item in inventory)
    if not item_exists:
        print("Ошибка: Товар не найден. Попробуйте снова.")
        return

    inventory = [item for item in inventory if item['product'].lower() != product.lower()]
    save_inventory(inventory)
    print("Товар удалён.")

# Обновление товара
def update_product():
    inventory = load_inventory()
    product = input("Введите название товара для обновления: ").strip()

    for item in inventory:
        if item['product'].lower() == product.lower():
            while True:
                try:
                    item['price'] = int(input("Введите новую цену: "))
                    item['count'] = int(input("Введите новое количество: "))
                    break
                except ValueError:
                    print("Ошибка: Цена и количество должны быть числовыми значениями.")
            save_inventory(inventory)
            print("Товар обновлён.")
            return
    print("Товар не найден.")

# Поиск товара
def search_product():
    inventory = load_inventory()
    product = input("Введите название товара для поиска: ").strip()

    for item in inventory:
        if item['product'].lower() == product.lower():
            headers = ["Название товара", "Цена", "Количество"]
            table = [[item['product'].title(), item['price'], item['count']]]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            return
    print("Товар не найден.")

# Фильтрация по цене
def filter_by_price():
    inventory = load_inventory()
    while True:
        try:
            max_price = int(input("Введите максимальную цену: "))
            break
        except ValueError:
            print("Ошибка: Введите числовое значение для цены.")

    filtered = [item for item in inventory if item['price'] <= max_price]
    if not filtered:
        print("Нет товаров дешевле указанной цены.")
    else:
        headers = ["Название товара", "Цена", "Количество"]
        table = [[item['product'].title(), item['price'], item['count']] for item in filtered]
        print(tabulate(table, headers=headers, tablefmt="grid"))

# Фильтрация по количеству
def filter_by_count():
    inventory = load_inventory()
    while True:
        try:
            max_count = int(input("Введите максимальное количество: "))
            break
        except ValueError:
            print("Ошибка: Введите числовое значение для количества.")

    filtered = [item for item in inventory if item['count'] <= max_count]
    if not filtered:
        print("Нет товаров с количеством ниже указанного.")
    else:
        headers = ["Название товара", "Цена", "Количество"]
        table = [[item['product'].title(), item['price'], item['count']] for item in filtered]
        print(tabulate(table, headers=headers, tablefmt="grid"))

# Меню программы
def menu():
    while True:
        print("\nМеню:")
        print("1. Показать список товаров")
        print("2. Добавить товар")
        print("3. Удалить товар")
        print("4. Обновить товар")
        print("5. Найти товар по названию")
        print("6. Показать товары с ценой ниже заданной")
        print("7. Показать товары с количеством ниже заданного")
        print("0. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            print_inventory()
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            search_product()
        elif choice == '6':
            filter_by_price()
        elif choice == '7':
            filter_by_count()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск программы
menu()







