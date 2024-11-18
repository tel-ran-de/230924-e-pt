import json
import os
import stat

# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('деление на ноль')
    except TypeError:
        print('ввод не числовых значений')
    else:
        print(f'result: {result}')
        return result
divide(5, '3')
divide(5, 3)
divide(5, 0)

# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.
def power_two():
    val = input("Введите число: ")
    try:
        result = float(val)**2
    except ValueError:
        print('ввод не числовых значений')
    else:
        print(f'Квадрат числа {float(val)} равен {result}')
        return result


power_two()

# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.

try:
    file = open('file.txt', 'r')
    text = file.read()
except FileNotFoundError:
    print('Вы пытаетесь открыть несуществующий файл!')
except PermissionError:
    print("У вас нет права доступа в файлу")
except IOError:
    print('Ошибка ввода/вывода')
else:
    print(text)
    file.close()

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.

os.chmod("output.txt", stat.S_ENFMT)
try:
    file = open('output.txt', 'w')
except PermissionError:
    print('Нет права доступа к файлу!')
except FileNotFoundError:
    print('Вы пытаетесь открыть несуществующий файл!')
except IOError:
    print('Ошибка ввода/вывода')
else:
    file.write('Hello, World!')
    file.close()

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.

os.chmod("log.txt", stat.S_ENFMT)
try:
    file = open('log.txt', 'w')
except PermissionError:
    print('Нет права доступа к файлу!')
except FileNotFoundError:
    print('Вы пытаетесь открыть несуществующий файл!')
except IOError:
    print('Ошибка ввода/вывода')
else:
    file.writeline('New log entry\n')
    file.close()
# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
try:
    file = open('pointer_example.txt', 'r+')
except PermissionError:
    print('Нет права доступа к файлу!')
except FileNotFoundError:
    print('Вы пытаетесь открыть несуществующий файл!')
except IOError:
    print('Ошибка ввода/вывода')
else:
    file.writeline("Python File Handling\n")
    file.close()

# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
import math

def calculate_square_root(number):
    # Добавьте проверку на отрицательное число и возбуждение исключения
    if number < 0:
        raise ValueError('число не должно быть отрицательным')
    return math.sqrt(number)

def safe_calculate_square_root(number):
    try:
        result = calculate_square_root(number)
        print(f"Квадратный корень из {number} равен {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
#
# # Тесты функции
safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным


# Задача 2. Допишите код ниже.
def convert_to_number(string):
    # Добавьте проверку на некорректное значение и возбуждение исключения
    if not string.isdigit():
        raise ValueError('Введенное значение не является числом')
    return int(string)
#
def safe_convert_to_number(string):
    try:
        number = convert_to_number(string)
        print(f"Конвертированное число: {number}")
    except ValueError as e:
        print(f"Ошибка: {e}")
#
# # Тесты функции
safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8, 14, добавив в него обработку ошибок,
# где это необходимо.
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
DATA_BASE = 'inventory.json'
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
#
try:
    with open(DATA_BASE, 'w') as database:
        json.dump(inventory, database)
except PermissionError:
    print('Нет права доступа к файлу!')
except FileNotFoundError:
    print('Вы пытаетесь открыть несуществующий файл!')
except IOError:
    print('Ошибка ввода/вывода')
else:
    print(f'Данные сохранены в базу данных - файл с именем {DATA_BASE}')

def inventory_read(file_name = DATA_BASE):
    try:
        with open(file_name, 'r') as database:
            inventory_database = json.load(database)
    except PermissionError:
        print('Нет права доступа к файлу!')
    except FileNotFoundError:
        print('Вы пытаетесь открыть несуществующий файл!')
    except IOError:
        print('Ошибка ввода/вывода')
    else:
        return inventory_database

def inventory_write(file_name = DATA_BASE, product_list=inventory_read()):
    try:
        with open(file_name, 'w') as database:
            json.dump(product_list, database)
    except PermissionError:
        print('Нет права доступа к файлу!')
    except FileNotFoundError:
        print('Вы пытаетесь открыть несуществующий файл!')
    except IOError:
        print('Ошибка ввода/вывода')
    else:
        print(f'обновленный список продуктов сохранен в файл {file_name}!' )

def check_number_input(message):
    while True:
        user_input = input(message)
        try:
            number = float(user_input)
        except ValueError:
            print('Введено не число')
        else:
            if number <= 0:
                raise ValueError('Число должно быть больше 0')
            else:
                return number
                break

def check_positive_number(message):
    while True:
        try:
            number = check_number_input(message)
        except ValueError as e:
            print(f'Ошибка - {e}')
        else:
            return number
            break

def check_product_input(product):
    '''Функция проверяет есть ли введенный товар в списке товара'''
    product_name_list = [item['product'].lower() for item in inventory_read()]
    if product.lower() not in product_name_list:
        return False
    else:
        return True

def print_products(product_list = inventory_read()):
    print('-' * 27)
    columns = list(product_list[0].keys())
    print('|', end='')
    for item in columns:
        print(f' {item} ', end='|')
    print()
    print('-' * 27)
    for product in product_list:
        vals = list(product.items())
        print('|', end='')
        for val in vals:
            print(f' {val[1]:{len(val[0]) + 1}}', end='|')
        print()
        print('-' * 27)


def add_product():
    new_product = input('Введите название товара: ')
    if not check_product_input(new_product):
        np_price = check_positive_number('Введите цену товара: ')
        np_count = check_positive_number('Введите количество товара: ')
        product_list = inventory_read()
        product_list.append({'product': new_product, 'price': np_price, 'count': np_count})
        inventory_write(product_list=product_list)
    else:
        print(f'Добавить можно только отсутствующий в списке продукт!')
    print_products(inventory_read())


def delete_product(product_list = inventory_read()):
    product_to_delete = input('Введите название удаляемого товара: ')
    if check_product_input(product_to_delete):
        product_list[:] = [item for item in product_list if item['product'] != product_to_delete]
        print(f'продукт {product_to_delete} удален из списка продуктов!')
        inventory_write(product_list=product_list)
    else:
        print(f'Удалять можно только продукт находящийся в списке товара!')
    print_products(product_list)


def update_product():
    product_to_update = input('Введите название обновляемого товара: ')
    if check_product_input(product_to_update):
        article_to_update = input(f'Если хотите обновить название продукта выберите 1\n'
                                  f'Если хотите обновить цену продукта выберите 2\n'
                                  f'Если хотите обновить количество продукта выберите 3: \n')
        product_list = inventory_read()
        if article_to_update == '1':
            new_product = input('Введите новое название товара: ')
            [item for item in product_list if item['product'] == product_to_update][0]['product'] = new_product
            print(f'Название продукта {product_to_update} изменено на {new_product} ')
        elif article_to_update == '2':
            new_price =  check_positive_number('Введите новую цену товара: ')
            [item for item in product_list if item['product'] == product_to_update][0]['price'] = new_price
            print(f'Новая цена продукта {product_to_update} изменена на {new_price} ')
        elif article_to_update == '3':
            new_count =  check_positive_number('Введите новое количество товара: ')
            [item for item in product_list if item['product'] == product_to_update][0]['count'] = new_count
            print(f'Новое количество продукта {product_to_update} изменена на {new_count} ')
        else:
            print('Выбор действия неверен!')
    else:
        print(f'Обновлять можно только продукт находящийся в списке товара!')
    inventory_write(product_list=product_list)
    product_list = inventory_read()
    print_products(product_list)


def update_product_new():
    product_list = inventory_read()
    articles_dict = dict(enumerate(product_list[0].keys(), 1))
    product_to_update = input('Введите название обновляемого товара: ')
    if check_product_input(product_to_update):
        article_to_update = int(input(f'Если хотите обновить название продукта выберите 1\n'
                                  f'Если хотите обновить цену продукта выберите 2\n'
                                  f'Если хотите обновить количество продукта выберите 3: \n'))
        if int(article_to_update) in list(articles_dict.keys()):
            new_article = input(f'Введите новое значение для {articles_dict[article_to_update]}')
            [item for item in product_list if item['product'] ==
            product_to_update][0][articles_dict[article_to_update]] = new_article
            print(f'Новое значение для {articles_dict[article_to_update]} продукта {product_to_update} '
                  f'изменена на {new_article} ')
        else:
            print('Выбор действия неверен!')
    else:
        print(f'Обновлять можно только продукт находящийся в списке товара!')
    inventory_write(product_list=product_list)
    product_list = inventory_read()
    print_products(product_list)

def find_product_name(product_list = inventory_read()):
    product_to_search = input('Введите название искомого товара: ')
    if check_product_input(product_to_search):
        print_products([item for item in product_list if item['product'] == product_to_search])
    else:
        print("Запрашиваемый товар не найден!")


def find_product_price( product_list = inventory_read()):
    max_price =  check_positive_number('Введите максимальную цену товара: ')
    search_list = [item for item in product_list if item['price'] <= max_price]
    print(f'Товары с ценой меньшей или равной {max_price}:')
    print_products(search_list)


def find_product_count(product_list = inventory_read()):
    max_count = check_positive_number('Введите максимальное количество товара: ')
    search_list = [item for item in product_list if item['count'] <= max_count ]
    print(f'Товары количеством меньшим или равным {max_count}:')
    print_products(search_list)


while True:
    print('\nМеню:')
    print('1. Показать список товаров.')
    print('2. Добавить товар.')
    print('3. Удалить товар.')
    print('4. Обновить название товара, стоимость или количество.')
    print('5. Найти товар по названию.')
    print('6. Вывести список товаров меньше определённой стоимости.')
    print('7. Вывести список товаров меньше определенного количества.')
    print('8. Выйти из программы.')

    choice = input('Выберите действие: ')

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
    elif choice == '8':
        print('Выход из программы')
        break
    else:
        print('Неверный выбор. Пожалуйста, выберите снова.')









