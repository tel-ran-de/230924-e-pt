import json
# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
file = open('text_files/data.txt', 'r')
# 2. Прочитайте весь контент файла и выведите его на экран.
text = file.read()
print(text)
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
file.seek(0)
text_10 = file.read(10)
print(text_10)
# 4. Прочитайте одну строку из файла и выведите ее на экран.
file.seek(0)
text_line = file.readline()
print(text_line)
# 5. Прочитайте все строки файла и выведите их на экран.
file.seek(0)
lines = file.readlines()
print(lines)
file.close()

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
file = open('text_files/output.txt', 'w')
# 2. Запишите в файл строку "Hello, World!".
text = "Hello, World! \n"
file.write(text)
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
lines = ["This is line 1\n", "This is line 2\n"]
file.writelines(lines)
# 4. Закройте файл.
file.close()
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
file = open('text_files/output.txt', 'r')
text = file.read()
print(text)
file.close()

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
file = open('text_files/log.txt', 'a')
# 2.Добавьте строку "New log entry\n" в конец файла.
text = "New log entry\n"
file.write(text)
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
lines = ["Log entry 1\n", "Log entry 2\n"]
file.writelines(lines)
# 4. Закройте файл.
file.close()
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
file = open('text_files/log.txt', 'r')
print(file.read())
file.close()

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
file = open('text_files/pointer_example.txt', 'w+')
# 2. Запишите в файл строку "Python File Handling\n".
file.write("Python File Handling\n")
# 3. Переместите указатель в начало файла и прочитайте первую строку.
file.seek(0)
print('прочитайте первую строку.', file.readline())
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
file.seek(7)
print('следующие 5 символов.', file.read(5))
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
file.seek(0, 2)
file.write("End of file\n")
# 6. Переместите указатель в начало файла и прочитайте весь файл.
file.seek(0, 0)
print(file.read())
file.close()


# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
user_dict =  {'name': 'Alice', 'age': 33, 'city': 'Bad Berleburg'}
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
with open('text_files/user.json', 'w') as file:
    json.dump(user_dict, file)
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.
with open('text_files/user.json', 'r') as file:
    result = json.load(file)
    print(result)

# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
with open('text_files/user.json', 'r') as file:
    result = json.load(file)
# 2. Обновите возраст пользователя на 29 лет.
    result['age'] = 29
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.
with open('text_files/user.json', 'w') as file:
    json.dump(result, file)

# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
with open('text_files/user.json', 'r') as file:
    old_user = json.load(file)
# 2. Добавьте нового пользователя в массив.
    new_user = {'name': 'Bruce', 'age': 23, 'city': 'Berlin'}
    users = [old_user, new_user]
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open('text_files/user.json', 'w') as file:
    json.dump(users, file)

# Задача 4: Удаление пользователя из массива JSON

# 1. Прочитайте массив объектов из файла `users.json`.
with open('text_files/user.json', 'r') as file:
    users = json.load(file)
# 2. Удалите одного из пользователей.
    users.pop()
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open('text_files/user.json', 'w') as file:
    json.dump(users, file)

# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле (через JSON).
# Используйте файл как базу данных проекта.
#
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
# 6. Вывести список товаров меньше определённой стоимости.
# 7. Вывести список товаров меньше определенного количества.

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
with open('text_files/inventory.json', 'w') as database:
    json.dump(inventory, database)

def inventory_read(file_name = 'text_files/inventory.json'):
    with open(file_name, 'r') as inventory_file:
        inventory_database = json.load(inventory_file)
        return inventory_database

def inventory_write(file_name = 'text_files/inventory.json', product_list=inventory):
    with open(file_name, 'w') as inventory_file:
        json.dump(product_list, inventory_file)
        print(f'обновленный список продуктов сохранен в файл {file_name}!' )


def check_input(product, product_list=inventory):
    '''функция проверяет есть ли введенный товар в списке товара'''
    product_list = inventory_read()
    product_name_list = [item['product'].lower() for item in product_list]
    if product.lower() not in product_name_list:
        print(f'Продукт {product} отсутствует в списке продуктов')
        res = False
    else:
        res = True
    return res


def print_products(product_list=inventory):
    product_list = inventory_read()
    print('-' * 27)
    columns = list(product_list[0].keys())
    print('|', end='')
    for item in columns:
        print(f' {item} ', end='|')
    print()
    print('-' * 27)
    for product in product_list:
        vals = list(product.items())
        print('|', end='')
        for val in vals:
            print(f' {val[1]:{len(val[0]) + 1}}', end='|')
        print()
        print('-' * 27)


def add_product(product_list=inventory):
    product_list = inventory_read()
    new_product = input('Введите название товара: ')
    if not check_input(new_product, product_list):
        np_price = int(input('Введите цену товара: '))
        np_count = int(input('Введите количество товара: '))
        product_list.append({'product': new_product,
                             'price': np_price,
                             'count': np_count
                             })
        inventory_write(product_list=product_list)
    else:
        print(f'Добавить можно только отсутствующий в списке продукт!')
    print_products(product_list)


def delete_product(product_list=inventory):
    product_list = inventory_read()
    product_to_delete = input('Введите название удаляемого товара: ')
    if check_input(product_to_delete, product_list):
        for item in product_list:
            if item['product'] == product_to_delete:
                product_list.remove(item)
        print(f'продукт {product_to_delete} удален из списка продуктов!')
        inventory_write(product_list=product_list)
    else:
        print(f'Удалять можно только продукт находящийся в списке товара!')
    print_products(product_list)


def update_product(product_list=inventory):
    product_list = inventory_read()
    product_to_update = input('Введите название обновляемого товара: ')
    if check_input(product_to_update, product_list):
        article_to_update = input(f'Если хотите обновить название продукта выберите 1\n'
                                  f'Если хотите обновить цену продукта выберите 2\n'
                                  f'Если хотите обновить количество продукта выберите 3: \n')
        if article_to_update == '1':
            new_product = input('Введите новое название товара: ')
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['product'] = new_product.title()
                    print_products([item])
            print(f'Название продукта {product_to_update} изменено на {new_product} ')
        elif article_to_update == '2':
            new_price = int(input('Введите новую цену товара: '))
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['price'] = new_price
                    print_products([item])
            print(f'Новая цена продукта {product_to_update} изменена на {new_price} ')
        elif article_to_update == '3':
            new_count = int(input('Введите новое количество товара: '))
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['count'] = new_count
                    print_products([item])
            print(f'Новое количество продукта {product_to_update} изменена на {new_count} ')
        else:
            print('Выбор действия неверен!')
    else:
        print(f'Обновлять можно только продукт находящийся в списке товара!')
    inventory_write(product_list=product_list)
    product_list = inventory_read()
    print_products(product_list)


def find_product_name(product_list=inventory):
    product_list = inventory_read()
    product_to_search = input('Введите название искомого товара: ')
    if check_input(product_to_search, product_list):
        print_products([product_to_search])
    else:
        print("Запрашиваемый товар не найден!")


def find_product_price(product_list=inventory):
    product_list = inventory_read()
    max_price = int(input('Введите максимальную цену товара: '))
    search_list = []
    for item in product_list:
        if item['price'] <= max_price:
            search_list.append(item)
    print('-' * 7)
    print(f'Товары с ценой меньшей или равной {max_price}:')
    print_products(search_list)


def find_product_count(product_list=inventory):
    product_list = inventory_read()
    max_count = int(input('Введите максимальное количество товара: '))
    search_list = []
    for item in product_list:
        if item['count'] <= max_count:
            search_list.append(item)
    print(f'Товары количеством меньшим или равным {max_count}:')
    print_products(search_list)


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
    print('8. Выйти из программы.')

    choice = input('Выберите действие: ')

    if choice == '1':
        print_products()
    elif choice == '2':
        add_product()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        find_product_name()
    elif choice == '6':
        find_product_price()
    elif choice == '7':
        find_product_count()
    elif choice == '8':
        print('Выход из программы')
        break
    else:
        print('Неверный выбор. Пожалуйста, выберите снова.')

