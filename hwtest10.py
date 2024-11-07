import json


inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
with open("data_shop.json", "w") as file_new:
    json.load(inventory, file_new)

def check_input(product, product_list=inventory):
    product_name_list = [item['product'].lower() for item in product_list]
    if product.lower() not in product_name_list:
        print(f'Продукт: {product} - отсутствует в списке продуктов')
        result = False
    else:
        result = True
    return result


def print_products(product_list = inventory):
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


def add_product(product_list = inventory):
    new_product = input("Введите название товара: ")
    if not check_input(new_product, product_list):
        np_price = int(input("Введите цену товара: "))
        np_count = int(input("Введите количество товара: "))
        product_list.append({'product': new_product,
                             'price': np_price,
                             'count': np_count
                             })
    else:
        print(f'Добавить можно товар, отсутствующий в списке.')
    print_products(product_list)


def delete_product(product_list=inventory):
    product_to_delete = input('Введите название удаляемого товара: ')
    if check_input(product_to_delete, product_list):
        for item in product_list:
            if item['product'] == product_to_delete:
                product_list.remove(item)
        print(f'Продукт: {product_to_delete} - удален из списка продуктов.')
    else:
        print(f'Удалять можно только продукт находящийся в списке.')
    print_products(product_list)


def update_product(product_list = inventory):
    product_to_update = input("Введите название обновляемого товара: ")
    if check_input(product_to_update, product_list):
        article_to_update = input(f'Если хотите обновить название продукта выберите 1\n'
                                  f'Если хотите обновить цену продукта выберите 2\n'
                                  f'Если хотите обновить количество продукта выберите 3: \n')
        if article_to_update == '1':
            new_product = input("Введите новое название товара: ")
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['product'] = new_product.title()
                    print_products([item])
            print(f'Название продукта "{product_to_update}" изменено на "{new_product}" ')
        elif article_to_update == '2':
            new_price = int(input("Введите новую цену товара: "))
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['price'] = new_price
                    print_products([item])
            print(f'Новая цена продукта: {product_to_update} изменена на {new_price} ')
        elif article_to_update == '3':
            new_count = int(input("Введите новое количество товара: "))
            for item in product_list:
                if item['product'].lower() == product_to_update.lower():
                    item['count'] = new_count
                    print_products([item])
            print(f'Новое количество продукта: {product_to_update} изменена на {new_count} ')
        else:
            print("Выбор действия неверен.")
    else:
        print(f'Обновлять можно только продукт из списка товаров.')
    print_products(product_list)


def find_product_name(product_list = inventory):
    product_to_search = input("Введите название искомого товара: ")
    if check_input(product_to_search, product_list):
        print_products([product_to_search])
    else:
        print("Запрашиваемый товар не найден.")


def find_product_price(product_list = inventory):
    max_price = int(input("Введите максимальную цену товара: "))
    search_list = []
    for item in product_list:
        if item['price'] <= max_price:
            search_list.append(item)
    print('-' * 7)
    print(f'Товары с ценой меньшей или равной - {max_price}:')
    print_products(search_list)


def find_product_count(product_list = inventory):
    max_count = int(input("Введите максимальное количество товара: "))
    search_list = []
    for item in product_list:
        if item['count'] <= max_count:
            search_list.append(item)
    print(f'Товары количеством меньшим или равным {max_count}:')
    print_products(search_list)

while True:
    print("     М Е Н Ю:")
    print("---------------------------------------------------------------------------------")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить название товара, стоимость или количество.")
    print("5. Найти товар по названию.")
    print("6. Вывести список товаров меньше определённой стоимости.")
    print("7. Вывести список товаров меньше определенного количества.")
    print("0. Выйти из программы.")
    print("---------------------------------------------------------------------------------")
    choice = input("Выберите действие: ")

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
    elif choice == '0':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
        print("---------------------------------------------------------------------------------")