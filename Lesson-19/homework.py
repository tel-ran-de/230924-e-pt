# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
# 1. Откройте файл `data.txt` для чтения

with open('data.txt', 'r') as file:
    # 2. Прочитайте весь контент файла и выведите его на экран
    full_content = file.read()
    print("Полный контент файла:")
    print(full_content)

# Снова открываем файл, так как указатель на файл вернется в начало только после закрытия
with open('data.txt', 'r') as file:
    # 3. Прочитайте первые 10 символов файла и выведите их на экран
    first_10_chars = file.read(10)
    print("\nПервые 10 символов файла:")
    print(first_10_chars)

# Открываем файл заново
with open('data.txt', 'r') as file:
    # 4. Прочитайте одну строку из файла и выведите ее на экран
    first_line = file.readline()
    print("\nПервая строка файла:")
    print(first_line)
#
# Открываем файл заново
with open('data.txt', 'r') as file:
    # 5. Прочитайте все строки файла и выведите их на экран
    all_lines = file.readlines()
    print("\nВсе строки файла:")
    for line in all_lines:
        print(line, end='')  # `end=''` убирает лишние переносы строк


# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.

# 1. Открываем (создаем) файл `output.txt` для записи
with open('output.txt', 'w') as file:
    # 2. Записываем в файл строку "Hello, World!"
    file.write("Hello, World!\n")

    # 3. Записываем в файл список строк
    lines = ["This is line 1\n", "This is line 2\n"]
    file.writelines(lines)

# 4. Закрытие файла происходит автоматически благодаря `with` оператору

# 5. Открываем файл `output.txt` для чтения и выводим его содержимое на экран
with open('output.txt', 'r') as file:
    content = file.read()
    print("Содержимое файла 'output.txt':")
    print(content)

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.

# 1. Открываем (создаем) файл `log.txt` для добавления данных
with open('log.txt', 'a') as file:
    # 2. Добавляем строку "New log entry\n" в конец файла
    file.write("New log entry\n")

    # 3. Добавляем список строк в конец файла
    log_entries = ["Log entry 1\n", "Log entry 2\n"]
    file.writelines(log_entries)

# 4. Закрытие файла происходит автоматически благодаря `with` оператору

# 5. Открываем файл `log.txt` для чтения и выведите его содержимое на экран
with open('log.txt', 'r') as file:
    content = file.read()
    print("Содержимое файла 'log.txt':")
    print(content)

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.

# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи
with open('pointer_example.txt', 'w+') as file:
    # 2. Запишите в файл строку "Python File Handling\n"
    file.write("Python File Handling\n")

    # 3. Переместите указатель в начало файла и прочитайте первую строку
    file.seek(0)  # Перемещаем указатель в начало файла
    first_line = file.readline()
    print("Первая строка файла:")
    print(first_line)

    # 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов
    file.seek(7)
    next_five_chars = file.read(5)
    print("\n5 символов, начиная с позиции 7:")
    print(next_five_chars)

    # 5. Переместите указатель в конец файла и добавьте строку "End of file\n"
    file.seek(0, 2)  # Перемещаем указатель в конец файла
    file.write("End of file\n")

    # 6. Переместите указатель в начало файла и прочитайте весь файл
    file.seek(0)
    full_content = file.read()
    print("\nПолное содержимое файла после всех операций:")
    print(full_content)

# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.

import json

# 1. Создаем словарь с информацией о пользователе (имя, возраст, город)
user_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 2. Записываем этот словарь в файл JSON `user.json` с использованием менеджера контекста
with open('user.json', 'w') as file:
    json.dump(user_data, file, indent=4)  # indent=4 для красивого форматирования

# 3. Читаем данные из файла `user.json` и выводим их на экран
with open('user.json', 'r') as file:
    data = json.load(file)
    print("Данные из файла 'user.json':")
    print(data)


# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.

import json

# 1. Читаем данные из файла `user.json`
with open('user.json', 'r') as file:
    user_data = json.load(file)

# 2. Обновляем возраст пользователя на 29 лет
user_data['age'] = 29

# 3. Записываем обновленные данные обратно в файл JSON с использованием менеджера контекста
with open('user.json', 'w') as file:
    json.dump(user_data, file, indent=4)  # indent=4 для красивого форматирования

print("Данные успешно обновлены.")


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.

import json
import os

# 1. Проверяем, существует ли файл `users.json`
if os.path.exists('users.json'):
    # Если файл существует, прочитаем его содержимое
    with open('users.json', 'r') as file:
        users = json.load(file)
else:
    # Если файла нет, выведем сообщение об ошибке
    users = []

# 2. Добавляем нового пользователя в массив
new_user = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
users.append(new_user)

# 3. Записываем обновленный массив обратно в файл JSON с использованием менеджера контекста
with open('users.json', 'w') as file:
    json.dump(users, file, indent=4)

print("Новый пользователь добавлен.")



# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
if os.path.exists('users.json'):
    with open('users.json', 'r') as file:
        users = json.load(file)
else:
    print("Файл 'users.json' не найден.")
    exit()

# 2. Удаляем одного из пользователей по имени

user_to_remove = "Bob"  # Пример: удаляем пользователя с именем Bob
users = [user for user in users if user['name'] != user_to_remove]

# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста
with open('users.json', 'w') as file:
    json.dump(users, file, indent=4)

print(f"Пользователь {user_to_remove} удален.")

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
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.

import json
import os

#  Путь к файлу JSON где хранится инвентарь

inventory_file = 'inventory.json'

inventory = [
    {'product': "Laptop", 'price': 1000, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 200, 'count': 10}
]
# with open('inventory.json', 'w') as file:
#     json.dump(inventory, file, indent=4)  # indent=4 для красивого форматирования

# 1. Загрузка инвентаря из файла.
# Проверяем существует ли файл
def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as file:
            return json.load(file)
    else:
        # Если файл не существует, создаем его с начальным списком товаров
        save_inventory(inventory)
        return inventory
#
# 2. Сохранение инвентаря в файл

def save_inventory(inventory):
    with open(inventory_file, 'w') as file:
        json.dump(inventory, file, indent=4)

# 3. Показываем список товаров
def show_inventory():
    inventory = load_inventory()
    print("\nСписок товаров:")
    for item in inventory:
        print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

# 4. Добавляем товар
def add_product():
    product_name = input("Введите название товара: ")
    price = float(input("Введите стоимость товара: "))
    count = int(input("Введите количество товара: "))

    inventory = load_inventory()
    inventory.append({'product': product_name, 'price': price, 'count': count})
    save_inventory(inventory)
    print(f"Товар '{product_name}' добавлен в инвентарь.")

# 5. Удаляем товар

def delete_product():
    product_name = input("Введите название товара для удаления: ")
    inventory = load_inventory()
    inventory = [item for item in inventory if item['product'] != product_name]
    save_inventory(inventory)
    print(f"Товар '{product_name}' удален из инвентаря.")

# 6. Обновляем товар
def update_product():
    product_name = input("Введите название товара для обновления: ")
    inventory = load_inventory()
    for item in inventory:
        if item['product'] == product_name:
            item['price'] = float(input("Введите новую стоимость товара: "))
            item['count'] = int(input("Введите новое количество товара: "))
            save_inventory(inventory)
            print(f"Товар '{product_name}' обновлен.")
            return
    print(f"Товар '{product_name}' не найден.")
#
#  7. Найти товар по названию.
#
def find_product():
    product_name = input("Введите название товара для поиска: ")
    inventory = load_inventory()
    for item in inventory:
        if item['product'] == product_name:
            print(f"Найден товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            return
    print(f"Товар '{product_name}' не найден.")
#
# 8. Выводим список товаров ниже определенной стоимости
#
def list_products_below_price():
    price_limit = float(input("Введите предел стоимости: "))
    inventory = load_inventory()
    print(f"\nТовары с ценой ниже {price_limit}:")
    for item in inventory:
        if item['price'] < price_limit:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
#
#  9. Выводим список товаров ниже определенного количества
#
def list_products_below_count():
    count_limit = int(input("Введите предел количества: "))
    inventory = load_inventory()
    print(f"\nТовары с количеством ниже {count_limit}:")
    for item in inventory:
        if item['count'] < count_limit:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
#
# 8. Главное меню
#
def main():
    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров меньше определенной стоимости.")
        print("7. Вывести список товаров меньше определенного количества.")
        print("8. Выход.")

        choice = input("Выберите действие (1-8): ")

        if choice == '1':
            show_inventory()
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            find_product()
        elif choice == '6':
            list_products_below_price()
        elif choice == '7':
            list_products_below_count()
        elif choice == '8':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 8.")
# 9. Запуск программы
main()



