# Тема: Чтение и запись данных в файл.
from idlelib.editor import keynames

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
print('Task(1)================================')
file = open('text_files/data.txt', 'r')
result_1 = file.read()
print(result_1)
print('-------------------------------')

file = open('text_files/data.txt', 'r')
result_2 = file.read(10)
print(result_2)
print('-------------------------------')

file = open('text_files/data.txt', 'r')
result_3 = file.readline()
print(result_3)
print('-------------------------------')

file = open('text_files/data.txt', 'r')
result_4 = file.readlines()
print(result_4)
file.close()

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
print('Task(2)================================')
file = open('text_files/output.txt', 'w')
file.write("Hello, World!\n")
file.writelines(["This is line 1\n", "This is line 2\n"])
file.close()
file = open('text_files/output.txt', 'r')
result = file.read()
print(result)
file.close()

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
print('Task(3)================================')
file = open('text_files/log.txt', 'a')
file.write("New log entry\n")
file.writelines(["Log entry 1\n", "Log entry 2\n"])
file.close()
file = open('text_files/log.txt', 'r')
result = file.read()
print(result)
file.close()

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
print('Task(4)================================')
file = open('text_files/pointer_example.txt', 'w+')
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
file.close()
# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.
print('JSON = Task(1)================================')
import json

all_users = {'name': 'Aleksejs',
        'age': 39,
        'city': 'London'}
with open('user.json', 'w') as file:
    json.dump(all_users, file)
with open('user.json', 'r') as file:
    result = json.load(file)
    print(result)


# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.
print('JSON = Task(2)================================')
with open('user.json', 'r') as file:
    user = json.load(file)
user['age'] = 29
with open('user.json', 'w') as file:
    json.dump(user, file)


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`--- создания нового файла (USERS)
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
# Задача 3: Добавление нового пользователя в массив JSON

print('JSON = Task(3)================================')

users = [
    {'name': 'Aleksejs', 'age': 39, 'city': 'London'}
]
with open('users.json', 'w') as file:
    json.dump(users, file)

with open('users.json', 'r') as file:
    all_users = json.load(file)

new_user = {'name': 'Linda', 'age': 35, 'city': 'Barcelona'}
all_users.append(new_user)

with open('users.json', 'w') as file:
    json.dump(all_users, file)

with open('users.json', 'r') as file:
    all_users = json.load(file)
    print(all_users)

# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
print('JSON = Task(4)================================')

with open('users.json', 'r') as file:
    all_users = json.load(file)
del_user = all_users.pop(0)

with open('users.json', 'w') as file:
    json.dump(del_user, file)

with open('users.json', 'r') as file:
    all_users = json.load(file)
    print(all_users)

print('Project================================')
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


