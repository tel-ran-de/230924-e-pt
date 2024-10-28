```python
# Тема: словари

# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.

# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"

employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}

# 1. Выведите имена всех сотрудников.
print("Имена всех сотрудников:")
for name in employees.keys():
    print(name)

# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
total_salary = sum(employee["salary"] for employee in employees.values())
print(f"\nОбщая сумма зарплат всех сотрудников: {total_salary}")

# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
employees["David"] = {"age": 28, "department": "IT", "salary": 6500}

# 4. Обновите зарплату "Alice" до 5500.
employees["Alice"]["salary"] = 5500

# 5. Удалите сотрудника "Charlie".
del employees["Charlie"]

# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
print("\nДанные о каждом сотруднике:")
for name, details in employees.items():
    print(f"Имя: {name}, Возраст: {details['age']}, Отдел: {details['department']}, Зарплата: {details['salary']}")

# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.

# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).

inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

# 1. Выведите названия всех товаров.
print("\nНазвания всех товаров:")
for item in inventory.keys():
    print(item)

# 2. Увеличьте количество "Apples" на 10.
inventory["Apples"]["quantity"] += 10

# 3. Измените цену "Bananas" на 1.5.
inventory["Bananas"]["price"] = 1.5

# 4. Удалите товар "Cherries".
del inventory["Cherries"]

# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
inventory["Dates"] = {"quantity": 15, "price": 4}

# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
total_cost = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"\nОбщая стоимость всех товаров: {total_cost}")

# Тема: кортежи и множества.

# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.

# Задание:
# 1. Выведите все координаты.
# 2. Найдите сумму всех координат по оси x и по оси y.
# 3. Добавьте новую координату (70, 80).
# 4. Замените первую координату на (15, 25).
# 5. Выведите все координаты, отсортированные по оси x.

coordinates = [(10, 20), (30, 40), (50, 60)]

# 1. Выведите все координаты.
print("\nВсе координаты:")
for coord in coordinates:
    print(coord)

# 2. Найдите сумму всех координат по оси x и по оси y.
sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print(f"\nСумма всех координат по оси x: {sum_x}, по оси y: {sum_y}")

# 3. Добавьте новую координату (70, 80).
coordinates.append((70, 80))

# 4. Замените первую координату на (15, 25).
coordinates[0] = (15, 25)

# 5. Выведите все координаты, отсортированные по оси x.
sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
print("\nВсе координаты, отсортированные по оси x:")
for coord in sorted_coordinates:
    print(coord)

# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.

# Задание:
# 1. Выведите все продукты.
# 2. Найдите суммарную стоимость всех продуктов.
# 3. Добавьте новый продукт "Date" с ценой 4.
# 4. Замените цену "Apple" на 2.5.
# 5. Выведите все продукты, отсортированные по цене.

products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]

# 1. Выведите все продукты.
print("\nВсе продукты:")
for product in products:
    print(product)

# 2. Найдите суммарную стоимость всех продуктов.
total_price = sum(price for name, price in products)
print(f"\nСуммарная стоимость всех продуктов: {total_price}")

# 3. Добавьте новый продукт "Date" с ценой 4.
products.append(("Date", 4))

# 4. Замените цену "Apple" на 2.5.
products = [("Apple", 2.5) if name == "Apple" else (name, price) for name, price in products]

# 5. Выведите все продукты, отсортированные по цене.
sorted_products = sorted(products, key=lambda x: x[1])
print("\nВсе продукты, отсортированные по цене:")
for product in sorted_products:
    print(product)

# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.

# Задание:
# 1. Выведите всех пользователей.
# 2. Добавьте нового пользователя "David".
# 3. Удалите пользователя "Bob".
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
# 5. Выведите количество пользователей.

users = {"Alice", "Bob", "Charlie"}

# 1. Выведите всех пользователей.
print("\nВсе пользователи:")
for user in users:
    print(user)

# 2. Добавьте нового пользователя "David".
users.add("David")

# 3. Удалите пользователя "Bob".
users.remove("Bob")

# 4. Проверьте, есть ли пользователь "Alice" в множестве.
is_alice_present = "Alice" in users
print(f"\nПользователь 'Alice' в множестве: {is_alice_present}")

# 5. Выведите количество пользователей.
print(f"\nКоличество пользователей: {len(users)}")

# Задача 4: Управление наборами данных
# У вас есть два множества, представляющих различные наборы данных.
# Необходимо провести различные операции с этими множествами.

# Задание:
# 1. Выведите элементы обоих множеств.
# 2. Найдите объединение двух множеств.
# 3. Найдите пересечение двух множеств.
# 4. Найдите разность множеств `set1` и `set2`.
# 5. Проверьте, является ли `set2` подмножеством `set1`.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Выведите элементы обоих множеств.
print("\nЭлементы множества set1:")
for elem in set1:
    print(elem)

print("\nЭлементы множества set2:")
for elem in set2:
    print(elem)

# 2. Найдите объединение двух множеств.
union_set = set1.union(set2)
print(f"\nОбъединение множеств: {union_set}")

# 3. Найдите пересечение двух множеств.
intersection_set = set1.intersection(set2)
print(f"\nПересечение множеств: {intersection_set}")

# 4. Найдите разность множеств `set1` и `set2`.
difference_set = set1.difference(set2)
print(f"\nРазность множеств set1 и set2: {difference_set}")

# 5. Проверьте, является ли `set2` подмножеством `set1`.
is_subset = set2.issubset(set1)
print(f"\nЯвляется ли set2 подмножеством set1: {is_subset}")

# Проект: Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.

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
    print("\nСписок товаров:")
    for item in inventory:
        print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def add_item():
    product = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': product, 'price': price, 'count': count})

def remove_item():
    product = input("Введите название товара для удаления: ")
    inventory[:] = [item for item in inventory if item['product'] != product]

def update_item():
    product = input("Введите название товара для обновления: ")
    for item in inventory:
        if item['product'] == product:
            item['product'] = input("Введите новое название товара: ")
            item['price'] = float(input("Введите новую цену товара: "))
            item['count'] = int(input("Введите новое количество товара: "))
            break

def find_item():
    product = input("Введите название товара для поиска: ")
    for item in inventory:
        if item['product'] == product:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            break
    else:
        print("Товар не найден.")

def show_items_below_price():
    price = float(input("Введите максимальную цену: "))
    for item in inventory:
        if item['price'] < price:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def show_items_below_count():
    count = int(input("Введите максимальное количество: "))
    for item in inventory:
        if item['count'] < count:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

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

    choice = input("Выберите действие: ")

    if choice == '1':
        show_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        update_item()
    elif choice == '5':
        find_item()
    elif choice == '6':
        show_items_below_price()
    elif choice == '7':
        show_items_below_count()
    elif choice == '8':
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
```