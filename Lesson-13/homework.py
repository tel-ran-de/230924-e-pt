# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.

def analyze_numbers(numbers):
    total = sum(numbers)
    average = sum(numbers) / len(numbers)
    chot = sum(1 for i in numbers if i % 2 == 0)
    return total, average, chot

numbers = [1, 2, 3, 4, 5, 6]
print(analyze_numbers(numbers))
print("---------")
# Вывод функции: (21, 3.5, 3)


# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
def analyze_strings(strings):
    longest = max(strings, key=len)
    shorter = min(strings, key=len)
    count_a = sum([1 for i in strings if "a" in i])
    return longest, shorter, count_a

strings = ["apple", "banana", "cherry", "date"]
print(analyze_strings(strings))
# Вывод функции: ('banana', 'date', 3)
print("----------")

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
def analyze_salaries(employees):
    total_solary = sum(employees.values()) / len(employees)
    max_salary = max(employees.values())
    name_max_salary = max(employees, key=employees.get)
    return total_solary, max_salary, name_max_salary

employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
print(analyze_salaries(employees))
# Вывод функции: (6000.0, 7000, 'Bob')
print("---------")

# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
def filter_numbers(numbers):
    chot = [i for i in numbers if i % 2 == 0]
    nechot = [i for i in numbers if i % 2 != 0]
    return chot, nechot

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_numbers(numbers))
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
print("-------")

# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
def create_dict(keys, values):
    dict_list = {keys[i]: values[i] for i in range(len(keys))}
    return dict_list
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(keys, values))
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("------")

# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char]=1
    return char_count

string = "hello world"
print(count_characters(string))
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print("--------")

# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
def sum_positive_negative(*args):
    sum_plus = sum([i for i in args if i > 0])
    sum_min = sum([i for i in args if i < 0])
    return sum_plus, sum_min

sum_positive_negative(1, -2, 3, -4, 5)
print(sum_positive_negative(1, -2, 3, -4, 5))
# Вывод функции: (9, -6)
print("----------")

# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
def generate_string(**kwargs):
    result = [f"{key}={value}" for key, value in kwargs.items()]
    return result

generate_string(name="Alice", age=30, city="New York")
print(*generate_string(name="Alice", age=30, city="New York"))
# Вывод функции: name=Alice, age=30, city=New York
print("-------")

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

def show_inventory():
    for item in inventory:
        print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")

def add_product():
    product = input("Введите имя продукта: ")
    price = float(input("Введите названия продукта: "))
    count = int(input("Введите количество продукта: "))
    inventory.append({'product': product, 'price': price, 'count': count})


def delete_product():
    product = input("Введите название продукта который хотите удалить: ")
    for item in inventory:
        if item['product'] == product:
            inventory.remove(item)
            break
    else:
        print("Продукт не наиден.")



def update_product():
    product = input("Введите название продукта чтоб обнавить: ")
    for item in inventory:
        if item['product'] == product:
            item['price'] = float(input("Введите новую цену: "))
            item['count'] = int(input("Введите новое количество: "))
            break
    else:
        print("Продукт не найден.")



def find_product():
    product = input("Введите название продукта которую ищите: ")
    for item in inventory:
        if item['product'] == product:
            print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
            break
    else:
        print("Продукт не найден.")


def products_below_price():
    price = float(input("Введите цену для пойска товара: "))
    for item in inventory:
        if item['price'] < price:
            print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")


def products_below_count():
    count = int(input("Введите количество что вас интересует: "))
    for item in inventory:
        if item['count'] < count:
            print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")


def main():
    while True:
        print("\nMenu:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить название товара, стоимость или количество.")
        print("5. Найти товар по названию.")
        print("6. Вывести список товаров меньше определенной стоимости.")
        print("7. Вывести список товаров меньше определенного количества.")
        print("8. Выйти.")

        choice = input("Выберите опцию: ")

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
            products_below_price()
        elif choice == '7':
            products_below_count()
        elif choice == '8':
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__": main()

