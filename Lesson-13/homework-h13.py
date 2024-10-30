# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)
# ОТВЕТ:
def analyze_numbers(numbers):
    # Сумма всех чисел
    total_sum = sum(numbers)

    # Среднее значение
    average = total_sum / len(numbers) if numbers else 0  # Защита от деления на ноль

    # Количество четных чисел
    even_count = sum(1 for num in numbers if num % 2 == 0)

    return total_sum, average, even_count

# Пример использования
numbers = [1, 2, 3, 4, 5, 6]
result = analyze_numbers(numbers)
print(result)  # (21, 3.5, 3)

result = analyze_numbers(numbers)
print(result)  # (21, 3.5, 3)

# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)
def analyze_strings(strings):
    # Находим самую длинную строку
    longest_string = max(strings, key=len) if strings else ""

    # Находим самую короткую строку
    shortest_string = min(strings, key=len) if strings else ""

    # Подсчитываем количество строк, содержащих букву "a"
    count_strings_with_a = sum(1 for string in strings if 'a' in string)

    return longest_string, shortest_string, count_strings_with_a

strings = ["apple", "banana", "cherry", "date"]
result = analyze_strings(strings)
print(result)  # ('banana', 'date', 3)

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')
#
# ОТВЕТ:
def analyze_salaries(employees):
    # 1. Находим среднюю зарплату
    total_salary = sum(employees.values())  # Сумма всех зарплат
    average_salary = total_salary / len(employees) if employees else 0  # Средняя зарплата

    # 2. Находим максимальную зарплату и имя сотрудника с этой зарплатой
    max_salary = max(employees.values()) if employees else 0  # Максимальная зарплата
    max_salary_employee = max(employees, key=employees.get) if employees else None  # Имя сотрудника

    return average_salary, max_salary, max_salary_employee


# Пример использования
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
result = analyze_salaries(employees)
print(result)  # (6000.0, 7000, 'Bob')

# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)


# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
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

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]


