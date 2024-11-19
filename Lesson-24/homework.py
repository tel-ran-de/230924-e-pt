# Тема: Модуль datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45
from datetime import datetime

# Определение текущей даты и времени
current_datetime = datetime.now()

# Форматирование даты и времени в строку "YYYY-MM-DD HH:MM:SS"
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Вывод результата
print("Текущая дата и время:", formatted_datetime)



# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

# from datetime import datetime

# Функция для вычисления возраста
def calculate_age(birth_date):
    # Преобразуем строку в объект datetime
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()

    # Вычисляем возраст с учетом текущей даты
    result = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return result


#  Результат
bd = input("Введите дату рождения в формате YYYY-MM-DD: ")
try:
    age = calculate_age(bd)
    print(f"Ваш возраст: {age} лет")
except ValueError:
    print("Ошибка: Введите дату в формате YYYY-MM-DD.")

# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.

# from datetime import datetime

# Функция для расчета дней до мероприятия
def days_until_event(event_date):
    # Преобразуем строку в объект datetime
    event_date = datetime.strptime(event_date, "%Y-%m-%d")
    today = datetime.today()

    # Вычисляем разницу между датами
    delta = event_date - today

    # Если событие уже прошло, вывести сообщение
    if delta.days < 0:
        return f"Мероприятие уже прошло {abs(delta.days)} дней назад."
    else:
        return f"До мероприятия осталось {delta.days} дней."


# Результат
event_date = input("Введите дату следующего мероприятия в формате YYYY-MM-DD: ")
try:
    result = days_until_event(event_date)
    print(result)
except ValueError:
    print("Ошибка: Введите дату в формате YYYY-MM-DD.")

# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.

# from datetime import datetime

# Функция для определения дня недели
def get_weekday(date_string):
    # Преобразуем строку в объект datetime
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    # Получаем название дня недели
    weekday = date_object.strftime("%A")
    return weekday

# Пример использования
date_input = input("Введите дату в формате YYYY-MM-DD: ")
try:
    weekday = get_weekday(date_input)
    print(f"День недели для {date_input}: {weekday}")
except ValueError:
    print("Ошибка: Введите дату в формате YYYY-MM-DD.")

# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.

from datetime import datetime

#  Функция для сравнения двух дат
def compare_dates(date1, date2):
    # Преобразуем строки в объекты datetime
    date1_object = datetime.strptime(date1, "%Y-%m-%d")
    date2_object = datetime.strptime(date2, "%Y-%m-%d")

    # Сравнение дат
    if date1_object > date2_object:
        return f"{date1} позже, чем {date2}."
    elif date1_object < date2_object:
        return f"{date1} раньше, чем {date2}."
    else:
        return f"{date1} и {date2} — это одна и та же дата."


# Пример использования
date1_input = input("Введите первую дату в формате YYYY-MM-DD: ")
date2_input = input("Введите вторую дату в формате YYYY-MM-DD: ")

try:
    result = compare_dates(date1_input, date2_input)
    print(result)
except ValueError:
    print("Ошибка: Введите даты в формате YYYY-MM-DD.")

# Тема: Модуль os

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.

import os

# Функция для создания, отображения и удаления директории
def manage_directory():
    # Имя директории
    dir_name = "test_directory"

    # Создание новой директории
    try:
        os.mkdir(dir_name)
        print(f"Директория '{dir_name}' создана.")
    except FileExistsError:
        print(f"Ошибка: Директория '{dir_name}' уже существует.")

    # Список всех директорий в текущем каталоге
    print("\nСписок директорий в текущем каталоге:")
    current_directories = [d for d in os.listdir() if os.path.isdir(d)]
    print("\n".join(current_directories))

    # Удаление созданной директории
    try:
        os.rmdir(dir_name)
        print(f"\nДиректория '{dir_name}' удалена.")
    except OSError:
        print(f"Ошибка: Не удалось удалить директорию '{dir_name}'.")

    # Запуск программы
manage_directory()

# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.

import os
# Функция для создания, переименования и отображения файлов в каталоге
def rename_file():
    # Имена файлов
    original_filename = "temp_file.txt"
    renamed_filename = "renamed_file.txt"

    # Создание файла и запись в него содержимого
    try:
        with open(original_filename, 'w') as file:
            file.write("Temporary content")
        print(f"Файл '{original_filename}' создан и записан.")
    except IOError as e:
        print(f"Ошибка при создании файла: {e}")

    # Переименование файла
    try:
        os.rename(original_filename, renamed_filename)
        print(f"\nФайл '{original_filename}' переименован в '{renamed_filename}'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{original_filename}' не найден.")
    except OSError as e:
        print(f"Ошибка при переименовании файла: {e}")

    # Вывод списка всех файлов в текущем каталоге
    print("\nСписок файлов в текущем каталоге:")
    files_in_directory = [f for f in os.listdir() if os.path.isfile(f)]
    print("\n".join(files_in_directory))

# Запуск программы
rename_file()

# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".

import os

# Функция для проверки существования файла и вывода его размера
def check_file_exists():
    filename = "example.txt"

    # Проверка существования файла
    if os.path.isfile(filename):
        # Получение размера файла в байтах
        file_size = os.path.getsize(filename)
        print(f"Файл '{filename}' существует. Его размер: {file_size} байт.")
    else:
        print("Файл не найден.")

# Запуск программы
check_file_exists()

# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".

import os

# Функция для сравнения размеров файлов
def compare_file_sizes(file1, file2):
    # Проверка существования первого файла
    if not os.path.isfile(file1):
        print(f"Файл '{file1}' не найден.")
        return

    # Проверка существования второго файла
    if not os.path.isfile(file2):
        print(f"Файл '{file2}' не найден.")
        return

    # Получение размеров файлов
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    # Сравнение размеров файлов
    if size1 > size2:
        print(f"Файл '{file1}' больше. Его размер: {size1} байт.")
    elif size1 < size2:
        print(f"Файл '{file2}' больше. Его размер: {size2} байт.")
    else:
        print("Файлы имеют одинаковый размер.")

# Запуск программы с вводом имен файлов
file1 = input("Введите имя первого файла: ")
file2 = input("Введите имя второго файла: ")

compare_file_sizes(file1, file2)

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


import json
import os
from datetime import datetime

# Путь к файлу JSON, где хранится инвентарь
inventory_file = 'inventory.json'

# Лог-файл
log_file = 'inventory_log.txt'

#  Перечень инвентаря
inventory = [
    {'product': "Laptop", 'price': 1000, 'count': 13, 'created_at': '2024-11-20 12:00:00', 'updated_at': '2024-11-20 12:00:00'},
    {'product': "Mouse", 'price': 50, 'count': 1, 'created_at': '2024-11-20 12:00:00', 'updated_at': '2024-11-20 12:00:00'},
    {'product': "Keyboard", 'price': 30, 'count': 33, 'created_at': '2024-11-20 12:00:00', 'updated_at': '2024-11-20 12:00:00'},
    {'product': "Monitor", 'price': 200, 'count': 10, 'created_at': '2024-11-20 12:00:00', 'updated_at': '2024-11-20 12:00:00'}
]

# Загрузка инвентаря из файла
def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as file:
            return json.load(file)
    else:
        save_inventory(inventory)
        return inventory

# Сохранение инвентаря в файл
def save_inventory(inventory):
    with open(inventory_file, 'w') as file:
        json.dump(inventory, file, indent=4)

# Логирование действий
def log_action(action):
    with open(log_file, 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {action}\n")

# Приведение названий товаров к нижнему регистру в целях минимизации ошибки при вводе наименования товара
def normalize_product_name(name):
    return name.strip().lower()

# Функция для показа списка товаров
def show_inventory():
    inventory = load_inventory()
    print("\nСписок товаров:")
    for item in inventory:
        print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

# Добавить товар
def add_product():
    product_name = normalize_product_name(input("Введите название товара: "))
    price = float(input("Введите стоимость товара: "))
    count = int(input("Введите количество товара: "))
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    inventory = load_inventory()
    inventory.append({'product': product_name, 'price': price, 'count': count, 'created_at': now, 'updated_at': now})
    save_inventory(inventory)
    log_action(f"Добавлен товар: {product_name} (цена: {price}, количество: {count})")
    print(f"Товар '{product_name}' добавлен в инвентарь.")

# Удалить товар
def delete_product():
    product_name = normalize_product_name(input("Введите название товара для удаления: "))
    inventory = load_inventory()
    filtered_inventory = [item for item in inventory if normalize_product_name(item['product']) != product_name]
    if len(filtered_inventory) == len(inventory):
        print(f"Товар '{product_name}' не найден.")
        return
    save_inventory(filtered_inventory)
    log_action(f"Удален товар: {product_name}")
    print(f"Товар '{product_name}' удален из инвентаря.")

# Обновить товар
def update_product():
    product_name = normalize_product_name(input("Введите название товара для обновления: "))
    inventory = load_inventory()
    for item in inventory:
        if normalize_product_name(item['product']) == product_name:
            item['price'] = float(input("Введите новую стоимость товара: "))
            item['count'] = int(input("Введите новое количество товара: "))
            item['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_inventory(inventory)
            log_action(f"Обновлен товар: {product_name} (цена: {item['price']}, количество: {item['count']})")
            print(f"Товар '{product_name}' обновлен.")
            return
    print(f"Товар '{product_name}' не найден.")

# Найти товар
def find_product():
    product_name = normalize_product_name(input("Введите название товара для поиска: "))
    inventory = load_inventory()
    for item in inventory:
        if normalize_product_name(item['product']) == product_name:
            print(f"Найден товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            return
    print(f"Товар '{product_name}' не найден.")

# Главное меню
def main():
    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Выход.")

        choice = input("Выберите действие (1-6): ")

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
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 6.")

# Запуск программы
main()












