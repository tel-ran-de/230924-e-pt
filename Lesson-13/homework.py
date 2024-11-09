# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)


def analyze_numbers(numbers):
    if not numbers:   # "Проверяем, что список не пустой"
     return (0, 0, 0)

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)

    return (total_sum, average, even_count)

"Функции"

numbers = [1, 2, 3, 4, 5, 6]
result = analyze_numbers(numbers)
print(result)  # (21, 3.5, 3)


# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)







# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)



def analyze_strings(strings):
    if not strings:                                        # "список строк не пустой"
     return (" ", " ",0)

    longest_string = max(strings, key=len)                 # "длинная строка"
    shortest_string = min(strings, key=len)                # "короткая строка"
    count_with_a = sum(1 for s in strings if 'a' in s)     # "Количество строк, содержащих букву" "a"

    return (longest_string, shortest_string, count_with_a)


"функции"

strings = ["apple", "banana", "cherry", "date"]
result = analyze_strings(strings)
print(result)  # ('banana', 'date', 3)






# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')



employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}

for name in employees.keys():
    print(name)

def analyze_salaries(employees):
    if not employees:                                                "словарь не пустой"
    return (0.0, 0, " "),
    salaries = list(employees.values()),                             "список зарплат"
    average_salary = sum(salaries) / len(salaries),                  "средняя зарплата"
    max_salary = max(salaries),                                      "максимальная зарплата"
    max_salary_employee = max(employees, key=employees.get ),        "сотрудник с максимальной зарплатой"

    return (average_salary, max_salary, max_salary_employee)


"функции"

employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
result = analyze_salaries(employees)
print(result) #(6000.0, 7000, 'Bob')






# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])



def filter_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0],  "Четные числа"
    odds = [num for num in numbers if num % 2 != 0],   "Нечетные числа"

    return (evens, odds)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_numbers(numbers)

print(result),    # ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])





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

print(result)  # {'name': 'Alice', 'age': 30, 'city': 'New Yor






# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}



def count_characters(string):
    return{char: string.count(char) for char in string}
string = "hello world"

print(count_characters(string))



def count_characters(string):
    return{char: string.count(char) for char in string}
string = "My name is Max"

print(count_characters(string.lower()))



def count_characters(string):
    return{char: string.count(char) for char in string}
string = "My name is Adler"

print(count_characters(string.lower()))





# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)



def sum_positive_negative(*args):
    positive_sum = sum(num for num in args if num > 0),         "Сумма положительных чисел"
    negative_sum = sum(num for num in args if num < 0),         "Сумма отрицательных чисел"

    return (positive_sum, negative_sum)

result = sum_positive_negative(1, -2, 3, -4, 5)

print(result),   # (9, -6)





# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York



generate_string = {"name":"Alice", "age":30, "city":"New York"}

def generate_string(**kwargs):
    return ', '.join(f"{key}={value}" for key, value in kwargs.items())

result = generate_string(name="Alice", age=30, city="New York")
print(result),   # name=Alice, age=30, city=New York







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
def main():
    inventory = [
        {'product': "Laptop", 'price': 10, 'count': 13},
        {'product': "Mouse", 'price': 50, 'count': 1},
        {'product': "Keyboard", 'price': 30, 'count': 33},
        {'product': "Monitor", 'price': 20, 'count': 10}
    ]

while True:
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить товар.")
    print("5. Найти товар по названию.")
    print("6. Вывести товары меньше определенной стоимости.")
    print("7. Вывести товары меньше определенного количества.")
    print("0. Выход.")

    choice = input("Выберите действие: ")

    if choice == '1':
        print(show_inventory(inventory))

    elif choice == '2':
        product = input("название товара: ")
        price = float(input("цену товара: "))
        count = int(input("количество товара: "))
        inventory = add_product(inventory, product, price, count)
        print(f"Товар '{product}' добавлен.")

    elif choice == '3':
        product = input("название товара для удаления: ")
        inventory = remove_product(inventory, product)
        print(f"Товар '{product}'удален.")

    elif choice == '4':
        product = input("название товара для обновления: ")
        new_name = input("новое название товара (или оставьте пустым для пропуска): ") or None
        new_price = input("новую цену товара (или оставьте пустым для пропуска): ")
        new_price = float(new_price) if new_price else None
        new_count = input("новое количество товара (или оставьте пустым для пропуска): ")
        new_count = int(new_count) if new_count else None
        update_product(inventory, product, new_name, new_price, new_count)

    elif choice == '5':
        product = input("название товара для поиска:" )
        find_product(inventory, product)

    elif choice == '6':
        max_price = float(input("максимальную цену:" ))
        below_price = products_below_price(inventory, max_price)
        show_inventory(below_price)

    elif choice == '7':
        max_count = int(input("максимальное количество:" ))
        below_count = products_below_count(inventory, max_count)
        show_inventory(below_count)
    elif choice == '0':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()


##########################################################################################################
##########################################################################################################
##########################################################################################################



# Начальный инвентарь
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]


"отображения всех товаров"
def show_inventory(inventory):
    return "\n".join([f"{item['product']} - Цена: {item['price']} - Количество: {item['count']}" for item in inventory])


"добавления товара"
def add_product(inventory, product, price, count):
    new_product = {'product': product, 'price': price, 'count': count}
    return inventory + [new_product]

"название товара для удаления"
def remove_product(inventory, product_name):
    return [item for item in inventory if item['product'] != product_name]


"обновления товара"
def update_product(inventory, product_name, new_name=None, new_price=None, new_count=None):
    updated_inventory = []
    for item in inventory:
        if item['product'] == product_name:
            updated_item = item.copy()
            if new_name is not None:
                updated_item['product'] = new_name
            if new_price is not None:
                updated_item['price'] = new_price
            if new_count is not None:
                updated_item['count'] = new_count
            updated_inventory.append(updated_item)
        else:
            updated_inventory.append(item)
    return updated_inventory


"для поиска товара по названию"
def find_product(inventory, product_name):
    return [item for item in inventory if product_name.lower() in item['product'].lower()]


"вывод товаров ниже заданной стоимости"
def filter_by_price(inventory, max_price):
    return [item for item in inventory if item['price'] < max_price]


"вывод товаров с количеством ниже заданного"
def filter_by_count(inventory, max_count):
    return [item for item in inventory if item['count'] < max_count]


"пользовател"

def menu(inventory):
    while True:
        print("\nМеню:")
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
            print(show_inventory(inventory))

        elif choice == '2':
            product = input("название товара: ")
            price = float(input("цену товара: "))
            count = int(input("количество товара: "))
            inventory = add_product(inventory, product, price, count)
            print(f"Товар '{product}' добавлен.")

        elif choice == '3':
            product_name = input("название товара для удаления: ")
            inventory = remove_product(inventory, product_name)
            print(f"Товар '{product_name}' удален.")

        elif choice == '4':
            product_name = input("название товара для обновления: ")
            new_name = input("новое название товара (или нажмите Enter для пропуска): ")
            new_price = input("новую цену товара (или нажмите Enter для пропуска): ")
            new_count = input("новое количество товара (или нажмите Enter для пропуска): ")
            new_price = float(new_price) if new_price else None
            new_count = int(new_count) if new_count else None
            inventory = update_product(inventory, product_name, new_name or None, new_price, new_count)
            print(f"Товар '{product_name}' обновлен.")

        elif choice == '5':
            product_name = input("название товара для поиска: ")
            found_items = find_product(inventory, product_name)
            if found_items:
                print(show_inventory(found_items))
            else:
                print(f"Товар '{product_name}' не найден.")

        elif choice == '6':
            max_price = float(input("максимальную цену: "))
            filtered_items = filter_by_price(inventory, max_price)
            if filtered_items:
                print(show_inventory(filtered_items))
            else:
                print(f"Нет товаров с ценой ниже {max_price}.")

        elif choice == '7':
            max_count = int(input("максимальное количество: "))
            filtered_items = filter_by_count(inventory, max_count)
            if filtered_items:
                print(show_inventory(filtered_items))
            else:
                print(f"Нет товаров с количеством ниже {max_count}.")

        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, снова.")

menu(inventory)




###########################################################################################
###########################################################################################
###########################################################################################