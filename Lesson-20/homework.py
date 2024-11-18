# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.

# РЕШЕНИЕ:

def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        return f'На ноль делить нельзя {e}'
    except TypeError as e:
        return f'Введено не число {e}'
    except ValueError as e:
        return f'Введено не число {e}'
    # except:
    #     return 'Что-то пошло не так!'
    else:
        return result


print(divide_numbers(1, 0))
print(divide_numbers(1, '0'))
print(divide_numbers(1, None))
print(divide_numbers(144, 12))

# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.

# РЕШЕНИЕ:

def get_square():
    try:
        # Запрашиваем ввод числа у пользователя
        number = float(input("Введите число: "))
        # Выводим квадрат числа
        print(f"Квадрат числа {number} равен {number ** 2}")
    except ValueError:
        # Обрабатываем случай, если ввод не является числом
        print("Ошибка: Введенное значение не является числом. Пожалуйста, попробуйте снова.")

# Запускаем функцию
get_square()


# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
# РЕШЕНИЕ:
try:
    # Открытие файла для чтения
    with open('data.txt', 'r') as file:
        # Чтение полного содержимого файла
        full_content = file.read()
        print("Полный контент файла:")
        print(full_content)
except FileNotFoundError:
    print("Ошибка: Файл 'data.txt' не найден. Проверьте, существует ли файл.")
except PermissionError:
    print("Ошибка: Нет прав для доступа к файлу 'data.txt'.")
except IOError as e:
    print(f"Ошибка ввода-вывода: {e}")

try:
    # Создание и запись данных в файл
    with open('output.txt', 'w') as file:
        file.write("Hello, World!\n")
        lines = ["This is line 1\n", "This is line 2\n"]
        file.writelines(lines)
except PermissionError:
    print("Ошибка: Нет прав для записи в файл 'output.txt'.")
except IOError as e:
    print(f"Ошибка ввода-вывода при записи в файл: {e}")

try:
    # Чтение данных из созданного файла
    with open('output.txt', 'r') as file:
        content = file.read()
        print("Содержимое файла 'output.txt':")
        print(content)
except FileNotFoundError:
    print("Ошибка: Файл 'output.txt' не найден.")
except PermissionError:
    print("Ошибка: Нет прав для доступа к файлу 'output.txt'.")
except IOError as e:
    print(f"Ошибка ввода-вывода при чтении из файла: {e}")



# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
# import math
#
# def calculate_square_root(number):
#     # Добавьте проверку на отрицательное число и возбуждение исключения
#
#     return math.sqrt(number)
#
# def safe_calculate_square_root(number):
#     try:
#         result = calculate_square_root(number)
#         print(f"Квадратный корень из {number} равен {result}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
# safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным

# РЕШЕНИЕ:

import math

def calculate_square_root(number):
    # Добавляем проверку на отрицательное число
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
#



# Задача 2. Допишите код ниже.
# def convert_to_number(string):
#     # Добавьте проверку на некорректное значение и возбуждение исключения
#
#     return int(string)
#
# def safe_convert_to_number(string):
#     try:
#         number = convert_to_number(string)
#         print(f"Конвертированное число: {number}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
# safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом

# РЕШЕНИЕ:
def convert_to_number(string):
    # Добавляем проверку на некорректное значение
    if not string.isdigit():
        raise ValueError("Введенное значение не является числом.")
    return int(string)

def safe_convert_to_number(string):
    try:
        number = convert_to_number(string)
        print(f"Конвертированное число: {number}")
    except ValueError as e:
        print(f"Ошибка: {e}")

# Тесты функции
safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом.

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

# РЕШЕНИЕ:

import json

DATABASE_FILE = "inventory.json"

# Функция для загрузки данных из файла
def load_data():
    try:
        with open(DATABASE_FILE, "r") as file:
            data = json.load(file)
            # Преобразуем список в словарь для удобства работы
            if isinstance(data, list):
                return {item["product"]: {"price": item["price"], "quantity": item["count"]} for item in data}
            elif isinstance(data, dict):
                return data
            else:
                print("Ошибка: неподдерживаемый формат данных.")
                return {}
    except FileNotFoundError:
        print("Файл базы данных не найден. Создаем новый файл.")
        return {}
    except json.JSONDecodeError:
        print("Ошибка: поврежден файл базы данных.")
        return {}

# Функция для сохранения данных в файл
def save_data(data):
    try:
        with open(DATABASE_FILE, "w") as file:
            # Преобразуем словарь обратно в список для сохранения
            json_data = [
                {"product": name, "price": details["price"], "count": details["quantity"]}
                for name, details in data.items()
            ]
            json.dump(json_data, file, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении данных: {e}")

# Функция для показа всех товаров
def show_inventory(inventory):
    print("Список товаров:")
    if not inventory:
        print("Нет товаров в инвентаре.")
        return
    for name, details in inventory.items():
        print(f"{name}: Цена - {details['price']}, Количество - {details['quantity']}")

# Функция для добавления нового товара
def add_product(inventory):
    name = input("Введите название товара: ")
    if name in inventory:
        print(f"Товар с названием '{name}' уже существует.")
        return
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    inventory[name] = {"price": price, "quantity": quantity}
    print(f"Товар '{name}' добавлен.")

# Функция для удаления товара
def remove_product(inventory):
    name = input("Введите название товара, который хотите удалить: ")
    if name not in inventory:
        print(f"Товар с названием '{name}' не найден.")
        return
    del inventory[name]
    print(f"Товар '{name}' удален.")

# Функция для обновления данных товара
def update_product(inventory):
    name = input("Введите название товара, который хотите обновить: ")
    if name not in inventory:
        print(f"Товар с названием '{name}' не найден.")
        return
    print("Что хотите обновить?")
    print("1. Цена товара")
    print("2. Количество товара")
    choice = input("Введите номер (1-2): ")
    if choice == "1":
        new_price = float(input("Введите новую цену товара: "))
        inventory[name]["price"] = new_price
        print(f"Цена товара '{name}' обновлена.")
    elif choice == "2":
        new_quantity = int(input("Введите новое количество товара: "))
        inventory[name]["quantity"] = new_quantity
        print(f"Количество товара '{name}' обновлено.")
    else:
        print("Неверный выбор.")

# Функция для поиска товара по названию
def find_product(inventory):
    name = input("Введите название товара для поиска: ")
    if name in inventory:
        details = inventory[name]
        print(f"{name}: Цена - {details['price']}, Количество - {details['quantity']}")
    else:
        print(f"Товар с названием '{name}' не найден.")

# Функция для вывода товаров ниже заданной стоимости
def show_products_below_price(inventory):
    price_limit = float(input("Введите максимальную цену: "))
    print(f"Товары с ценой ниже {price_limit}:")
    for name, details in inventory.items():
        if details["price"] < price_limit:
            print(f"{name}: Цена - {details['price']}, Количество - {details['quantity']}")

# Функция для вывода товаров с количеством ниже заданного
def show_products_below_quantity(inventory):
    quantity_limit = int(input("Введите минимальное количество: "))
    print(f"Товары с количеством меньше {quantity_limit}:")
    for name, details in inventory.items():
        if details["quantity"] < quantity_limit:
            print(f"{name}: Цена - {details['price']}, Количество - {details['quantity']}")

# Главная функция программы
def main():
    inventory = load_data()

    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров ниже заданной стоимости.")
        print("7. Вывести список товаров ниже заданного количества.")
        print("8. Выйти.")

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            remove_product(inventory)
        elif choice == "4":
            update_product(inventory)
        elif choice == "5":
            find_product(inventory)
        elif choice == "6":
            show_products_below_price(inventory)
        elif choice == "7":
            show_products_below_quantity(inventory)
        elif choice == "8":
            save_data(inventory)
            print("Изменения сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()







