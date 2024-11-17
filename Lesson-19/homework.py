# Тема: Чтение и запись данных в файл.
from fileinput import close
# print("Тема: Чтение и запись данных в файл.")
# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
#
# print("---------Задание 1: Чтение данных из файла--------")
file_data = open('text_files/data.txt', 'r')
content = file_data.read()
print(50 * "-")
print("Весь контент файла:")
print(content)
print(50 * "-")
file_data.seek(0)    # Возвращаем указатель на начало файла
first_10_chars = file_data.read(10)
print("Первые 10 символов файла:")
print(first_10_chars)
print(50 * "-")
file_data.seek(0)    # Возвращаем указатель на начало файла
first_line = file_data.readline()
print("Первая строка файла:")
print(first_line)
print(50 * "-")
file_data.seek(0)    # Возвращаем указатель на начало файла
all_lines_file = file_data.readlines()
print("Все строки файла:")
for line in all_lines_file:
    print(line, end='')
print(50 * "-")
# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
#
# print("---------Задание 2: Запись данных в файл--------")
file_output = open('text_files/output.txt', 'w')
file_output.write("Hello, World!\n")
lines = ["This is line 1\n", "This is line 2\n"]
file_output.writelines(lines)
file_output.close()

file_output = open('text_files/output.txt', 'r')
content = file_output.read()
print("Содержимое файла output.txt:")
print(content)
print(50 * "-")
# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
# print("---------Задание 3: Добавление данных в файл--------")
file_log = open('text_files/log.txt', 'a')
file_log.write("New log entry\n")
lines = ["Log entry 1\n", "Log entry 2\n"]
file_log.writelines(lines)
file_log.close()

file_log = open('text_files/log.txt', 'r')
content = file_log.read()
print("Содержимое файла log.txt:")
print(content)
print(50 * "-")
# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
# print("---------Задание 4: Работа с указателем--------")
file_pointer_example = open('pointer_example.txt', 'r+')
file_pointer_example.write("Python File Handling\n")
# 3. Переместите указатель в начало файла и прочитайте первую строку.
file_pointer_example.seek(0)
first_line = file_pointer_example.readline()
print("Первая строка файла:")
print(first_line)
print(50 * "-")
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
file_pointer_example.seek(7)
next_5_chars = file_pointer_example.read(5)
print("Следующие 5 символов после позиции 7:")
print(next_5_chars)
print(50 * "-")
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
file_pointer_example.seek(0, 2)  # в конец файла
file_pointer_example.write("End of file\n")
file_pointer_example.close()

file_pointer_example = open('pointer_example.txt', 'r')
print(file_pointer_example.read())
print(50 * "-")
# Тема: Менеджер контекста и JSON
import json


print("Тема: Менеджер контекста и JSON")
print("Задача 1: Чтение и запись JSON данных с использованием менеджера контекста")

# Задача 1: Чтение и запись JSON данных
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
user_info = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# 2. Записываем этот словарь в файл JSON `user.json` с использованием менеджера контекста
with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(user_info, file, ensure_ascii=False, indent=4)

# 3. Читаем данные из файла `user.json` и выводим их на экран
with open('user.json', 'r', encoding='utf-8') as file:
    user_data = json.load(file)
    print(50 * "-")
    print("Данные из файла user.json:")
    print(user_data)

print(50 * "-")
print("Задача 2: Обновление данных в файле JSON")

# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON.

with open('user.json', 'r', encoding='utf-8') as file:
    user_data = json.load(file)

user_data['age'] = 29

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)

print("Обновленные данные из файла user.json:")
print(user_data)

print(50 * "-")
print("Задача 3: Добавление нового пользователя в массив JSON")

# Задача 3: Добавление нового пользователя в массив JSON
# Проверим, является ли файл `users.json` массивом объектов.

try:
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
except FileNotFoundError:
    # Если файл не найден, создаём пустой список
    users = []

# Проверяем, что данные являются списком
if not isinstance(users, list):
    print("Ошибка: данные в файле не являются списком. Создаем новый список.")
    users = []

# 2. Добавляем нового пользователя в массив
new_user = {
    "name": "Alex",
    "age": 30,
    "city": "New York"
}
users.append(new_user)

# Выводим обновленный список пользователей
print("Обновленный список пользователей:", users)

# 3. Записываем обновленный массив обратно в файл JSON
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)

print("Новый пользователь успешно добавлен в файл users.json")


# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
print(50 * "-")
print("Задача 4: Удаление пользователя из массива JSON")

try: # 1. Читаем массив объектов из файла `users.json`
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
except FileNotFoundError:
    print("Файл `users.json` не найден.")
    users = []

if not isinstance(users, list):
    print("Ошибка: данные в файле не являются списком.")
    users = []

name_to_delete = "Alex" # 2. Удаляем пользователя по имени ("Alex")
users = [user for user in users if user.get("name") != name_to_delete]

with open('users.json', 'w', encoding='utf-8') as file:  # 3. Записываем обновлённый массив обратно в файл JSON
    json.dump(users, file, ensure_ascii=False, indent=4)

print("Пользователь удалён из файла users.json")
print("Обновлённый список пользователей:", users)


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле (через JSON).
# Используйте файл как базу данных проекта.
#
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

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]
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

# загрузка файла
def load_inventory():
    with open(inventory_file, 'r', encoding='utf-8') as file:
        return json.load(file)
# сохранение в файл
def save_inventory(inventory):
    with open(inventory_file, 'w', encoding='utf-8') as file:
        json.dump(inventory, file, ensure_ascii=False, indent=4)

def print_inventory():
    inventory = load_inventory()
    if not inventory:
        print("Инвентарь пуст.")
    else:
        headers = ["Название товара", "Цена", "Количество"]
        table = [[item['product'].title(), item['price'], item['count']] for item in inventory]
        print(tabulate(table, headers=headers, tablefmt="grid"))

def add_product():
    inventory = load_inventory()
    product = input("Введите название товара: ").strip()
    for item in inventory:
        if item['product'].lower() == product.lower():
            print("Товар уже существует.")
            return
    price = int(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': product, 'price': price, 'count': count})
    save_inventory(inventory)
    print("Товар добавлен.")

def delete_product():
    inventory = load_inventory()
    product = input("Введите название товара для удаления: ").strip()
    item_exists = any(item['product'].lower() == product.lower() for item in inventory)
    if not item_exists:
        print("Ошибка: Товар не найден.")
        return
    inventory = [item for item in inventory if item['product'].lower() != product.lower()]
    save_inventory(inventory)
    print("Товар удалён.")

def update_product():
    inventory = load_inventory()
    product = input("Введите название товара для обновления: ").strip()
    for item in inventory:
        if item['product'].lower() == product.lower():
            item['price'] = int(input("Введите новую цену: "))
            item['count'] = int(input("Введите новое количество: "))
            save_inventory(inventory)
            print("Товар обновлён.")
            return
    print("Товар не найден.")

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

def filter_by_price():
    inventory = load_inventory()
    max_price = int(input("Введите максимальную цену: "))
    filtered = [item for item in inventory if item['price'] <= max_price]
    if not filtered:
        print("Нет товаров дешевле указанной цены.")
    else:
        headers = ["Название товара", "Цена", "Количество"]
        table = [[item['product'].title(), item['price'], item['count']] for item in filtered]
        print(tabulate(table, headers=headers, tablefmt="grid"))

def filter_by_count():
    inventory = load_inventory()
    max_count = int(input("Введите максимальное количество: "))
    filtered = [item for item in inventory if item['count'] <= max_count]
    if not filtered:
        print("Нет товаров с количеством ниже указанного.")
    else:
        headers = ["Название товара", "Цена", "Количество"]
        table = [[item['product'].title(), item['price'], item['count']] for item in filtered]
        print(tabulate(table, headers=headers, tablefmt="grid"))

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

menu()

