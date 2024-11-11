# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.


# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.


# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.


# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
# import math
#
# def calculate_square_root(number):
#     # Добавьте проверку на отрицательное число и возбуждение исключения
#
#     return math.sqrt(number)
#
# def safe_calculate_square_root(number):
#     try:
#         result = calculate_square_root(number)
#         print(f"Квадратный корень из {number} равен {result}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
# safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным


# Задача 2. Допишите код ниже.
# def convert_to_number(string):
#     # Добавьте проверку на некорректное значение и возбуждение исключения
#
#     return int(string)
#
# def safe_convert_to_number(string):
#     try:
#         number = convert_to_number(string)
#         print(f"Конвертированное число: {number}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
# safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8, 14, добавив в него обработку ошибок, где это необходимо.
#
# Используйте файл как базу данных проекта.
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







