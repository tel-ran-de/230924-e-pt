# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)
def analyze_numbers(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    even_count = len([num for num in numbers if num % 2 == 0])
    return total_sum, average, even_count

numbers = [1, 2, 3, 4, 5, 6]

print(analyze_numbers(numbers))  # (21, 3.5, 3)


# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)
def analyze_strings(strings):
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    count_a = len([string for string in strings if 'a' in string])
    return longest, shortest, count_a

strings = ["apple", "banana", "cherry", "date"]

print(analyze_strings(strings))  # ('banana', 'date', 3)


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')
def analyze_salaries(employees):
    average_salary = sum(employees.values()) / len(employees)
    max_salary = max(employees.values())
    employee_max_salary = max(employees, key=employees.get)
    return average_salary, max_salary, employee_max_salary

employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}

print(analyze_salaries(employees))  # (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
def filter_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_numbers(numbers))  # ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
