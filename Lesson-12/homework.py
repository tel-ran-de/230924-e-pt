# Тема: словари
from idlelib.editor import keynames

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

# employees = {
#     "Alice": {"age": 30, "department": "HR", "salary": 5000},
#     "Bob": {"age": 25, "department": "IT", "salary": 6000},
#     "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
# }
#
# for i in employees:
#     print(i)


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

