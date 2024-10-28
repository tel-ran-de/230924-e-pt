```python
# Задача 1: Анализ чисел
def analyze_numbers(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    return total_sum, average, even_count

# Пример использования
numbers = [1, 2, 3, 4, 5, 6]
print(analyze_numbers(numbers))  # Вывод: (21, 3.5, 3)

# Задача 2: Работа со строками
def analyze_strings(strings):
    longest_string = max(strings, key=len)
    shortest_string = min(strings, key=len)
    count_a = sum(1 for string in strings if 'a' in string)
    return longest_string, shortest_string, count_a

# Пример использования
strings = ["apple", "banana", "cherry", "date"]
print(analyze_strings(strings))  # Вывод: ('banana', 'date', 3)

# Задача 3: Обработка словаря сотрудников
def analyze_salaries(employees):
    average_salary = sum(employees.values()) / len(employees)
    max_salary = max(employees.values())
    max_salary_employee = max(employees, key=employees.get)
    return average_salary, max_salary, max_salary_employee

# Пример использования
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
print(analyze_salaries(employees))  # Вывод: (6000.0, 7000, 'Bob')

# Задача 4: Фильтрация списка
def filter_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

# Пример использования
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_numbers(numbers))  # Вывод: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

# Задача 5: Генерация словаря
def create_dict(keys, values):
    return dict(zip(keys, values))

# Пример использования
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(keys, values))  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Задача 6: Подсчет символов в строке
def count_characters(string):
    return {char: string.count(char) for char in string}

# Пример использования
string = "hello world"
print(count_characters(string))  # Вывод: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Задача 7: Обработка произвольного числа аргументов
def sum_positive_negative(*args):
    positive_sum = sum(num for num in args if num > 0)
    negative_sum = sum(num for num in args if num < 0)
    return positive_sum, negative_sum

# Пример использования
print(sum_positive_negative(1, -2, 3, -4, 5))  # Вывод: (9, -6)

# Задача 8: Генерация строки из именованных аргументов
def generate_string(**kwargs):
    return ', '.join(f"{key}={value}" for key, value in kwargs.items())

# Пример использования
print(generate_string(name="Alice", age=30, city="New York"))  # Вывод: name=Alice, age=30, city=New York

# Проект: Управление инвентарем в интернет-магазине
def show_inventory(inventory):
    for item in inventory:
        print(item)

def add_item(inventory, product, price, count):
    inventory.append({'product': product, 'price': price, 'count': count})

def remove_item(inventory, product):
    inventory[:] = [item for item in inventory if item['product'] != product]

def update_item(inventory, product, price=None, count=None):
    for item in inventory:
        if item['product'] == product:
            if price is not None:
                item['price'] = price
            if count is not None:
                item['count'] = count

def find_item(inventory, product):
    return [item for item in inventory if item['product'] == product]

def filter_by_price(inventory, max_price):
    return [item for item in inventory if item['price'] < max_price]

def filter_by_count(inventory, max_count):
    return [item for item in inventory if item['count'] < max_count]

# Пример использования
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

# Меню
while True:
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить название товара, стоимость или количество.")
    print("5. Найти товар по названию.")
    print("6. Вывести список товаров меньше определнной стоимости.")
    print("7. Вывести список товаров меньше определенного количества.")
    print("8. Выйти.")

    choice = input("Выберите опцию: ")

    if choice == '1':
        show_inventory(inventory)
    elif choice == '2':
        product = input("Введите название товара: ")
        price = float(input("Введите стоимость товара: "))
        count = int(input("Введите количество товара: "))
        add_item(inventory, product, price, count)
    elif choice == '3':
        product = input("Введите название товара для удаления: ")
        remove_item(inventory, product)
    elif choice == '4':
        product = input("Введите название товара для обновления: ")
        price = input("Введите новую стоимость (или нажмите Enter для пропуска): ")
        count = input("Введите новое количество (или нажмите Enter для пропуска): ")
        update_item(inventory, product, float(price) if price else None, int(count) if count else None)
    elif choice == '5':
        product = input("Введите название товара для поиска: ")
        found_items = find_item(inventory, product)
        if found_items:
            for item in found_items:
                print(item)
        else:
            print("Товар не найден.")
    elif choice == '6':
        max_price = float(input("Введите максимальную стоимость: "))
        filtered_items = filter_by_price(inventory, max_price)
        for item in filtered_items:
            print(item)
    elif choice == '7':
        max_count = int(input("Введите максимальное количество: "))
        filtered_items = filter_by_count(inventory, max_count)
        for item in filtered_items:
            print(item)
    elif choice == '8':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
```