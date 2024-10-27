# tasks_and_solutions.py

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

for name in employees:
    print(name)

total_salary = sum(employee["salary"] for employee in employees.values())
print(f"Общая сумма зарплат: {total_salary}")

employees["David"] = {"age": 28, "department": "IT", "salary": 6500}
employees["Alice"]["salary"] = 5500
del employees["Charlie"]

for name, info in employees.items():
    print(f"Имя: {name}, Возраст: {info['age']}, Отдел: {info['department']}, Зарплата: {info['salary']}")


# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.

inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

for product in inventory:
    print(product)

inventory["Apples"]["quantity"] += 10
inventory["Bananas"]["price"] = 1.5
del inventory["Cherries"]
inventory["Dates"] = {"quantity": 15, "price": 4}

total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"Общая стоимость всех товаров: {total_value}")


# Тема: кортежи и множества

# Задача 1: Обработка данных о координатах
coordinates = [(10, 20), (30, 40), (50, 60)]

for coord in coordinates:
    print(coord)

sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print(f"Сумма координат по оси x: {sum_x}, по оси y: {sum_y}")

coordinates.append((70, 80))
coordinates[0] = (15, 25)
sorted_coords = sorted(coordinates, key=lambda x: x[0])

for coord in sorted_coords:
    print(coord)


# Задача 2: Обработка данных о продуктах
products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]

for product in products:
    print(product)

total_cost = sum(price for name, price in products)
print(f"Суммарная стоимость продуктов: {total_cost}")

products.append(("Date", 4))
products = [(name, 2.5) if name == "Apple" else (name, price) for name, price in products]
sorted_products = sorted(products, key=lambda x: x[1])

for product in sorted_products:
    print(product)


# Задача 3: Управление группами пользователей
users = {"Alice", "Bob", "Charlie"}

for user in users:
    print(user)

users.add("David")
users.discard("Bob")
print(f"Есть ли пользователь 'Alice' в множестве: {'Alice' in users}")
print(f"Количество пользователей: {len(users)}")


# Задача 4: Управление наборами данных
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2

print(f"Объединение: {union_set}")
print(f"Пересечение: {intersection_set}")
print(f"Разность (set1 - set2): {difference_set}")
print(f"Является ли set2 подмножеством set1: {set2.issubset(set1)}")


# Проект: Управление инвентарем в интернет-магазине
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

def show_inventory():
    for item in inventory:
        print(item)

def add_product(product, price, count):
    inventory.append({'product': product, 'price': price, 'count': count})

def remove_product(product_name):
    global inventory
    inventory = [item for item in inventory if item['product'] != product_name]

def update_product(product_name, new_price=None, new_count=None):
    for item in inventory:
        if item['product'] == product_name:
            if new_price is not None:
                item['price'] = new_price
            if new_count is not None:
                item['count'] = new_count

def find_product(product_name):
    for item in inventory:
        if item['product'] == product_name:
            print(item)

def products_below_price(price_limit):
    return [item for item in inventory if item['price'] < price_limit]

def products_below_count(count_limit):
    return [item for item in inventory if item['count'] < count_limit]

# Использование функций:
show_inventory()
add_product("Tablet", 25, 7)
remove_product("Mouse")
update_product("Keyboard", new_price=35)
find_product("Monitor")
cheap_products = products_below_price(30)
low_stock_products = products_below_count(15)

print("Товары с ценой ниже 30:", cheap_products)
print("Товары с количеством меньше 15:", low_stock_products)
