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
print("Задача 1.1")
employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}
print("----------------------")
print("1. Список сотрудников:")
for name in employees:
    print(f"{name}")
print("----------------------")
summa = sum(employee["salary"] for employee in employees.values())
print(f"2. Общая зарплата сотрудников: {summa}")
print("----------------------")
print("3. Добавляем нового сотрудника:")
employees["David"] = {"age": 28, "department": "IT", "salary": 6500}
for name in employees:
    print(f"{name}")
print("-----------------------")
print("4. Поднимаем зарплату Alice до 5500")
employees["Alice"] ["salary"] = 5500
print(employees)
print("_______________________")
print("Удаляем сотрудника Charlie")
del employees["Charlie"]
print(employees)
print("-----------------------")
print("Данные о каждом сотруднике")
for name, info in employees.items():
    print(f"Имя: {name}, Возоаст: {info["age"]}, Отдел: {info["department"]}, Зарплата: {info["salary"]}")
print("------------------------")

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
print("Задача 1.2")
inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}
print("---------------------")
print("1. Название всех товаров")
for name in inventory:
    print(f"{name}")
print("----------------------")
print("2. Увеличить количество яблок на 10")
inventory["Apples"]["quantity"] += 10
print(inventory)
print("----------------------")
print("3. Изменить цену бананов на 1,5")
inventory["Bananas"]["price"] = 1.5
print(inventory)
print("----------------------")
print("4. Удалить товар Черри")
del inventory["Cherries"]
print(inventory)
print("----------------------")
print("5. Добавить новый товар - финики количеством 15 и ценой 4")
inventory["Dates"] = {"quantity": 15, "price": 4}
print(inventory)
print("----------------------")

total_cost = 0
for item, details in inventory.items():
    total_cost += details["quantity"] * details["price"]
print(f"Общая стоимость товаров: {total_cost}")
print("-----------------------")


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
print("Задача 2.1")
coordinates = [(10, 20), (30, 40), (50, 60)]
print("-----------------------")
print("1. Выводим все координаты: ")
for x, y in coordinates:
    print(f"X {x}, Y {y}")
print("------------------------")
sum_y = sum(y for x, y in coordinates)
print(f"2. Сумма всех координат по оси 'Y': {sum_y}")
print("-------------------------")
print("3. Добавляем новую координату (70, 80)")
coordinates.append((70, 80))
print(coordinates)
print("--------------------------")
print("4. 4. Заменить первую координату на (15, 25)")
coordinates[0] = (15, 25)
print(coordinates)
print("--------------------------")
print("5. Все координаты, отсортированные по оси x:")
sort_x = sorted(coordinates)
for x, y in sort_x:
    print(f"({x}, {y})")
print("---------------------------")

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

print("Задача 2.2")
print("-----------------------------")
print("1. Все продукты:")
for product, price in products:
    print(f"{product}")
print("-----------------------------")
total_cost = sum(price for _, price in products)
print(f"2. Сумарная стоимомть всех продуктов: {total_cost}")
print("------------------------------")
print("3. Добавить новый продукт 'Date' с ценой 4")
products.append(("Date", 4))
print(products)
print("------------------------------")
print("4. Заменить цену 'Apple' на 2.5")
products[0] = ("Apple", 2.5)
print(products)
print("------------------------------")
print("5. Вывести все продукты, отсортированные по цене")
sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)
print("-------------------------------")


# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
#
# Задание:
# 1. Выведите всех пользователей.
# 2. Добавьте нового пользователя "David".
# 3. Удалите пользователя "Bob".
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
# 5. Выведите количество пользователей.
print("Задача 2.3")

users = {"Alice", "Bob", "Charlie"}
print("1. Выведите всех пользователей")
for user in users:
    print(f"{user}")
print("-----------------------")
print("2. Добавьте нового пользователя 'David'")
users.add("David")
print(users)
print("------------------------")
print("3. Удалите пользователя 'Bob'")
users.remove("Bob")
print(users)
print("------------------------")
print("4. Проверьте, есть ли пользователь 'Alice' в множестве")
if 'Alice' in users:
    print(True)
print("------------------------")
print("5. Выведите количество пользователей")
print(len(users))
print("-------------------------")

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

print("Задача 2.4.1")
print("-------------------------")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("1. Выведите элементы обоих множеств.")
print(set1, set2)
print("-------------------------")
print("2. Найдите объединение двух множеств")
print(set1 | set2)
print("-------------------------")
print("3. Найдите пересечение двух множеств.")
print(set1 & set2)
print("-------------------------")
print("4. Найдите разность множеств `set1` и `set2`")
print(set1 - set2)
print("--------------------------")
print("5. Проверьте, является ли `set2` подмножеством `set1`")
is_subset = set2.issubset(set1)
print(is_subset)
print("--------------------------")

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

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]

