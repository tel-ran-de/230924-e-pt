# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)
def analyze_numbers(numbers):
    total_summ = sum(numbers)
    average = total_summ / len(numbers)
    even_count = sum(1 for number in numbers if number % 2 == 0)

    return (total_summ, average, even_count)

numbers = [1, 2, 3, 4, 5, 6]
result = analyze_numbers(numbers)
print(result)

# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)
def analyze_strings(strings):
    longest_string = max(strings, key=len)
    shortest_string = min(strings, key=len)
    count_with_a = sum(1 for s in strings if 'a' in s)

    return (longest_string, shortest_string, count_with_a)

strings = ["apple", "banana", "cherry", "date"]
result = analyze_strings(strings)
print(result)

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')
def analyze_salaries(employees):
    total_salary = sum(employees.values())
    average_salary = total_salary / len(employees)
    max_salary_employee = max(employees, key=employees.get)
    max_salary = employees[max_salary_employee]

    return (average_salary, max_salary, max_salary_employee)

employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
result = analyze_salaries(employees)
print(result)


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
def filter_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    return (even_numbers, odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_numbers(numbers)
print(result)


# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}
def create_dict(keys, values):

    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
result = create_dict(keys, values)
print(result)

# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

string = "hello world"
result = count_characters(string)
print(result)

# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)
def sum_positive_negative(*args):
    positive_sum = sum(num for num in args if num > 0)
    negative_sum = sum(num for num in args if num < 0)

    return (positive_sum, negative_sum)

result = sum_positive_negative(1, -2, 3, -4, 5)
print(result)


# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York
def generate_string(**kwargs):
    return ', '.join(f"{key}={value}" for key, value in kwargs.items())

result = generate_string(name="Alice", age=30, city="New York")
print(result)

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

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

def show_products():
    print("Список товаров:")
    for item in inventory:
        print(f"Наименование: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def add_product():
    product_name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': product_name, 'price': price, 'count': count})
    print(f"Товар '{product_name}' добавлен.")

def remove_product():
    product_name = input("Введите название товара для удаления: ")
    global inventory
    inventory = [item for item in inventory if item['product'] != product_name]
    print(f"Товар '{product_name}' удален.")

def update_product():
    product_name = input("Введите название товара, который нужно обновить: ")
    for item in inventory:
        if item['product'] == product_name:
            new_name = input("Введите новое название товара (оставьте пустым для пропуска): ")
            new_price = input("Введите новую цену товара (оставьте пустым для пропуска): ")
            new_count = input("Введите новое количество товара (оставьте пустым для пропуска): ")

            if new_name:
                item['product'] = new_name
            if new_price:
                item['price'] = float(new_price)
            if new_count:
                item['count'] = int(new_count)

            print(f"Товар '{product_name}' обновлен.")
            return
    print(f"Товар '{product_name}' не найден.")

def find_product():
    product_name = input("Введите название товара для поиска: ")
    for item in inventory:
        if item['product'] == product_name:
            print(f"Найден товар: Наименование: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
            return
    print(f"Товар '{product_name}' не найден.")

def products_below_price():
    price_limit = float(input("Введите лимит цены: "))
    print(f"Товары с ценой ниже {price_limit}:")
    for item in inventory:
        if item['price'] < price_limit:
            print(f"Наименование: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def products_below_quantity():
    quantity_limit = int(input("Введите лимит количества: "))
    print(f"Товары с количеством ниже {quantity_limit}:")
    for item in inventory:
        if item['count'] < quantity_limit:
            print(f"Наименование: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def main():
    while True:
        print("\\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров меньше определнной стоимости.")
        print("7. Вывести список товаров меньше определенного количества.")
        print("8. Выход.")

        choice = input("Выберите действие: ")

        if choice == '1':
            show_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            remove_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            find_product()
        elif choice == '6':
            products_below_price()
        elif choice == '7':
            products_below_quantity()
        elif choice == '8':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()

