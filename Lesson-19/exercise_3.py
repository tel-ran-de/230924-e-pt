# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле.
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

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

import json#импортирую библиотеку джейсон чтоб работать с JSON-файлом, который используются для хранения данных.

# Файл для хранения данных
FILE_NAME = 'inventory.json'

# Функция для чтения данных из файла. Эта функция открывает файл inventory.json для чтения
# и загружает данные из него. Если файл не найден, возвращается пустой список
def read_inventory():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Функция для записи данных в файл
#аписываю данные в файл inventory.json в формате JSON с отступами для удобства чтения.
def write_inventory(inventory):
    with open(FILE_NAME, 'w') as file:
        json.dump(inventory, file, indent=4)

# Функция для отображения списка товаров
# читаем данные из файла и выводим на экран список всех товаров с их названиями, ценами и количеством.
def show_inventory():
    inventory = read_inventory()
    for item in inventory:
        print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")

# Функция для добавления товара.
# функция добавляет новый товар в список, а затем записывает обновленный список в файл.
def add_product(product, price, count):
    inventory = read_inventory()
    inventory.append({'product': product, 'price': price, 'count': count})
    write_inventory(inventory)

# Функция для удаления товара.
# функция удаляет товар из списка по его названию и записывает обновленный список в файл.
def delete_product(product):
    inventory = read_inventory()
    inventory = [item for item in inventory if item['product'] != product]
    write_inventory(inventory)

# Функция для обновления товара.
# функция обновляет название, цену или количество товара в списке и записывает обновленный список в файл.
def update_product(product, new_name=None, new_price=None, new_count=None):
    inventory = read_inventory()
    for item in inventory:
        if item['product'] == product:
            if new_name:
                item['product'] = new_name
            if new_price is not None:
                item['price'] = new_price
            if new_count is not None:
                item['count'] = new_count
    write_inventory(inventory)

# Функция для поиска товара по названию.
# функция ищет товар по названию и выводит его данные, если товар найден.
# Если товар не найден, выводится сообщение об этом
def find_product(product):
    inventory = read_inventory()
    for item in inventory:
        if item['product'] == product:
            print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
            return
    print("Product not found")

# Функция для вывода товаров с ценой ниже заданной.
# функция выводит на экран товары, цена которых ниже заданного значения.
def products_below_price(price):
    inventory = read_inventory()
    for item in inventory:
        if item['price'] < price:
            print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")

# Функция для вывода товаров с количеством ниже заданного.
# функция выводит на экран товары, количество которых ниже заданного значения.
def products_below_count(count):
    inventory = read_inventory()
    for item in inventory:
        if item['count'] < count:
            print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")

# Пример использования, меню для взаимодействия с пользователем
if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров меньше определенной стоимости.")
        print("7. Вывести список товаров меньше определенного количества.")
        print("8. Выйти.")

        choice = input("Выберите опцию: ")

        if choice == '1':
            show_inventory()
        elif choice == '2':
            product = input("Введите название товара: ")
            price = float(input("Введите цену товара: "))
            count = int(input("Введите количество товара: "))
            add_product(product, price, count)
        elif choice == '3':
            product = input("Введите название товара для удаления: ")
            delete_product(product)
        elif choice == '4':
            product = input("Введите название товара для обновления: ")
            new_name = input("Введите новое название (или оставьте пустым): ")
            new_price = input("Введите новую цену (или оставьте пустым): ")
            new_count = input("Введите новое количество (или оставьте пустым): ")
            update_product(product, new_name or None, float(new_price) if new_price else None, int(new_count) if new_count else None)
        elif choice == '5':
            product = input("Введите название товара для поиска: ")
            find_product(product)
        elif choice == '6':
            price = float(input("Введите максимальную цену: "))
            products_below_price(price)
        elif choice == '7':
            count = int(input("Введите максимальное количество: "))
            products_below_count(count)
        elif choice == '8':
            break
        else:
            print("Неверный выбор, попробуйте снова.")




