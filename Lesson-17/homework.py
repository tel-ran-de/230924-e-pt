# Тема: Создание модулей

# Задание: Создание и использование собственного модуля
#
# Часть 1: Создание модуля
#
# 1. Создайте файл с именем `math_operations.py`.
# создан файл с именем `math_operations.py

# 2. В этом файле определите три функции:
#     - `multiply(a, b)`: возвращает произведение двух чисел `a` и `b`.
#     - `subtract(a, b)`: возвращает разность между двумя числами `a` и `b`.
#     - `divide(a, b)`: возвращает результат деления числа `a` на `b`.
# 3. Включите конструкцию `if __name__ == "__main__"`, которая будет выполнять принт сообщения,
# если модуль запущен напрямую: “Модуль запущен напрямую”.
#
# Часть 2: Использование модуля
#
# 1. Создайте другой файл с именем `main.py`.
# 2. Импортируйте в этот файл созданный вами модуль `math_operations`.
# 3. Используйте функции из модуля для выполнения операций умножения, вычитания и деления,
# и выведите результаты на экран.
# 4. Затем запустите напрямую модуль `math_operations.py`
# и проверьте, что отработало сообщение “Модуль запущен напрямую”.
# отработано


# Тема: модули random, math
# Основные функции этих модулей есть в файле examples.

# Задание 1: Округление и вычисление квадратного корня
# Напишите функцию, которая принимает на вход два числа: одно для округления вверх, другое для округления вниз.
# Затем программа должна вычислить квадратный корень каждого округленного числа и вывести результаты.
import math
from itertools import count
from math import floor, factorial


def calculation(up, down):
    rounded_up = math.ceil(up)
    rounded_down = math.floor(down)

    sqrt_up = math.sqrt(rounded_up)
    sqrt_down = math.sqrt(rounded_down)

    return  sqrt_up, sqrt_down
print(math.ceil(8.2))
print(math.floor(8.2))

print(calculation(8.2, 8.2))

# Задание 2: Факториал и возведение в степень
# Напишите функцию, которая вычисляет факториал числа, а затем возводит результат в степень,
# равную количеству цифр в этом факториале. Выведите результат.


def calculation_power(n):
    factorial = math.factorial(n)
    count_digits = len(str(factorial))
    result = factorial ** count_digits
    return result

print(f"вычисление факториала 5: {factorial(5)}")
print(f"возведение факториала в степень 3: {calculation_power(5)}")

# Задание 3: Перемешивание списка и выбор элемента
# Напишите функцию, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Перемешайте список и выберите один случайный элемент. Выведите результат.
import random


def shuffle_and_select():
    random_list = [random.randint(1, 100) for _ in range(10)]
    random.shuffle(random_list)
    selected_element = random.choice(random_list)
    print(random_list)
    print(f"Список после перемешивания: {random_list}")
    print(f"Выбранный случайный элемент: {selected_element}")

shuffle_and_select()

# Задание 4: Отбрасывание дробной части и факториал
# Напишите программу, которая принимает дробное число, отбрасывает его дробную часть,
# а затем вычисляет факториал полученного целого числа. Выведите результат.

import math

def factorial_of_integer_part(number):
    integer_part = int(number)
    factorial = math.factorial(integer_part)
    return factorial

decimal_number = 5.2
result = factorial_of_integer_part(decimal_number)
print(f"Факториал целой части числа {decimal_number} ({int(decimal_number)}): {result}")

# Задание 5: Генерация и округление случайного числа
# Напишите программу, которая генерирует случайное дробное число в диапазоне от 1.5 до 10.5,
# округляет его до ближайшего целого в меньшую и большую сторону, а затем выводит результаты.

def generate_and_round():
    random_number = random.uniform(1.5, 10.5)
    rounded_down = math.floor(random_number)
    rounded_up = math.ceil(random_number)

    print(f"Случайное дробное число: {random_number}")
    print(f"Округлено в меньшую сторону: {rounded_down}")
    print(f"Округлено в большую сторону: {rounded_up}")

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
# 4. Проверка установки Djacngo
# После установки Django проверьте его версию, чтобы убедиться, что установка прошла успешно.
# django-admin --version
#
# 5. Создайте файл requirements.txt, где будет указан django.
#
# После завершения работы в виртуальной среде, её можно деактивировать: deactivate