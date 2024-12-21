# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
def analyze_numbers(numbers_list):
    numbers_sum = sum(numbers_list)
    average = numbers_sum/len(numbers_list)
    evens = sum(1 for i in numbers if i % 2 == 0)
    return numbers_sum, average, evens

numbers = [1, 2, 3, 4, 5, 6]
print(analyze_numbers(numbers))

# Вывод функции: (21, 3.5, 3)


# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
def analyze_strings(string):
    min_str = min(string, key=len)
    max_str = max(string, key=len)
    a_total = sum(1 for word in string if 'a' in word)
    print((min_str, max_str, a_total))
    return min_str, max_str, a_total

strings = ["apple", "banana", "cherry", "date"]
analyze_strings(strings)
# Вывод функции: ('banana', 'date', 3)


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
def analyze_salaries(employees):
    salary_list = [val for val in employees.values()]
    average = sum(salary_list)/len(employees)
    max_salary = max(salary_list)
    name =[item[0] for item in list(employees.items()) if item[1] == max_salary]
    print(average, max_salary, *name)
    return average, max_salary, *name
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
print(analyze_salaries(employees))

# Вывод функции: (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
def filter_numbers(numbers_list):
    even= [x for x in numbers_list if x % 2 == 0]
    odd = [x for x in numbers_list if x % 2 != 0]
    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_numbers(numbers))

# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(keys, values))
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.


def count_characters(string):
    result_dict = {}
    for char in string:
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    return result_dict

string = "hello world"
print(count_characters(string))
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#


def sum_positive_negative(*args):
    positiv_sum = sum(x for x in args if x > 0)
    negativ_sum = sum(x for x in args if x < 0)
    print(positiv_sum, negativ_sum)
    return positiv_sum, negativ_sum


sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)


# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
def generate_string(**kwargs):
    res_list = [f'{item[0]} = {item[1]},' for item in list(kwargs.items())]
    print(*res_list)


generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York


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
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.


inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

def check_input(product, product_list = inventory):
    '''функция проверяет есть ли введенный товар в списке товара'''
    product_name_list = [item['product'].lower() for item in product_list]
    if product.lower() not in product_name_list:
        print(f'Продукт {product} отсутствует в списке продуктов')
        result = False
    else:
        result = True
    return result


def print_products(product_list = inventory):
    print('-'*27)
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
            print(f' {val[1]:{len(val[0])+1}}', end='|')
        print()
        print('-' * 27)

def add_product(product_list = inventory):
    new_product = input('Введите название товара: ')
    if not check_input(new_product, product_list):
        np_price = int(input('Введите цену товара: '))
        np_count = int(input('Введите количество товара: '))
        product_list.append({'product': new_product,
                          'price': np_price,
                          'count': np_count
                          })
    else:
        print(f'Добавить можно только отсутствующий в списке продукт!')
    print_products(product_list)

def delete_product(product_list = inventory):
    product_to_delete = input('Введите название удаляемого товара: ')
    if check_input(product_to_delete, product_list):
        for item in product_list:
            if item['product'] == product_to_delete:
                product_list.remove(item)
        print(f'продукт {product_to_delete} удален из списка продуктов!')
    else: 
        print(f'Удалять можно только продукт находящийся в списке товара!')
    print_products(product_list)

def update_product(product_list = inventory):
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
    print_products(product_list)
        
        
def find_product_name(product_list = inventory):
    product_to_search = input('Введите название искомого товара: ')
    if check_input(product_to_search, product_list):
        print_products([product_to_search])
    else:
        print("Запрашиваемый товар не найден!")

def find_product_price(product_list = inventory):
    max_price = int(input('Введите максимальную цену товара: '))
    search_list = []
    for item in product_list:
        if item['price'] <= max_price:
            search_list.append(item)
    print('-' * 7)
    print(f'Товары с ценой меньшей или равной {max_price}:')
    print_products(search_list)

def find_product_count(product_list = inventory):
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
