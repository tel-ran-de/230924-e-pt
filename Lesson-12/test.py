
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

while True:

    print('\n','Меню:')
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
        print('Список товаров')
        for item in inventory:
            print(f'Название: {item["product"]}, Цена: {item["price"]}, Количество: {item["count"]}')
    if choice == '2':
        new_product = input('Введите название товара: ')
        price = int(input('Введите цену товара: '))
        count = int(input('Введите количество товара: '))
        inventory.append({'product': new_product,
                           'price': price,
                           'count': count
                          })
    if choice == '3':
        del_product = input('Введите название удаляемого товара: ')
        for item in inventory:
            if item['product'] == del_product:
                inventory.remove(item)
    if choice == '4':
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
            print('Выбор некорректен!')
    if choice == '5':
        product_to_search = input('Введите название искомого товара: ')
        for item in inventory:
            if item['product'].lower() == product_to_search.lower():
                print(f'Название: {item["product"]}, Цена: {item["price"]}, Количество: {item["count"]}')
                break
        else:
            print("Товар не найден!")
    if choice == '6':
        max_price = int(input('Введите максимальную цену товара: '))
        products_list = []
        for item in inventory:
            if item['price'] <= max_price:
                products_list.append(item)
        print('-'* 7)
        print(f'Товары с ценой меньшей или равной {max_price}:')
        for article in products_list:
            print(f'Название: {article["product"]}, Цена: {article["price"]}, Количество: {article["count"]}')
    if choice == '7':
        max_count = int(input('Введите максимальное количество товара: '))
        products_list = []
        for item in inventory:
            if item['count'] <= max_count:
                products_list.append(item)
        print('-' * 7)
        print(f'Товары количеством меньшим или равным {max_count}:')
        for article in products_list:
            print(f'Название: {article["product"]}, Цена: {article["price"]}, Количество: {article["count"]}')
    if choice == '8':
        print('Выход из программы')
        break