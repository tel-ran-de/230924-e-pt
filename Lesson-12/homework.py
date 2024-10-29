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
# ОТВЕТ:
employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}
# 1. Выводим имена всех сотрудников
print("Имена сотрудников:")
for name in employees:
    print(name)
#
# 2. Найти и вывести общую сумму зарплат всех сотрудников
total_salary = sum(employee["salary"] for employee in employees.values())
print("\nОбщая сумма зарплат всех сотрудников:", total_salary)
#
# 3. Добавляем нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500
#
employees["David"] = {"age": 28, "department": "IT", "salary": 6500}
print("\nДобавлен сотрудник David:", employees["David"])
#
# 4. Обновляем зарплату "Alice" до 5500

employees["Alice"]["salary"] = 5500
print("\nОбновленная зарплата Alice:", employees["Alice"]["salary"])
#
# 5. Удалить сотрудника "Charlie"
#
employees.pop("Charlie", None)
print("\nСотрудник Charlie удален.")
#
# 6. Выводим данные о каждом сотруднике в указанном формате
#
print("\nДанные о сотрудниках:")
for name, info in employees.items():
    print(f"Имя: {name}, Возраст: {info['age']}, Отдел: {info['department']}, Зарплата: {info['salary']}")
#
#
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
# ОТВЕТ:

inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}
# Выводим названия всех товаров
#
print('Товары в магазине')
for item in inventory.keys():
    print(item)
# Увеличиваем количество "Apples" на 10.
#
inventory['Apples']['quantity'] += 10
#
# 3. Изменяем цену "Bananas" на 1.5
#
inventory["Bananas"]["price"] = 1.5
#
# 4. Удаляем товар "Cherries"
#
del inventory["Cherries"]

# 5. Добавляем новый товар "Dates" с количеством 15 и ценой 4
inventory["Dates"] = {"quantity": 15, "price": 4}
#
# 6. Выводим общую стоимость всех товаров
#
total_cost = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"Общая стоимость всех товаров: {total_cost}")
#
#
# Тема: кортежи и множества.
#
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
#
# ОТВЕТ:
# Исходный список координат
coordinates = [(10, 20), (30, 40), (50, 60)]
#
# # 1. Выводим все координаты
#
print("Координаты:")
for coord in coordinates:
    print(coord)
#
# 2. Находим сумму всех координат по оси x и по оси y
sum_x = sum(coord[0] for coord in coordinates)
sum_y = sum(coord[1] for coord in coordinates)
print(f"Сумма по оси x: {sum_x}, Сумма по оси y: {sum_y}")
#
# 3. Добавляем новую координату (70, 80)
coordinates.append((70, 80))
#
# 4. Заменяем первую координату на (15, 25)
coordinates[0] = (15, 25)
#
# 5. Выводим все координаты, отсортированные по оси x
#
sorted_coordinates = sorted(coordinates, key=lambda coord: coord[0])
print("Координаты, отсортированные по оси x:")
for coord in sorted_coordinates:
    print(coord)
#
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
#
# ОТВЕТ:
#
# Исходный список продуктов
products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
#
# 1. Выводим список всех продуктов
#
print("Продукты:")
for product in products:
    print(product)
#
# 2. Находим суммарную стоимость всех продуктов
#
total_cost_products = sum(price for _, price in products)
print(f"Суммарная стоимость всех продуктов: {total_cost_products}")
#
# 3. Добавляем новый продукт "Date" с ценой 4
#
products.append(("Date", 4))
#
# 4. Заменяем цену "Apple" на 2.5
#
products = [(name, 2.5) if name == "Apple" else (name, price) for name, price in products]
#
# 5. Выводим все продукты, отсортированные по цене
#
sorted_products = sorted(products, key=lambda product: product[1])
print("Продукты, отсортированные по цене:")
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
#
# ОТВЕТ:
#
users = {"Alice", "Bob", "Charlie"}
#
# 1. Выводим список всех пльзователей

print("Пользователи")
for user in users:
    print(user)
#
# 2. Добавляем нового пользователя "David"
users.add("David")
print("\nПользователь 'David' добавлен.")
#
# 3. Удаляем пользователя "Bob"
#
users.discard("Bob")  # Используем discard, чтобы избежать ошибки, если пользователя нет
print("\nПользователь 'Bob' удален.")
#
# 4. Проверяем, есть ли пользователь "Alice" в множестве
#
if "Alice" in users:
    print("\nПользователь 'Alice' присутствует в множестве.")
else:
    print("\nПользователь 'Alice' отсутствует в множестве.")
#
# 5. Выводим количество пользователей
print(f"\nКоличество пользователей: {len(users)}")
#
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
#
# ОТВЕТ:
#
# Исходные множества
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
#
# 1. Выводим элементы обоих множеств
print("Элементы множества set1:", set1)
print("Элементы множества set2:", set2)
#
# 2. Находим объединение двух множеств
union_set = set1 | set2  # или альтернативный способ set1.union(set2)
print("\nОбъединение двух множеств:", union_set)
#
## 3. Находим пересечение двух множеств
#
intersection_set = set1 & set2  # или как вариант set1.intersection(set2)
print("Пересечение двух множеств:", intersection_set)
#
# 4. Находим разность множеств set1 и set2
#
differ_set = set1 - set2  # или set1.difference(set2)
print("Разность множеств set1 и set2:", differ_set)
#
# 5. Проверяем, является ли set2 подмножеством set1
is_subset = set2.issubset(set1)
print("Является ли set2 подмножеством set1:", is_subset)
#
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
#
# ОТВЕТ:
#
# Исходный инвентарь
inventory = [
    {'product': "Laptop", 'price': 1000, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 200, 'count': 10}
]


# 1. Показываем список товаров.
def show_inventory():
    print("\nСписок товаров:")
    for item in inventory:
        print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    #


# 2. Добавляем товар.
def add_product():
    product_name = input("Введите название товара: ")
    price = float(input("Введите стоимость товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': product_name, 'price': price, 'count': count})
    print(f"Товар '{product_name}' добавлен в инвентарь.")


# 3. Удаляем товар
def delete_product():
    product_name = input("Введите название товара для удаления: ")
    global inventory
    inventory = [item for item in inventory if item['product'] != product_name]
    print(f"Товар '{product_name}' удален из инвентаря.")


# 4. Обновляем товар
def update_product():
    product_name = input("Введите название товара для обновления: ")
    for item in inventory:
        if item['product'] == product_name:
            item['price'] = float(input("Введите новую стоимость товара: "))
            item['count'] = int(input("Введите новое количество товара: "))
            print(f"Товар '{product_name}' обновлен.")
            return
    print(f"Товар '{product_name}' не найден.")


#
#  5. Найти товар по названию.
#
def find_product():
    product_name = input("Введите название товара для поиска: ")
    for item in inventory:
        if item['product'] == product_name:
            print(f"Найден товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            return
    print(f"Товар '{product_name}' не найден.")


#
# 6. Выводим список товаров ниже определенной стоимости
#
def list_products_below_price():
    price_limit = float(input("Введите предел стоимости: "))
    print(f"\nТовары с ценой ниже {price_limit}:")
    for item in inventory:
        if item['price'] < price_limit:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")


#
#  7. Выводим список товаров ниже определенного количества
#
def list_products_below_count():
    count_limit = int(input("Введите предел количества: "))
    print(f"\nТовары с количеством ниже {count_limit}:")
    for item in inventory:
        if item['count'] < count_limit:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")


#
# 8. Главное меню
#
def main():
    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров меньше определенной стоимости.")
        print("7. Вывести список товаров меньше определенного количества.")
        print("8. Выход.")

        choice = input("Выберите действие (1-8): ")

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
            list_products_below_price()
        elif choice == '7':
            list_products_below_count()
        elif choice == '8':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 8.")


#
# 9. Запуск программы
#
main()
#
