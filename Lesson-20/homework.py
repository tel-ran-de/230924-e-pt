# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
print('Task(1)================================')
def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return f'На ноль делить нельзя'
    except TypeError:
        return 'ввод не числовых значений'
    except ValueError:
        return 'ввод не числовых значений'
    else:
        return result


print(divide_numbers(1, 0))
print(divide_numbers(1, '0'))
print(divide_numbers(1, None))
print(divide_numbers(100, 10))
print('Task(2)================================')
# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.
def square_numbers():
    try:
        number = float(input('Введите число: '))
        result = number ** 2
    except ValueError:
        return 'Введённое значение не является числом!'
    else:
        return f'Квадрат числа {number} равен {result}'

print(square_numbers())
print('Task(3)================================')
# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
print('Task(1)-lesson 19================================')

try:
    with open('text_files/data.txt', 'r') as file:
        result_1 = file.read()
        print(result_1)

    with open('text_files/data.txt', 'r') as file:
        result_2 = file.read(10)
        print(result_2)

    with open('text_files/data.txt', 'r') as file:
        result_3 = file.readline()
        print(result_3)


    with open('text_files/data.txt', 'r') as file:
        result_4 = file.readlines()
        print(result_4)

except FileNotFoundError:
    print("Файл 'data.txt' не найден!")
except PermissionError:
    print("Нет доступу к файлу 'data.txt'")
except IOError:
    print("Ошибка ввода-вывода")


# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
print('Task(2)-lesson 19================================')
try:
    with open('text_files/output.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.writelines(["This is line 1\n", "This is line 2\n"])
        file.close()
        file = open('text_files/output.txt', 'r')
        result = file.read()
        print(result)

except FileNotFoundError:
    print("Файл 'data.txt' не найден!")
except PermissionError:
    print("Нет доступу к файлу 'data.txt'")
except IOError:
    print("Ошибка ввода-вывода")

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
print('Task(3)-lesson 19================================')
try:
    with open('text_files/log.txt', 'a') as file:
        file.write("New log entry\n")
        file.writelines(["Log entry 1\n", "Log entry 2\n"])
        file.close()
        file = open('text_files/log.txt', 'r')
        result = file.read()
        print(result)

except FileNotFoundError:
    print("Файл 'data.txt' не найден!")
except PermissionError:
    print("Нет доступу к файлу 'data.txt'")
except IOError:
    print("Ошибка ввода-вывода")

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
print('Task(4)-lesson 19================================')
try:
    with open('text_files/pointer_example.txt', 'w+') as file:
        file.write("Python File Handling\n")
        file.seek(0)
        result = file.readline()
        print(result)
        file.seek(7)
        result_1 = file.read(5)
        print(result_1)
        file.seek(0, 2)
        file.write("End of file\n")
        file.seek(0)
        result_2 = file.read()
        print(result_2)

except FileNotFoundError:
    print("Файл 'data.txt' не найден!")
except PermissionError:
    print("Нет доступу к файлу 'data.txt'")
except IOError:
    print("Ошибка ввода-вывода")

# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError('Число должно быть не отрицательным!')
    # Добавьте проверку на отрицательное число и возбуждение исключения

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
    if not string.isdigit():
        raise ValueError ('Ведённое значение не является числом')
    # Добавьте проверку на некорректное значение и возбуждение исключения

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

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = []
    return inventory


def save_inventory(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)

def show_inventory():
    inventory = load_inventory()
    print('\nСписок товаров:')
    for item in inventory:
        print(f'Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}')

def add_item():
    inventory = load_inventory()
    product_name = input('Введите название товара: ')
    price_item = input('Введите цену: ')
    count_item = input('Введите количество: ')
    inventory.append({'product': product_name, 'price': price_item, 'count': count_item})
    save_inventory(inventory)
    print(f'product: {product_name}, price: {price_item}, count: {count_item} добавлен в список товаров.')

def delete_items():
    inventory = load_inventory()
    delete_item = input('Какой товар вы хотите удалить: ')
    for item in inventory:
        if item['product'] == delete_item:
            inventory.remove(item)
            save_inventory(inventory)
            print(f'product: {delete_item} удален!')
            return
    print('Продукт не найден.')

def update_item():
    inventory = load_inventory()
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
            else:
                print('Продукт не найден.')
            save_inventory(inventory)
            return

def find_item():
    inventory = load_inventory()
    name_item = input('Введите название товара для поиска: ')
    for item in inventory:
        if item['product'] == name_item:
            print(f'Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}')
            return
    else:
        print('Продукт не найден.')

def below_price():
    inventory = load_inventory()
    below_item_price = float(input('Введите определенную стоимость: '))
    print(f'\nТовары меньше {below_item_price} стоимости:')
    for item in inventory:
        if item['price'] < below_item_price:
            print(f'Товар: {item['product']}')

def below_count():
    inventory = load_inventory()
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







