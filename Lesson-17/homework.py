# Тема: Создание модулей

# Задание: Создание и использование собственного модуля
#
# Часть 1: Создание модуля
#
# 1. Создайте файл с именем `math_operations.py`.
# 2. В этом файле определите три функции:
#     - `multiply(a, b)`: возвращает произведение двух чисел `a` и `b`.
#     - `subtract(a, b)`: возвращает разность между двумя числами `a` и `b`.
#     - `divide(a, b)`: возвращает результат деления числа `a` на `b`.
# 3. Включите конструкцию `if __name__ == "__main__"`, которая будет выполнять принт сообщения,
# если модуль запущен напрямую: “Модуль запущен напрямую”.
#
# math_operations.py

# def multiply(a, b):
#     """Returns the product of two numbers a and b."""
#     return a * b

# def subtract(a, b):
#     """Returns the difference between two numbers a and b."""
#     return a - b

# def divide(a, b):
#     """Returns the result of dividing a by b."""
#     if b == 0:
#         raise ValueError("Cannot divide by zero.")
#     return a / b

# if __name__ == "__main__":
#     print("Модуль запущен напрямую")


# Часть 2: Использование модуля
#
# 1. Создайте другой файл с именем `main.py`.
# 2. Импортируйте в этот файл созданный вами модуль `math_operations`.
# 3. Используйте функции из модуля для выполнения операций умножения, вычитания и деления,
# и выведите результаты на экран.
# 4. Затем запустите напрямую модуль `math_operations.py`
# и проверьте, что отработало сообщение “Модуль запущен напрямую”.
# main.py

# import math_operations as mo

# a = 10
# b = 5

# print("Умножение:", mo.multiply(a, b))
# print("Вычитание:", mo.subtract(a, b))
# print("Деление:", mo.divide(a, b))


# Тема: модули random, math
# Основные функции этих модулей есть в файле examples.

import math


def calculate_sqrt(round_up, round_down):
    # Округляем числа
    rounded_up = math.ceil(round_up)  # Округление вверх
    rounded_down = math.floor(round_down)  # Округление вниз

    # Вычисляем квадратные корни
    sqrt_up = math.sqrt(rounded_up)
    sqrt_down = math.sqrt(rounded_down)

    # Выводим результаты
    print(f"Округленное вверх: {rounded_up}, Квадратный корень: {sqrt_up}")
    print(f"Округленное вниз: {rounded_down}, Квадратный корень: {sqrt_down}")


# Пример использования функции
calculate_sqrt(4.3, 9.8)

# Задание 1: Округление и вычисление квадратного корня
# Напишите функцию, которая принимает на вход два числа: одно для округления вверх, другое для округления вниз.
# Затем программа должна вычислить квадратный корень каждого округленного числа и вывести результаты.

import math


def calculate_sqrt(round_up, round_down):
    # Округляем числа
    rounded_up = math.ceil(round_up)  # Округление вверх
    rounded_down = math.floor(round_down)  # Округление вниз

    # Вычисляем квадратные корни
    sqrt_up = math.sqrt(rounded_up)
    sqrt_down = math.sqrt(rounded_down)

    # Выводим результаты
    print(f"Округленное вверх: {rounded_up}, Квадратный корень: {sqrt_up}")
    print(f"Округленное вниз: {rounded_down}, Квадратный корень: {sqrt_down}")


# Пример использования функции
calculate_sqrt(4.3, 9.8)

# Задание 2: Факториал и возведение в степень
# Напишите функцию, которая вычисляет факториал числа, а затем возводит результат в степень,
# равную количеству цифр в этом факториале. Выведите результат.

import math


def factorial_power(n):
    # Вычисляем факториал числа n
    factorial_result = math.factorial(n)

    # Преобразуем факториал в строку, чтобы посчитать количество цифр
    num_digits = len(str(factorial_result))

    # Возводим факториал в степень, равную количеству цифр
    result = factorial_result ** num_digits

    # Выводим результат
    print(f"Факториал {n}! равен {factorial_result}, "
          f"количество цифр: {num_digits}, "
          f"результат возведения в степень: {result}")


# Пример использования функции
factorial_power(5)

# Задание 3: Перемешивание списка и выбор элемента
# Напишите функцию, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Перемешайте список и выберите один случайный элемент. Выведите результат.

import random


def random_list_selection():
    # Создаем список из 10 случайных чисел от 1 до 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]

    # Перемешиваем список
    random.shuffle(random_numbers)

    # Выбираем один случайный элемент из перемешанного списка
    selected_number = random.choice(random_numbers)

    # Выводим результаты
    print(f"Сгенерированный список: {random_numbers}")
    print(f"Выбранный случайный элемент: {selected_number}")


# Пример использования функции
random_list_selection()

# Задание 4: Отбрасывание дробной части и факториал
# Напишите программу, которая принимает дробное число, отбрасывает его дробную часть,
# а затем вычисляет факториал полученного целого числа. Выведите результат.

import math


def calculate_factorial_of_truncated(number):
    # Отбрасываем дробную часть
    truncated_number = math.trunc(number)
    print(f"Отброшена дробная часть, осталось целое число: {truncated_number}")

    # Вычисляем факториал целого числа
    try:
        factorial_result = math.factorial(truncated_number)
        print(f"Факториал числа {truncated_number} равен: {factorial_result}")
    except ValueError:
        print("Факториал определен только для неотрицательных целых чисел.")


# Пример использования
number = float(input("Введите дробное число: "))
calculate_factorial_of_truncated(number)

# Задание 5: Генерация и округление случайного числа
# Напишите программу, которая генерирует случайное дробное число в диапазоне от 1.5 до 10.5,
# округляет его до ближайшего целого в меньшую и большую сторону, а затем выводит результаты.

import random
import math


def generate_and_round():
    # Генерируем случайное дробное число от 1.5 до 10.5
    random_number = random.uniform(1.5, 10.5)
    print(f"Случайное число: {random_number}")

    # Округление вниз
    rounded_down = math.floor(random_number)
    print(f"Округление вниз: {rounded_down}")

    # Округление вверх
    rounded_up = math.ceil(random_number)
    print(f"Округление вверх: {rounded_up}")


# Запуск функции
generate_and_round()

# Тема: Сторонние модули

# Задание: Установка Django в виртуальную среду
#
# 1. Установка виртуального окружения
# Создайте отдельную папку для выполнения задания. Перейдите в эту папку в терминале (команда cd <название папки>)
# Для создания виртуальной среды используйте модуль `venv`, который встроен в Python 3.
# Находясь в папке задания в терминале введите python -m venv myenv
#
# 2. Активация виртуальной среды
# После создания виртуального окружения, его нужно активировать.
# На Windows: myenv\\Scripts\\activate
# На MacOS и Linux: source myenv/bin/activate
#
# 3. Установка Django
# Когда виртуальная среда активирована, можно установить Django с помощью `pip`.
# pip install django
#
# 4. Проверка установки Django
# После установки Django проверьте его версию, чтобы убедиться, что установка прошла успешно.
# django-admin --version
#
# 5. Создайте файл requirements.txt, где будет указан django.

# DJANGO и библиотеки установлены, создан файл requirements.txt, в файле указан django.

# После завершения работы в виртуальной среде, её можно деактивировать: deactivate
