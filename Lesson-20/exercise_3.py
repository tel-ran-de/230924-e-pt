# Тема: Интеграционная практика. Мини-проект


# Проект: Перепишите проект из уроков 12-13, 19, добавив в него обработку ошибок, где это необходимо.
#
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

import json
# Проект: Управление инвентарем в интернет-магазине

FILENAME = 'inventory.json'

def load_inventory(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_inventory(filename, inventory):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(inventory, file, indent=4)


def show_inventory(inventory):
    for item in inventory:
        print(item)


def add_item(inventory, product, price, count):
    inventory.append({'product': product, 'price': price, 'count': count})
    save_inventory(FILENAME, inventory)


def remove_item(inventory, product):
    inventory[:] = [item for item in inventory if item['product'] != product]


def update_item(inventory, product, price=None, count=None):
    for item in inventory:
        if item['product'] == product:
            if price is not None:
                item['price'] = price
            if count is not None:
                item['count'] = count


def find_item(inventory, product):
    return [item for item in inventory if item['product'] == product]


def filter_by_price(inventory, max_price):
    return [item for item in inventory if item['price'] < max_price]


def filter_by_count(inventory, max_count):
    return [item for item in inventory if item['count'] < max_count]


# Пример использования
inventory = load_inventory(FILENAME)
# Меню
while True:
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить название товара, стоимость или количество.")
    print("5. Найти товар по названию.")
    print("6. Вывести список товаров меньше определнной стоимости.")
    print("7. Вывести список товаров меньше определенного количества.")
    print("8. Выйти.")

    choice = input("Выберите опцию: ")

    if choice == '1':
        show_inventory(inventory)
    elif choice == '2':
        product = input("Введите название товара: ")
        price = float(input("Введите стоимость товара: "))
        count = int(input("Введите количество товара: "))
        add_item(inventory, product, price, count)
    elif choice == '3':
        product = input("Введите название товара для удаления: ")
        remove_item(inventory, product)
    elif choice == '4':
        product = input("Введите название товара для обновления: ")
        price = input("Введите новую стоимость (или нажмите Enter для пропуска): ")
        count = input("Введите новое количество (или нажмите Enter для пропуска): ")
        update_item(inventory, product, float(price) if price else None, int(count) if count else None)
    elif choice == '5':
        product = input("Введите название товара для поиска: ")
        found_items = find_item(inventory, product)
        if found_items:
            for item in found_items:
                print(item)
        else:
            print("Товар не найден.")
    elif choice == '6':
        max_price = float(input("Введите максимальную стоимость: "))
        filtered_items = filter_by_price(inventory, max_price)
        for item in filtered_items:
            print(item)
    elif choice == '7':
        max_count = int(input("Введите максимальное количество: "))
        filtered_items = filter_by_count(inventory, max_count)
        for item in filtered_items:
            print(item)
    elif choice == '8':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")









