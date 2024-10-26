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
# employees = {
#     "Alice": {"age": 30, "department": "HR", "salary": 5000},
#     "Bob": {"age": 25, "department": "IT", "salary": 6000},
#     "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
# }

employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}}

for name in employees.keys():
    print(name)

total_salary = sum(employee["salary"] for employee in employees.values())
print(f"\nОбщая сумма зарплат всех сотрудников: {total_salary}")

employees["David"] = {"age": 28, "department": "IT", "salary": 6500}

employees["Alice"]["salary"] = 5500

del employees["Charlie"]

for name, details in employees.items():
    print(f"Имя: {name}, Возраст: {details['age']}, Отдел: {details['department']}, Зарплата: {details['salary']}")




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
# inventory = {
#     "Apples": {"quantity": 50, "price": 2},
#     "Bananas": {"quantity": 30, "price": 1},
#     "Cherries": {"quantity": 20, "price": 3},
# }


inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

for product in inventory.keys():
    print(product)

inventory["Apples"]["quantity"] += 10

inventory["Bananas"]["price"] = 1.5

del inventory["Cherries"]

inventory["Dates"] = {"quantity": 15, "price": 4}

total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"\nОбщая стоимость всех товаров: {total_value}")



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
# coordinates = [(10, 20), (30, 40), (50, 60)]

coordinates = [(10, 20), (30, 40), (50, 60)]
for coord in coordinates:
    print(coord)

sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print(f"\nСумма координат по оси x: {sum_x}")
print(f"Сумма координат по оси y: {sum_y}")

coordinates.append((70, 80))

coordinates[0] = (15, 25)

sorted_coordinates = sorted(coordinates, key=lambda coord: coord[0])
print("\nКоординаты, отсортированные по оси x:")
for coord in sorted_coordinates:
    print(coord)



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
# products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]


products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
for product in products:
    print(product)

total_cost = sum(price for name, price in products)
print(f"\nСуммарная стоимость всех продуктов: {total_cost}")

products.append(("Date", 4))

products = [(name, 2.5) if name == "Apple" else (name, price) for name, price in products]

sorted_products = sorted(products, key=lambda product: product[1])
print("\nПродукты, отсортированные по цене:")
for product in sorted_products:
    print(product)



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
# users = {"Alice", "Bob", "Charlie"}

users = {"Alice", "Bob", "Charlie"}

for user in users:
    print(user)

users.add("David")

users.remove("Bob")

if "Alice" in users:
    print("\nПользователь 'Alice' есть в множестве.")

print(f"\nКоличество пользователей: {len(users)}")



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
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Множество 1:", set1)
print("Множество 2:", set2)

union = set1.union(set2)
print("\nОбъединение множеств:", union)

intersection = set1.intersection(set2)
print("Пересечение множеств:", intersection)

difference = set1.difference(set2)
print("Разность множеств (set1 - set2):", difference)

is_subset = set2.issubset(set1)
print(f"\nЯвляется ли set2 подмножеством set1: {is_subset}")


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

nventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

while True:
    print('-------')
    print('\nМеню:')
    print('1. Показать список товаров.')
    print('2. Добавить товар.')
    print('3. Удалить товар.')
    print('4. Обновить название товара, стоимость или количество.')
    print('5. Найти товар по названию.')
    print('6. Вывести список товаров меньше определённой стоимости.')
    print('7. Вывести список товаров меньше определенного количества.')

    choice = input('Выберите действие: ')

    if choice == '1':
        print('-------')
        print('Список товаров')
        for item in inventory:
            print(f'Название: {item["product"]}, Цена: {item["price"]}, Количество: {item["count"]}')
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':
        print('Выход из программы')
        break
    else:
        print('Неверный выбор. Пожалуйста, выберите снова.')