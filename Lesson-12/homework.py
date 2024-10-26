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
for name in employees.keys():
    print(name)
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
salary = sum([ x['salary'] for x in employees.values()])
print(salary)
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
employees['David'] = {'age':28, 'department': 'IT', 'salary': 6500}
# 4. Обновите зарплату "Alice" до 5500.
employees['Alice']['salary'] = 5500
# 5. Удалите сотрудника "Charlie".
employees.pop("Charlie")
print(employees)
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
for key, value in employees.items():
     print(f"Имя: {key}, Возраст: {value['age']}, Отдел: {value['department']}, "
         f"Зарплата: {value['salary']}")


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
for item in inventory:
    print(item)
# 2. Увеличьте количество "Apples" на 10.
inventory['Apples']['quantity'] += 10
# 3. Измените цену "Bananas" на 1.5.
inventory['Bananas']['price'] = 1.5
# 4. Удалите товар "Cherries".
inventory.pop('Cherries')
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
inventory['Dates'] = {"quantity": 15, "price": 4}
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
total_sum = sum([x["quantity"] * x["price"] for x in inventory.values()])
print(inventory)
print(total_sum)

# Тема: кортежи и множества.

# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.
#
# Задание:

#
coordinates = [(10, 20), (30, 40), (50, 60)]
# 1. Выведите все координаты.
print(*coordinates)
# 2. Найдите сумму всех координат по оси x и по оси y.
x_sum = sum([x[0] for x in coordinates])
y_sum = sum([x[1] for x in coordinates])
print(x_sum, y_sum)
# 3. Добавьте новую координату (70, 80).
coordinates.append((70,80))
# 4. Замените первую координату на (15, 25).
coordinates[0] = (15, 25)
# 5. Выведите все координаты, отсортированные по оси x.
coordinates.sort()
print(coordinates)



# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.
#
# Задание:


#
products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
# 1. Выведите все продукты.
for item in products:
    print(item[0])
# 2. Найдите суммарную стоимость всех продуктов.
products_sum = sum([x[1] for x in products])
print(products_sum)
# 3. Добавьте новый продукт "Date" с ценой 4.
products.append(('Date', 4))
# 4. Замените цену "Apple" на 2.5.
products[0] = ("Apple", 2.5)
print(products)
# 5. Выведите все продукты, отсортированные по цене.
result = sorted(products, key=lambda x : x[1])
print(result)
# Решение без использования lambda
products_sorted = []
check_list =  sorted([x[1] for x in products])
k = 0
while True:
    for product in products:
        if check_list[k] == product[1]:
            products_sorted.append(product)
            k += 1
    if len(products_sorted) == len(products):
        break
print(products_sorted)


# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
#

users = {"Alice", "Bob", "Charlie"}
# 1. Выведите всех пользователей.
for index, user in enumerate(users):
    print(f'{index+1}. {user}')
# 2. Добавьте нового пользователя "David".
users.add("David")
# 3. Удалите пользователя "Bob".
users.remove('Bob')
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
print(f'{"Alice" in users}')
print(users.issuperset({'Alice'}))
# 5. Выведите количество пользователей.
print(len(users))


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
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# 1. Выведите элементы обоих множеств.
print(*set1)
print(*set2)
# 2. Найдите объединение двух множеств.
print(set1.union(set2))
# 3. Найдите пересечение двух множеств.
print(set1.intersection(set2))
# 4. Найдите разность множеств `set1` и `set2`.
print(set1.difference(set2))
# 5. Проверьте, является ли `set2` подмножеством `set1`.
print(set2.issubset(set1))



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
    print('8. Выход из программы.')

    choice = input('Выберите действие: ')

    if choice == '1':
        print('-------')
        print('Список товаров')
        for item in inventory:
            print(f'Название: {item["product"]}, Цена: {item["price"]}, Количество: {item["count"]}')
    elif choice == '2':
        new_product = input('Введите название товара: ')
        np_price = int(input('Введите цену товара: '))
        np_count = int(input('Введите количество товара: '))
        inventory.append({'product': new_product,
                           'price': np_price,
                           'count': np_count
                          })
    elif choice == '3':
        product_to_delete = input('Введите название удаляемого товара: ')
        for item in inventory:
            if item['product'] == product_to_delete:
                inventory.remove(item)
    elif choice == '4':
        product_to_update = input('Введите название обновляемого товара: ')
        item_to_update = input(f'Если хотите обновить название продукта выберите 1\n'
                               f'Если хотите обновить цену продукта выберите 2\n'
                               f'Если хотите обновить количество продукта выберите 3: \n')
        if item_to_update == '1':
            new_product = input('Введите новое название товара: ')
            for item in inventory:
                if item['product'] == product_to_update:
                    item['product'] = new_product
        elif item_to_update == '2':
            new_price = input('Введите новую цену товара: ')
            for item in inventory:
                if item['product'] == product_to_update:
                    item['price'] = new_price
        elif item_to_update == '3':
            new_count = input('Введите новое количество товара: ')
            for item in inventory:
                if item['product'] == product_to_update:
                    item['count'] = new_count
        else:
            print('Выбор действия неверен!')
    elif choice == '5':
        product_to_search = input('Введите название искомого товара: ')
        for item in inventory:
            if item['product'].lower() == product_to_search.lower():
                print(f'Название: {item["product"]}, Цена: {item["price"]}, Количество: {item["count"]}')
                break
        else:
            print("Запрашиваемый товар не найден!")

    elif choice == '6':
        max_price = int(input('Введите максимальную цену товара: '))
        products_list = []
        for item in inventory:
            if item['price'] <= max_price:
                products_list.append(item)
        print('-'* 7)
        print(f'Товары с ценой меньшей или равной {max_price}:')
        for article in products_list:
            print(f'Название: {article["product"]}, Цена: {article["price"]}, Количество: {article["count"]}')
    elif choice == '7':
        max_count = int(input('Введите максимальное количество товара: '))
        products_list = []
        for item in inventory:
            if item['count'] <= max_count:
                products_list.append(item)
        print('-' * 7)
        print(f'Товары количеством меньшим или равным {max_count}:')
        for article in products_list:
            print(f'Название: {article["product"]}, Цена: {article["price"]}, Количество: {article["count"]}')

    elif choice == '8':
        print('Выход из программы')
        break
    else:
        print('Неверный выбор. Пожалуйста, выберите снова.')

