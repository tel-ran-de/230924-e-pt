# Тема: словари

# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".

# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
#
employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}
# 1. Выведите имена всех сотрудников.
names = employees.keys()
print("Имена всех сотрудников:", list(names))

# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
total_sum = sum(employee["salary"] for employee in employees.values())
print(f"Обшая сумма:", total_sum )

# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
employees["David"] = {"age": 28, "department": "IT", "salary": 6500}
print(f"Добавлен сотрудник Давид", employees )

# 4. Обновите зарплату "Alice" до 5500.
employees["Alice"]["salary"] = 5500
print(f"Обновление зарплати Алиси", employees["Alice"]["salary"])

# 5. Удалите сотрудника "Charlie".
del employees["Charlie"]
print("Удален сотрудник Чарл")

print("---------------")

# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
#
inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}
# 1. Выведите названия всех товаров.
names = inventory.keys()
print(names)

# 2. Увеличьте количество "Apples" на 10.
inventory["Apples"]["quantity"] = 30+10
print("Количество яблок увеличено -", inventory["Apples"]["quantity"])

# 3. Измените цену "Bananas" на 1.5.
inventory["Bananas"]["price"] = 1.5
print("Цена на бананы изменен -", inventory["Bananas"]["price"])

# 4. Удалите товар "Cherries".
del inventory["Cherries"]
print(f"Товар Черри удален")

# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
inventory["Dates"] = {"quantity": 15, "price": 4}
print("добавлен Dates -", inventory)

# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений)

total_sum = sum(inventor["price"] * inventor["quantity"] for inventor in inventory.values())
print(f"Обшая сумма:", total_sum )

print("--------------")


# Тема: кортежи и множества.

# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все координаты.
# 2. Найдите сумму всех координат по оси x и по оси y.
# 3. Добавьте новую координату (70, 80).
# 4. Замените первую координату на (15, 25).
# 5. Выведите все координаты, отсортированные по оси x.
#
coordinates = [(10, 20), (30, 40), (50, 60)]

# 1. Выведите все координаты
for coord in coordinates:
    print(coord)

# 2. Найдите сумму всех координат по оси x и по оси y.
sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print(f"\nСумма координат по оси x: {sum_x}")
print(f"Сумма координат по оси y: {sum_y}")

# 3. Добавьте новую координату (70, 80).
coordinates.append((70, 80))
print("Добавлен координаты-", coordinates)

# 4. Замените первую координату на (15, 25).
coordinates[0] = (15, 25)
print("Замена первого координата -", coordinates)

# 5. Выведите все координаты, отсортированные по оси x.
coord_x = sorted(x for x, y in coordinates)
print("все координаты по оси x -", coord_x)

print("----------")

# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все продукты.
# 2. Найдите суммарную стоимость всех продуктов.
# 3. Добавьте новый продукт "Date" с ценой 4.
# 4. Замените цену "Apple" на 2.5.
# 5. Выведите все продукты, отсортированные по цене.
#
products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]

# 1. Выведите все продукты.
for product in products:
    print(product[0], end=" ")

print()
# 2. Найдите суммарную стоимость всех продуктов.
total_sum = sum(price for name, price in products)
print("Суммарная стоимость всех продуктов:", total_sum)

# 3. Добавьте новый продукт "Date" с ценой 4.
products.append(("Date", 4))
print(products)

# 4. Замените цену "Apple" на 2.5.
products = [(name,  2.5) if name == "Apple" else (name, price) for name, price in products]
print("Замена цену на Apple --", products)

# 5. Выведите все продукты, отсортированные по цене.
sorted_products = sorted(products, key=lambda product: product[1])
print(sorted_products)

print("---------")


# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
#
# Задание:
# 1. Выведите всех пользователей.
# 2. Добавьте нового пользователя "David".
# 3. Удалите пользователя "Bob".
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
# 5. Выведите количество пользователей.
#
users = {"Alice", "Bob", "Charlie"}

# 1. Выведите всех пользователей.
print(*users)

# 2. Добавьте нового пользователя "David".
users.add("David")
print(*users)

# 3. Удалите пользователя "Bob".
users.remove("Bob")
print(*users)

# 4. Проверьте, есть ли пользователь "Alice" в множестве.
if "Alice" in users:
    print("DA")
else:
    print("NET")

# 5. Выведите количество пользователей.
print(len(users))

print("-------------")

# Задача 4: Управление наборами данных


# У вас есть два множества, представляющих различные наборы данных.
# Необходимо провести различные операции с этими множествами.
#
# Задание:
# 1. Выведите элементы обоих множеств.
# 2. Найдите объединение двух множеств.
# 3. Найдите пересечение двух множеств.
# 4. Найдите разность множеств `set1` и `set2`.
# 5. Проверьте, является ли `set2` подмножеством `set1`.
#
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Выведите элементы обоих множеств.
print("Множество 1:", set1)
print("Множество 2:", set2)

# 2. Найдите объединение двух множеств.

union_set = set1 | set2
print("Объединение -", union_set)

# 3. Найдите пересечение двух множеств.
intersection_set = set1 & set2
print("Пересечение -", intersection_set)

# 4. Найдите разность множеств `set1` и `set2`.
diference_set = set1 - set2
print("Раность -", diference_set)

# 5. Проверьте, является ли `set2` подмножеством `set1`.
is_subset = set2.issubset(set1)
print(is_subset)

print("--------")

# Проект: Управление инвентарем в интернет-магазине
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

def show_inventory():
    for item in inventory:
        print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def add_product():
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': name, 'price': price, 'count': count})
    print(f"Товар {name} добавлен в инвентарь.")

def delete_product():
    name = input("Введите название товара для удаления: ")
    global inventory
    inventory = [item for item in inventory if item['product'] != name]
    print(f"Товар {name} удален из инвентаря.")

def update_product():
    name = input("Введите название товара для обновления: ")
    for item in inventory:
        if item['product'] == name:
            item['price'] = float(input("Введите новую цену товара: "))
            item['count'] = int(input("Введите новое количество товара: "))
            print(f"Товар {name} обновлен.")
            break
    else:
        print(f"Товар {name} не найден.")

def find_product():
    name = input("Введите название товара для поиска: ")
    for item in inventory:
        if item['product'] == name:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            break
    else:
        print(f"Товар {name} не найден.")

def products_below_price():
    price = float(input("Введите максимальную цену: "))
    for item in inventory:
        if item['price'] < price:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def products_below_count():
    count = int(input("Введите минимальное количество: "))
    for item in inventory:
        if item['count'] < count:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def menu():
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
            products_below_price()
        elif choice == '7':
            products_below_count()
        elif choice == '8':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

menu()
