# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.





def divide_numbers(a, b):
    try:
        "Преобразуем в числа (если они еще не числа)"

        a = float(a)
        b = float(b)

        "Выполнение деления"
        result = a / b
        return result

    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."

    except (ValueError, TypeError):
        return "Ошибка: Введены некорректные значения. Пожалуйста, введите числа."


"Примеры использования"

print(divide_numbers(10, 2))  # Ожидаемый результат: 5.0
print(divide_numbers(10, 0))  # Ожидаемый результат: Ошибка: Деление на ноль невозможно.
print(divide_numbers('10', '5'))  # Ожидаемый результат: 2.0
print(divide_numbers('abc', 2))






# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.






# Функция для запроса ввода числа и вычисления его квадрата
def get_square():
    try:
        # Запрос ввода от пользователя
        user_input = input("Введите число: ")

        # Преобразование ввода в число
        number = float(user_input)

        # Вывод квадрата числа
        print(f"Квадрат числа {number} равен {number ** 2}")

    except ValueError:
        # Обработка исключения, если введено не число
        print("Ошибка! Введите корректное число.")


# Вызов функции
get_square()







# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.


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







import math


def calculate_square_root(number):
    # Проверка на отрицательное число
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
safe_calculate_square_root(-9)  # Ожидае







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


# Функции для работы с инвентарем

def load_inventory(filename="inventory.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Ошибка: Невозможно прочитать файл, возможно он поврежден.")
        return []


def save_inventory(inventory, filename="inventory.json"):
    try:
        with open(filename, "w") as file:
            json.dump(inventory, file, indent=4)
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


def show_inventory(inventory):
    if not inventory:
        print("Инвентарь пуст.")
        return
    for item in inventory:
        print(f"{item['product']} | Цена: {item['price']} | Количество: {item['count']}")


def add_product(inventory, product, price, count):
    if price <= 0 or count <= 0:
        raise ValueError("Цена и количество должны быть больше нуля.")

    new_product = {'product': product, 'price': price, 'count': count}
    inventory.append(new_product)
    print(f"Товар '{product}' успешно добавлен.")


def remove_product(inventory, product):
    for item in inventory:
        if item['product'] == product:
            inventory.remove(item)
            print(f"Товар '{product}' удален.")
            return
    print(f"Товар '{product}' не найден.")


def update_product(inventory, product, price=None, count=None):
    for item in inventory:
        if item['product'] == product:
            if price is not None:
                if price <= 0:
                    raise ValueError("Цена должна быть больше нуля.")
                item['price'] = price
            if count is not None:
                if count <= 0:
                    raise ValueError("Количество должно быть больше нуля.")
                item['count'] = count
            print(f"Товар '{product}' обновлен.")
            return
    print(f"Товар '{product}' не найден.")


def find_product(inventory, product):
    for item in inventory:
        if item['product'] == product:
            print(f"Найден товар: {item['product']} | Цена: {item['price']} | Количество: {item['count']}")
            return
    print(f"Товар '{product}' не найден.")


def filter_by_price(inventory, max_price):
    filtered = [item for item in inventory if item['price'] < max_price]
    if not filtered:
        print("Нет товаров с такой ценой.")
        return
    for item in filtered:
        print(f"{item['product']} | Цена: {item['price']} | Количество: {item['count']}")


def filter_by_count(inventory, max_count):
    filtered = [item for item in inventory if item['count'] < max_count]
    if not filtered:
        print("Нет товаров с таким количеством.")
        return
    for item in filtered:
        print(f"{item['product']} | Цена: {item['price']} | Количество: {item['count']}")


# Главное меню
def main():
    inventory = load_inventory()

    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров меньше определенной стоимости.")
        print("7. Вывести список товаров меньше определенного количества.")
        print("8. Выйти.")

        choice = input("Введите номер действия: ")

        try:
            if choice == "1":
                show_inventory(inventory)
            elif choice == "2":
                product = input("Введите название товара: ")
                price = int(input("Введите цену товара: "))
                count = int(input("Введите количество товара: "))
                add_product(inventory, product, price, count)
            elif choice == "3":
                product = input("Введите название товара для удаления: ")
                remove_product(inventory, product)
            elif choice == "4":
                product = input("Введите название товара для обновления: ")
                price = input("Введите новую цену товара (оставьте пустым для пропуска): ")
                count = input("Введите новое количество товара (оставьте пустым для пропуска): ")
                price = int(price) if price else None
                count = int(count) if count else None
                update_product(inventory, product, price, count)
            elif choice == "5":
                product = input("Введите название товара для поиска: ")
                find_product(inventory, product)
            elif choice == "6":
                max_price = int(input("Введите максимальную стоимость: "))
                filter_by_price(inventory, max_price)
            elif choice == "7":
                max_count = int(input("Введите максимальное количество: "))
                filter_by_count(inventory, max_count)
            elif choice == "8":
                save_inventory(inventory)
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()


#####################################################################################################
#####################################################################################################
#####################################################################################################


