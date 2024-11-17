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

name_to_delete = "Alex" # 2. Удаляем пользователя по имени (например, "Alex")
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
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]


