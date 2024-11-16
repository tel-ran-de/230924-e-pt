# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
file = open("text_files/data.txt", "r")
# 2. Прочитайте весь контент файла и выведите его на экран.
content = file.read()
print(content)
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
file.seek(0)
file_read_10 = file.read(10)
print(file_read_10)
# 4. Прочитайте одну строку из файла и выведите ее на экран.
file.seek(0)
file_line = file.readline()
print(file_line)
# 5. Прочитайте все строки файла и выведите их на экран.
file.seek(0)
all_lines = file.readlines()
print(all_lines)
file.close()

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
#создан
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")#2. Запишите в файл строку "Hello, World!".

    lines = ["This is line 1\n", "This is line 2\n"]
    file.writelines(lines)# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.сам закрывается с менеджером with
with open('output.txt', 'r') as file:
        content = file.read()
        print(content)# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.


# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
with open('log.txt', 'a') as file:
    file.write("New log entry\n")# 2. Добавьте строку "New log entry\n" в конец файла.
    file.writelines(["Log entry 1\n", "Log entry 2\n"])# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
with open('log.txt', 'r') as file:
        content = file.read()
        print(content)# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.


# Задание 4: Работа с указателем
with open('pointer_example.txt', 'w+') as file:# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
    file.write("Python File Handling\n")# 2. Запишите в файл строку "Python File Handling\n".
    file.seek(0)
    first_line = file.readline()
    print("Первая строка:", first_line)  # 3. Переместите указатель в начало файла и прочитайте первую строку.
    file.seek(7)
    next_five_chars = file.read(5)
    print("Следующие 5 символов с позиции 7:", next_five_chars) # 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
    file.seek(0, 2)
    file.write("End of file\n")# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
    file.seek(0)
    entire_content = file.read()
    print("Содержимое файла:\n", entire_content) # 6. Переместите указатель в начало файла и прочитайте весь файл.


# Тема: Менеджер контекста и JSON
import json
# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
user_info = {
    "name": "Ольга",
    "age": 43,
    "city": "Миндэн"
}# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
with open('user.json', 'w', encoding='utf-8') as json_file:
    json.dump(user_info, json_file, ensure_ascii=False, indent=4)# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
with open('user.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data)# 3. Прочитайте данные из файла `user.json` и выведите их на экран.


# Задача 2: Обновление данных в файле JSON
import json

with open('user.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)# 1. Прочитайте данные из файла `user.json`.
    data['age'] = 29# 2. Обновите возраст пользователя на 29 лет.
with open('user.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `user.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.

with open('user.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

if isinstance(users, dict):
    users = [users]

new_user = {
    "name": "Paskal",
    "age": 30,
    "city": "Berlin"
}

users.append(new_user)

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)

print("Новый пользователь добавлен!")

# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open('user.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

user_to_remove = "Ольга"
users = [user for user in users if user["name"] != user_to_remove]

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)

print("Пользователь успешно удален!")

# Тема: Интеграционная практика. Мини-проект - Проект будет сдан дополнительно

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


