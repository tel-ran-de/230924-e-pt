# Тема: Модуль datetime
from datetime import datetime
import json
import os
# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45
# now = datetime.now()
# now_date = now.strftime('%Y-%m-%d %H:%M:%S')
# print(now_date)
print('+========================+')
# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.
# def calculate_age(birth_date):
#     birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
#     today = datetime.today()
#     result = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return result
#
#
# # Пример использования
# bd = input("Введите дату рождения в формате DD.MM.YYYY: ")
# age = calculate_age(bd)
# print(f"Ваш возраст: {age} лет")
print('+========================+')
# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.
# today = datetime.today().date()
# event_date_input = input("Введите дату в формате YYYY-MM-DD: ")
# event_date = datetime.strptime(event_date_input, '%Y-%m-%d').date()
# delta = event_date - today
# print(f'Осталось {delta.days}')
print('+========================+')
# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.
# date_input = input("Введите дату в формате YYYY-MM-DD: ")
# date = datetime.strptime(date_input, "%Y-%m-%d")
#
# day_of_week = date.strftime("%A")
#
# print(f'День недели для даты: {date_input} будет {day_of_week}')
print('+========================+')
# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.
# date_1_input = input("Введите первую дату в формате YYYY-MM-DD: ")
# date_2_input = input("Введите вторую дату в формате YYYY-MM-DD: ")
#
# date_1 = datetime.strptime(date_1_input, '%Y-%m-%d').date()
# date_2 = datetime.strptime(date_2_input, '%Y-%m-%d').date()
# if date_1 > date_2:
#     print(f"Дата {date_1} позже, чем {date_2}")
# elif date_1 < date_2:
#     print(f"Дата {date_2} позже, чем {date_1}")
# else:
#     print("Обе даты одинаковы.")
print('+========================+')
# Тема: Модуль os

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.
import os


# directory_new = "test_directory"
# os.mkdir(directory_new)
#
# file_dir = os.listdir('.')
# for i in os.listdir('.'):
#     if os.path.isdir(i):
#         print(i)

# os.rmdir(directory_new)
print('+========================+')
# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.
# file_1 = "temp_file.txt"
# with open(file_1, 'w') as file:
#     file.write("Temporary content")
#
# file_2 = "renamed_file.txt"
# # os.rename(file_1, file_2)
# for i in os.listdir('.'):
#     if os.path.isfile(i):
#         print(i)
print('+========================+')
# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".
# new_file = "examples.py"
# if os.path.exists(new_file):
#
#     print(os.path.getsize(new_file))
# else:
#     print("Файл не найден")
print('+========================+')
# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".
# file_1 = input('Введите имя файла 1: ')
# file_2 = input('Введите имя файла 2: ')
# size_1 = os.path.getsize(file_1)
# size_2 = os.path.getsize(file_2)
#
# if size_1 < size_2:
#     print(f'{file_2} больше {file_1}' )
# elif size_1 > size_2:
#     print(f'{file_1} больше {file_2}')
# else:
#     print("Файлы имеют одинаковый размер")
print('+========================+')
# Тема: Интеграционная практика.

# Проект: Перепишите проект из уроков 7-8, 14-15, добавив в него фичи 1 - 3 на основе модулей datetime и os.
#
# Фича 1. Добавьте в каждый товар дату и время его создания,
# а также дату и время обновления данных о товаре или количества товара.
#
# Фича 2: Логирование действий с товарами
# Создайте лог-файл, куда будет записываться история всех действий с товарами (добавление, удаление, обновление).
# Используйте модуль datetime для добавления временных меток к каждому действию с товарами.
#
# Фича 3. Резервное копирование данных:
# Используйте модуль os для создания резервных копий файла с товарами.
# Например, при каждом запуске программы создается копия файла с добавлением текущей даты и времени.
#
#
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
# Используйте файл как базу данных проекта.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.



def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = []
        print('Файл не найден! Создание нового списка.')
    return inventory



def save_inventory(inventory):
    try:
        with open('inventory.json', 'w') as file:
            json.dump(inventory, file)
    except IOError as e:
        print('Ошибка сохранения файла')

def show_inventory():
    inventory = load_inventory()
    if not inventory:
        print('\nСписок товаров пуст.')
        return
    print('\nСписок товаров:')
    for item in inventory:
        print(f"Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}")

def add_item():
    try:
        inventory = load_inventory()
        product_name = input('Введите название товара: ')
        price_item = float(input('Введите цену: '))
        count_item = int(input('Введите количество: '))
        inventory.append({'product': product_name, 'price': price_item, 'count': count_item})
        save_inventory(inventory)
        print(f"product: {product_name}, price: {price_item}, count: {count_item} добавлен в список товаров.")
    except ValueError:
        print('Цена и количество должны быть числами.')


def delete_items():
    try:
        inventory = load_inventory()
        delete_item = input('Какой товар вы хотите удалить: ')
        for item in inventory:
            if item['product'] == delete_item:
                inventory.remove(item)
                save_inventory(inventory)
                print(f'product: {delete_item} удален!')
            else:
                print('Продукт не найден.')
    except IOError:
        print("Ошибка обработки файла!")


def update_item():
    try:
        inventory = load_inventory()
        name_item = input('Введите название товара для обновления: ')
        for item in inventory:
            if item['product'] == name_item:
                items = input("Что вы хотите обновить: product, price, count: ").lower()
                if items == 'product':
                    item['product'] = input('Введите новое название товара: ')
                elif items == 'price':
                    item['price'] = float(input('Введите новую цену товара: '))
                elif items == 'count':
                    item['count'] = int(input('Введите новое количество товара: '))
                else:
                    print('Продукт не найден.')
                save_inventory(inventory)
                print(f'Продукт {item['product']} обновлён.')
                return
    except ValueError:
        print('Цена и количество должны быть числами.')
    except IOError as e:
        print("Ошибка обработки файла!")


def find_item():
    inventory = load_inventory()
    name_item = input('Введите название товара для поиска: ')
    for item in inventory:
        if item['product'] == name_item:
            print(f"Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}")
            return
    else:
        print('Продукт не найден.')

def below_price():
    try:
        inventory = load_inventory()
        below_item_price = float(input('Введите определенную стоимость: '))
        print(f'\nТовары меньше {below_item_price} стоимости:')
        for item in inventory:
            if item['price'] < below_item_price:
                print(f'Товар: {item['product']}')
    except ValueError:
        print('Цена товара должно быть числом.')

def below_count():
    try:
        inventory = load_inventory()
        below_item_count = int(input('Введите определенное количество: '))
        print(f'\nТовары меньше количества {below_item_count}')
        for item in inventory:
            if item['count'] < below_item_count:
                print(f'Товар: {item['product']}')
    except ValueError:
        print('Количество товара должно быть числом.')


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










