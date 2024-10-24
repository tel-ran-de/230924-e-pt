# Проект: Перепишите проект из урока 7 в функциональном стиле.
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


def show_inventory(inventory):
    for item in inventory:
        print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")


def add_product(inventory, product, price, count):
    inventory.append({'product': product, 'price': price, 'count': count})
    print(f"Товар '{product}' добавлен.")


def delete_product(inventory, product_name):
    inventory[:] = [item for item in inventory if item['product'] != product_name]
    print(f"Товар '{product_name}' удален.")


def update_product(inventory, product_name, new_product=None, new_price=None, new_count=None):
    for item in inventory:
        if item['product'] == product_name:
            if new_product:
                item['product'] = new_product
            if new_price is not None:
                item['price'] = new_price
            if new_count is not None:
                item['count'] = new_count
            print(f"Товар '{product_name}' обновлен.")
            break


def find_product(inventory, product_name):
    for item in inventory:
        if item['product'] == product_name:
            print(f"Найден товар: {item}")
            return item
    print(f"Товар '{product_name}' не найден.")
    return None


def products_below_price(inventory, price_limit):
    filtered = [item for item in inventory if item['price'] < price_limit]
    print(f"Товары с ценой ниже {price_limit}:")
    show_inventory(filtered)


def products_below_count(inventory, count_limit):
    filtered = [item for item in inventory if item['count'] < count_limit]
    print(f"Товары с количеством ниже {count_limit}:")
    show_inventory(filtered)


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
    print()

    choice = input("Выберите действие: ")

    if choice == "1":
        show_inventory(inventory)
        print()
    elif choice == "2":
        product = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        count = int(input("Введите количество товара: "))
        add_product(inventory, product, price, count)
    elif choice == "3":
        product_name = input("Введите название товара для удаления: ")
        delete_product(inventory, product_name)
    elif choice == "4":
        product_name = input("Введите название товара для обновления: ")
        new_product = input("Новое название (или пропустите): ") or None
        new_price = input("Новая цена (или пропустите): ")
        new_price = float(new_price) if new_price else None
        new_count = input("Новое количество (или пропустите): ")
        new_count = int(new_count) if new_count else None
        update_product(inventory, product_name, new_product, new_price, new_count)
    elif choice == "5":
        product_name = input("Введите название товара для поиска: ")
        find_product(inventory, product_name)
    elif choice == "6":
        price_limit = float(input("Введите максимальную цену: "))
        products_below_price(inventory, price_limit)
    elif choice == "7":
        count_limit = int(input("Введите максимальное количество: "))
        products_below_count(inventory, count_limit)
    elif choice == "8":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")


