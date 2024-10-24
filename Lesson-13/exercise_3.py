# Проект: Перепишите проект из урока 7 в функциональном стиле.
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


# функция для вывода списка товаров
def show_inventory(product_list):
    print('-------')
    print('Список товаров')
    for item in product_list:
        print(f'Название: {item["product"]}, Цена: {item["price"]}, Количество: {item["count"]}')


# функция для добавления нового товара
def add_product(product_list, product, price, count):
    pass


# функция для удаления товара
def remove_product(product_list, product):
    pass


# функция для обновления товара
def update_product(product_list, product, price, count):
    pass


# функция для поиска товара по названию
def find_product(product_list, product):
    pass


# функция для вывода товаров меньше определённой стоимости
def show_products_below_price(product_list, price):
    pass


# функция для вывода товаров меньше определённого количества
def show_products_below_count(product_list, count):
    pass


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
        show_inventory(product_list=inventory)
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


