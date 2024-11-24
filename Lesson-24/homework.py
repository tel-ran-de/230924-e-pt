# Тема: Модуль datetime
from datetime import datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45

print("-----------------------------Тема: Модуль datetime----------------------------------")
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)

# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

# # Функция для вычисления возраста
def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
    today = datetime.today()
    result = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return result

bd = input("Введите дату рождения в формате DD.MM.YYYY: ")
age = calculate_age(bd)
print(f"Ваш возраст: {age} лет")


# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.

def days_until_event(event_date):
    event_date = datetime.strptime(event_date, "%Y-%m-%d").date()   # Преобразование строки в объект даты
    today = datetime.today().date()

    days_remaining = (event_date - today).days  # Вычисление разницы в днях

    if days_remaining < 0:
        return "Мероприятие уже прошло!"    # Проверка на прошедшую дату
    return days_remaining

event_date_input = input("Введите дату следующего мероприятия в формате YYYY-MM-DD: ")
try:
    result = days_until_event(event_date_input)
    if isinstance(result, int):
        print(f"До мероприятия осталось {result} дней.")
    else:
        print(result)
except ValueError:
    print("Ошибка: Некорректный формат даты. Используйте YYYY-MM-DD.")

# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.

# определения дня недели
def get_day_of_week(date_input):
    # Преобразование строки в объект даты
    date = datetime.strptime(date_input, "%Y-%m-%d").date()
    # Получение дня недели
    day_of_week = date.strftime("%A")  # Полное название дня недели
    return day_of_week

date_input = input("Введите дату в формате YYYY-MM-DD: ")
try:
    day_of_week = get_day_of_week(date_input)
    print(f"День недели для даты {date_input}: {day_of_week}")
except ValueError:
    print("Ошибка: Некорректный формат даты. Используйте YYYY-MM-DD.")

# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.


def compare_dates(date1, date2):
    # Преобразование строк в объекты даты
    date1 = datetime.strptime(date1, "%Y-%m-%d").date()
    date2 = datetime.strptime(date2, "%Y-%m-%d").date()

    if date1 > date2:
        return f"Дата {date1} позже даты {date2}."
    elif date1 < date2:
        return f"Дата {date1} раньше даты {date2}."
    else:
        return f"Дата {date1} совпадает с датой {date2}."

date1_input = input("Введите первую дату в формате YYYY-MM-DD: ")
date2_input = input("Введите вторую дату в формате YYYY-MM-DD: ")

try:
    result = compare_dates(date1_input, date2_input)
    print(result)
except ValueError:
    print("Ошибка: Некорректный формат даты. Используйте YYYY-MM-DD.")


# Тема: Модуль os
print("-----------------------------Тема: Модуль os----------------------------------")

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.
import os


def create_and_remove_directory():
    dir_name = "test_directory"

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Директория '{dir_name}' создана.")
    else:
        print(f"Директория '{dir_name}' уже существует.")

    all_dirs = [d for d in os.listdir() if os.path.isdir(d)]
    print("Список всех директорий в текущем каталоге:")
    print(all_dirs)

    if os.path.exists(dir_name): # Удаление
        os.rmdir(dir_name)
        print(f"Директория '{dir_name}' удалена.")
    else:
        print(f"Директория '{dir_name}' не существует для удаления.")


# Вызов функции
create_and_remove_directory()

# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.

def create_and_rename_file():
    original_file = "temp_file.txt"
    renamed_file = "renamed_file.txt"

    with open(original_file, "w") as file:  # запись строки
        file.write("Temporary content")
    print(f"Файл '{original_file}' создан и содержимое записано.")

    if os.path.exists(original_file):   # Переименование файла
        os.rename(original_file, renamed_file)
        print(f"Файл '{original_file}' переименован в '{renamed_file}'.")
    else:
        print(f"Файл '{original_file}' не существует для переименования.")

    # Список всех файлов
    all_files = [f for f in os.listdir() if os.path.isfile(f)]
    print("Список всех файлов в текущем каталоге:")
    print(all_files)

create_and_rename_file()


# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".

def check_file_existence():
    file_name = "examples.py"

    if os.path.exists(file_name) and os.path.isfile(file_name):
        file_size = os.path.getsize(file_name)
        print(f"Файл '{file_name}' существует. Его размер: {file_size} байт.")
    else:
        print(f"Файл '{file_name}' не найден.")

check_file_existence()


# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".

def compare_file_sizes(file1, file2):
    if not os.path.exists(file1):
        print(f"Файл '{file1}' не найден.")
        return
    if not os.path.exists(file2):
        print(f"Файл '{file2}' не найден.")
        return

    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    if size1 > size2:
        print(f"Файл '{file1}' больше, его размер: {size1} байт.")
    elif size1 < size2:
        print(f"Файл '{file2}' больше, его размер: {size2} байт.")
    else:
        print("Файлы имеют одинаковый размер.")

file_name1 = input("Введите имя первого файла: ")
file_name2 = input("Введите имя второго файла: ")
compare_file_sizes(file_name1, file_name2)

# Тема: Интеграционная практика.
print("--------------------------Тема: Интеграционная практика.------------------------------")
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

# Тема: Интеграционная практика.

# Проект: Перепишите проект из уроков 12-13, 19-20, добавив в него фичи 1 - 3 на основе модулей datetime и os.
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
# 6. Вывести список товаров меньше определенной стоимости.
# 7. Вывести список товаров меньше определенного количества.
# Фильтрация по цене
import json
import os
import shutil
from datetime import datetime
from tabulate import tabulate


# Файлы для хранения данных
inventory_file = 'inventory.json'
log_file = 'actions.log'

# Функция для поиска последнего резервного файла
def get_latest_backup():
    backups = [file for file in os.listdir() if file.startswith("backup_") and file.endswith(".json")]
    if not backups:
        return None
    backups.sort(key=lambda name: datetime.strptime(name, "backup_%H-%M-%S_%d-%m-%Y.json"), reverse=True)
    return backups[0]

# Резервное копирование данных
def backup_inventory():
    backup_name = f"backup_{datetime.now().strftime('%H-%M-%S_%d-%m-%Y')}.json"
    try:
        if os.path.exists(inventory_file):
            shutil.copy(inventory_file, backup_name)
            print(f"Резервная копия создана: {backup_name}")
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")

# Логирование действий
def log_action(action, details=""):
    try:
        with open(log_file, 'a', encoding='utf-8') as log:
            log.write(f"{datetime.now().strftime('%H:%M:%S %d.%m.%Y')} | {action} | {details}\n")
    except Exception as e:
        print(f"Ошибка записи в лог: {e}")

# Проверка существования файла инвентаря
if not os.path.exists(inventory_file):
    inventory = [
        {'product': "Laptop", 'price': 1000, 'count': 13, 'created_at': str(datetime.now()), 'updated_at': str(datetime.now())},
        {'product': "Mouse", 'price': 50, 'count': 1, 'created_at': str(datetime.now()), 'updated_at': str(datetime.now())},
        {'product': "Keyboard", 'price': 30, 'count': 33, 'created_at': str(datetime.now()), 'updated_at': str(datetime.now())},
        {'product': "Monitor", 'price': 200, 'count': 10, 'created_at': str(datetime.now()), 'updated_at': str(datetime.now())}
    ]
    with open(inventory_file, 'w', encoding='utf-8') as file:
        json.dump(inventory, file, ensure_ascii=False, indent=4)

# Загрузка инвентаря
def load_inventory():
    try:
        with open(inventory_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Основной файл повреждён или отсутствует. Попытка загрузить данные из последнего резервного файла...")
        latest_backup = get_latest_backup()
        if latest_backup:
            try:
                with open(latest_backup, 'r', encoding='utf-8') as backup_file:
                    print(f"Загрузка данных из резервного файла: {latest_backup}")
                    return json.load(backup_file)
            except Exception as e:
                print(f"Ошибка при загрузке резервного файла: {e}")
        print("Резервные файлы не найдены. Возвращён пустой инвентарь.")
        return []

# Сохранение инвентаря
def save_inventory(inventory):
    try:
        with open(inventory_file, 'w', encoding='utf-8') as file:
            json.dump(inventory, file, ensure_ascii=False, indent=4)
    except Exception as e:
        log_action("Ошибка сохранения данных", str(e))
        print(f"Ошибка при сохранении данных: {e}")

# Вывод инвентаря
def print_inventory(items=None):
    if items is None:
        items = load_inventory()
    if not items:
        print("Инвентарь пуст.")
    else:
        headers = ["Название товара", "Цена", "Количество", "Создано", "Обновлено"]
        table = [[item['product'], item['price'], item['count'], item['created_at'], item['updated_at']] for item in items]
        print(tabulate(table, headers=headers, tablefmt="grid"))

# Добавление товара
def add_product():
    inventory = load_inventory()
    product = input("Введите название товара: ").strip()
    for item in inventory:
        if item['product'].lower() == product.lower():
            print("Товар уже существует.")
            return
    try:
        price = int(input("Введите цену товара: "))
        count = int(input("Введите количество товара: "))
        timestamp = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        new_product = {'product': product, 'price': price, 'count': count, 'created_at': timestamp, 'updated_at': timestamp}
        inventory.append(new_product)
        save_inventory(inventory)
        log_action("Добавление товара", f"Товар: {product}, Цена: {price}, Количество: {count}")
        print("Товар добавлен.")
        print_inventory([new_product])  # Вывод добавленного товара в формате таблицы
    except ValueError:
        log_action("Ошибка ввода данных", "Неверный формат цены или количества")
        print("Ошибка: неверный формат данных.")

# Удаление товара
def delete_product():
    inventory = load_inventory()
    product = input("Введите название товара для удаления: ").strip()
    updated_inventory = [item for item in inventory if item['product'].lower() != product.lower()]
    if len(updated_inventory) == len(inventory):
        print("Товар не найден.")
        return
    save_inventory(updated_inventory)
    log_action("Удаление товара", f"Товар: {product}")
    print("Товар удалён.")

# Обновление товара
def update_product():
    inventory = load_inventory()
    product = input("Введите название товара для обновления: ").strip()
    for item in inventory:
        if item['product'].lower() == product.lower():
            try:
                item['price'] = int(input("Введите новую цену: "))
                item['count'] = int(input("Введите новое количество: "))
                item['updated_at'] = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
                save_inventory(inventory)
                log_action("Обновление товара", f"Товар: {product}, Новая цена: {item['price']}, Новое количество: {item['count']}")
                print("Товар обновлён.")
                print_inventory([item])  # Вывод обновленного товара в формате таблицы
                return
            except ValueError:
                log_action("Ошибка ввода данных", "Неверный формат цены или количества")
                print("Ошибка: неверный формат данных.")
                return
    log_action("Ошибка обновления товара", f"Товар '{product}' не найден")
    print("Товар не найден.")

# Поиск товара
def search_product():
    inventory = load_inventory()
    product = input("Введите название товара для поиска: ").strip()
    for item in inventory:
        if item['product'].lower() == product.lower():
            headers = ["Название товара", "Цена", "Количество", "Создано", "Обновлено"]
            table = [[item['product'], item['price'], item['count'], item['created_at'], item['updated_at']]]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            return
    print("Товар не найден.")
def filter_by_price():
    inventory = load_inventory()
    try:
        max_price = int(input("Введите максимальную цену: "))
        filtered = [item for item in inventory if item['price'] <= max_price]
        if not filtered:
            print("Нет товаров дешевле указанной цены.")
        else:
            headers = ["Название товара", "Цена", "Количество", "Создано", "Обновлено"]
            table = [[item['product'], item['price'], item['count'], item['created_at'], item['updated_at']] for item in filtered]
            print(tabulate(table, headers=headers, tablefmt="grid"))
    except ValueError:
        print("Ошибка: введите числовое значение для цены.")

# Фильтрация по количеству
def filter_by_count():
    inventory = load_inventory()
    try:
        max_count = int(input("Введите максимальное количество: "))
        filtered = [item for item in inventory if item['count'] <= max_count]
        if not filtered:
            print("Нет товаров с количеством ниже указанного.")
        else:
            headers = ["Название товара", "Цена", "Количество", "Создано", "Обновлено"]
            table = [[item['product'], item['price'], item['count'], item['created_at'], item['updated_at']] for item in filtered]
            print(tabulate(table, headers=headers, tablefmt="grid"))
    except ValueError:
        print("Ошибка: введите числовое значение для количества.")

# Меню программы
def menu():
    backup_inventory()
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

if __name__ == "__main__":
    menu()










