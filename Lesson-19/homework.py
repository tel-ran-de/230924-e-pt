# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.




with open('data.txt', 'r') as file:
    # 2. Прочитаем весь контент файла и выведем его на экран
    content = file.read()
    print("Полный контент файла:")
    print(content)

    # 3. Прочитаем первые 10 символов файла и выведем их
    file.seek(0)  # Сбрасываем указатель файла на начало
    first_10_chars = file.read(10)
    print("\nПервые 10 символов файла:")
    print(first_10_chars)

    # 4. Прочитаем одну строку из файла и выведем её
    file.seek(0)  # Сбрасываем указатель файла на начало
    first_line = file.readline()
    print("\nПервая строка файла:")
    print(first_line)

    # 5. Прочитаем все строки файла и выведем их на экран
    file.seek(0)  # Сбрасываем указатель файла на начало
    all_lines = file.readlines()
    print("\nВсе строки файла:")
    for line in all_lines:
        print(line, end='')  # Используем end='', чтобы не добавлять лишний символ новой




# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.




 "Открытие файла для записи"
with open('output.txt', 'w') as file:

    "Записываем строку"
    file.write("Hello, World!\n")

    "Записываем список строк"
    file.writelines(["This is line 1\n", "This is line 2\n"])

"Открытие файла для чтения и вывод его содержимого"
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)















# Задание 3:







# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.




 "1. Открываем (создаем) файл для чтения и записи"
with open('pointer_example.txt', 'w+') as file:

    "2. Записываем строку в файл"
    file.write("Python File Handling\n")

    "3. Перемещаем указатель в начало файла и читаем первую строку"
    file.seek(0)  # Перемещаем указатель в начало файла
    first_line = file.readline()
    print("Первая строка:", first_line)

    "4. Перемещаем указатель на позицию 7 и читаем следующие 5 символов"
    file.seek(7)  # Перемещаем указатель на позицию 7
    five_chars = file.read(5)  # Читаем следующие 5 символов
    print("5 символов начиная с позиции 7:", five_chars)

    "5. Перемещаем указатель в конец файла и добавляем строку "End of file"
    file.seek(0, 2)  # Перемещаем указатель в конец файла
    file.write("End of file\n")

    "6. Перемещаем указатель в начало файла и читаем весь файл"
    file.seek(0)  # Перемещаем указатель в начало файла
    full_content = file.read()  # Читаем весь файл
    print("\nПолное содержимое файла:")
    print(full_content)





# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.


# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.





import json
import os

# Путь к файлу с пользователями
FILE_NAME = 'users.json'

# Функция для загрузки данных из файла
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Функция для сохранения данных в файл
def save_users(users):
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4)

# Функция для добавления нового пользователя
def add_user(users, name, age, city):
    new_user = {
        'name': name,
        'age': age,
        'city': city
    }
    users.append(new_user)
    print(f"Пользователь '{name}' добавлен.")

# Главная функция для работы с пользователями
def main():
    # Загружаем пользователей из файла
    users = load_users()

    # Запрашиваем информацию о новом пользователе
    print("Введите данные нового пользователя:")
    name = input("Имя: ")
    age = input("Возраст: ")
    city = input("Город: ")

    # Проверяем, что возраст — это число
    try:
        age = int(age)
    except ValueError:
        print("Возраст должен быть числом!")
        return

    # Добавляем нового пользователя в список
    add_user(users, name, age, city)

    # Сохраняем обновленный список пользователей в файл
    save_users(users)

# Запуск программы
if __name__ == "__main__":
    main()






# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.






import json
import os

# Путь к файлу с пользователями
FILE_NAME = 'users.json'

# Функция для загрузки данных из файла
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Функция для сохранения данных в файл
def save_users(users):
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4)

# Функция для удаления пользователя по имени
def delete_user(users, username):
    user_to_delete = None
    for user in users:
        if user['name'].lower() == username.lower():
            user_to_delete = user
            break

    if user_to_delete:
        users.remove(user_to_delete)
        print(f"Пользователь '{username}' удален.")
    else:
        print(f"Пользователь с именем '{username}' не найден.")

# Главная функция для работы с пользователями
def main():
    # Загружаем пользователей из файла
    users = load_users()

    if not users:
        print("Нет пользователей для удаления.")
        return

    # Печатаем список пользователей
    print("Список пользователей:")
    for index, user in enumerate(users, start=1):
        print(f"{index}. Имя: {user['name']}, Возраст: {user['age']}")

    # Запрашиваем пользователя, которого нужно удалить
    username_to_delete = input("Введите имя пользователя для удаления: ")

    # Удаляем пользователя
    delete_user(users, username_to_delete)

    # Сохраняем обновленный список пользователей в файл
    save_users(users)

# Запуск программы
if __name__ == "__main__":
    main()








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

import json
import os

# Путь к файлу, который будет хранить инвентарь
FILE_NAME = 'inventory.json'


# Функция для загрузки данных из файла
def load_inventory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []


# Функция для сохранения данных в файл
def save_inventory(inventory):
    with open(FILE_NAME, 'w') as file:
        json.dump(inventory, file, indent=4)


# Функция для отображения списка всех товаров
def show_inventory(inventory):
    if not inventory:
        print("Инвентарь пуст.")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")


# Функция для добавления товара
def add_product(inventory):
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': name, 'price': price, 'count': count})
    save_inventory(inventory)
    print(f"Товар '{name}' добавлен в инвентарь.")


# Функция для удаления товара
def delete_product(inventory):
    name = input("Введите название товара для удаления: ")
    for item in inventory:
        if item['product'].lower() == name.lower():
            inventory.remove(item)
            save_inventory(inventory)
            print(f"Товар '{name}' удален из инвентаря.")
            return
    print(f"Товар '{name}' не найден в инвентаре.")


# Функция для обновления данных о товаре
def update_product(inventory):
    name = input("Введите название товара для обновления: ")
    for item in inventory:
        if item['product'].lower() == name.lower():
            print(f"Найден товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            choice = input("Что хотите обновить? (name/price/count): ").lower()
            if choice == 'name':
                item['product'] = input("Введите новое название товара: ")
            elif choice == 'price':
                item['price'] = float(input("Введите новую цену товара: "))
            elif choice == 'count':
                item['count'] = int(input("Введите новое количество товара: "))
            else:
                print("Неверный выбор.")
                return
            save_inventory(inventory)
            print(f"Товар '{item['product']}' обновлен.")
            return
    print(f"Товар '{name}' не найден в инвентаре.")


# Функция для поиска товара по названию
def find_product(inventory):
    name = input("Введите название товара для поиска: ")
    found = [item for item in inventory if name.lower() in item['product'].lower()]
    if found:
        for item in found:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print(f"Товар '{name}' не найден.")


# Функция для вывода товаров по цене ниже заданной
def filter_by_price(inventory):
    price = float(input("Введите максимальную цену товара: "))
    filtered = [item for item in inventory if item['price'] < price]
    if filtered:
        for item in filtered:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print(f"Товары дешевле {price} не найдены.")


# Функция для вывода товаров с количеством ниже заданного
def filter_by_count(inventory):
    count = int(input("Введите минимальное количество товара: "))
    filtered = [item for item in inventory if item['count'] < count]
    if filtered:
        for item in filtered:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print(f"Товары с количеством менее {count} не найдены.")


# Главная функция для работы с меню
def main():
    inventory = load_inventory()
    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить товар.")
        print("5. Найти товар по названию.")
        print("6. Вывести товары дешевле заданной цены.")
        print("7. Вывести товары с количеством меньше заданного.")
        print("8. Выход.")

        choice = input("Выберите действие (1-8): ")

        if choice == '1':
            show_inventory(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            delete_product(inventory)
        elif choice == '4':
            update_product(inventory)
        elif choice == '5':
            find_product(inventory)
        elif choice == '6':
            filter_by_price(inventory)
        elif choice == '7':
            filter_by_count(inventory)
        elif choice == '8':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()
