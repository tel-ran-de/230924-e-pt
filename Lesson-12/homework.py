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
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}}

for name in employees.keys():
    print(name)
print('\n')
total_salary = sum(employee["salary"] for employee in employees.values())
print(f"Общая сумма зарплат всех сотрудников: {total_salary}")
print('\n')
employees["David"] = {"age": 28, "department": "IT", "salary": 6500}

employees["Alice"]["salary"] = 5500

del employees["Charlie"]

for name, details in employees.items():
    print(f"Имя: {name}, Возраст: {details['age']}, Отдел: {details['department']}, Зарплата: {details['salary']}")
print('=================================================')

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

for product in inventory.keys():
    print(product)

inventory["Apples"]["quantity"] += 10

inventory["Bananas"]["price"] = 1.5

del inventory["Cherries"]

inventory["Dates"] = {"quantity": 15, "price": 4}

total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"Общая стоимость всех товаров: {total_value}")

print('=================================================')
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

print(f'Все координаты: {coordinates}')

sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print(f"Сумма координат по оси x: {sum_x}")
print(f"Сумма координат по оси y: {sum_y}")

coordinates.append((70, 80))

coordinates[0] = (15, 25)

print(f'Новые координаты: {coordinates}')
print('=================================================')


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
print(f'Все продукты: {products}')
print()
sum_products = sum(i for j, i in products)
print(f'Cуммарная стоимость всех продуктов: {sum_products}')
print()
products.append(('Date', 4))
print(f'Новый список продуктов: {products}')
print()
products[0] = ("Apple", 2.5)
print('Заменена цена "Apple" на 2.5')
print("\nПродукты, отсортированные по цене:")
for product in sorted(products, key=lambda i: i[1]):
    print(product)
print('=================================================')
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
for user in users:
    print(user)
print()
users.add('David')
print(users)
print()
users.remove('Bob')
print(users)
print()
print(f'Пользователь "Alice" в множестве: {'Alice' in users}')
print(f'Количество пользователей: {len(users)}')
print('=================================================')
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
all_set = set1.union(set2)
print(all_set)



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
print('=================================================')
inventory = [
     {'product': "Laptop", 'price': 10, 'count': 13},
     {'product': "Mouse", 'price': 50, 'count': 1},
     {'product': "Keyboard", 'price': 30, 'count': 33},
     {'product': "Monitor", 'price': 20, 'count': 10}
 ]
def show_inventory():
    print('\nСписок товаров:')
    for item in inventory:
        print(f'Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}')

def add_item():
    product_name = input('Введите название товара: ')
    price_item = input('Введите цену: ')
    count_item = input('введите количество:')
    inventory.append({'product': product_name, 'price': price_item, 'count': count_item})
    print(f'product: {product_name}, price: {price_item}, count: {count_item} добавлен в список товаров.')

def delete_items():
    delete_item = input('Какой товар вы хотите удалить: ')
    for item in inventory:
        if item['product'] == delete_item:
            inventory.remove(item)
            print(f'product: {delete_item} удален!')
            return
    print('Продукт не найден.')

def update_item():
    name_item = input('Введите название товара для обновления: ')
    for item in inventory:
        if item['product'] == name_item:
            items = input("Что вы хотите обновить: product, price, count ")
            if items == 'product':
                item['product'] = input('Введите новое название товара; ')
            elif items == 'price':
                item['price'] = float(input('Введите новую цену товара: '))
            elif items == 'count':
                item['count'] = int(input('Введите новое количество товара: '))
                break
            else:
                 print('Продукт не найден.')

def find_item():
    name_item = input('Введите название товара для поиска: ')
    for item in inventory:
        if item['product'] == name_item:
            print(f'Название продукта: {item['product']}, Цена: {item['price']}, Количество товаров: {item['count']}')
            break
    else:
        print('Продукт не найден.')

def below_price():
    below_item_price = float(input('Введите определенную стоимость: '))
    print(f'\nТовары меньше {below_item_price} стоимости:')
    for item in inventory:
        if item['price'] < below_item_price:
            print(f'Товар: {item['product']}')

def below_count():
    below_item_count = int(input('Введите определенное количество: '))
    print(f'\nТовары меньше количества {below_item_count}')
    for item in inventory:
        if item['count'] < below_item_count:
            print(f'Товар: {item['product']}')


while True:
    print('\nМеню:')
    print('1. Показать список товаров.')
    print('2. Добавить товар.')
    print('3. Удалить товар.')
    print('4. Обновить название товара, стоимость или количество.')
    print('5. Найти товар по названию.')
    print('6. Вывести список товаров меньше определнной стоимости.')
    print('7. Вывести список товаров меньше определенного количества.')
    print('8. Выйти.')

    choice = input('Выберите действие: ')
    if choice == '1':
        show_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        delete_items()
    elif choice == '4':
        update_item()
    elif choice == '5':
        find_item()
    elif choice == '6':
        below_price()
    elif choice == '7':
        below_count()
    elif choice == '8':
        print('Программа завершена')
        break
    else:
        print('Неверный набор.')

