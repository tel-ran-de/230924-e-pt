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
# Часть 2: Использование модуля
#
# 1. Создайте другой файл с именем `main.py`.
# 2. Импортируйте в этот файл созданный вами модуль `math_operations`.
# 3. Используйте функции из модуля для выполнения операций умножения, вычитания и деления,
# и выведите результаты на экран.
# 4. Затем запустите напрямую модуль `math_operations.py`
# и проверьте, что отработало сообщение “Модуль запущен напрямую”.


# Тема: модули random, math
# Основные функции этих модулей есть в файле examples.

# Задание 1: Округление и вычисление квадратного корня
# Напишите функцию, которая принимает на вход два числа: одно для округления вверх, другое для округления вниз.
# Затем программа должна вычислить квадратный корень каждого округленного числа и вывести результаты.
import math, random

def round_and_aqrt(up_num, down_num):
    round_up = math.ceil(up_num)
    round_down = math.floor(down_num)

    sqrt_up_num = math.sqrt(up_num)
    sqrt_down_num = math.sqrt(down_num)
    print(f'Квадратный корень числа {round_up}: {sqrt_up_num}')
    print(f'Квадратный корень числа {round_down}: {sqrt_down_num}')

round_and_aqrt(6.8, 9.3)
print('=============================================')
# Задание 2: Факториал и возведение в степень
# Напишите функцию, которая вычисляет факториал числа, а затем возводит результат в степень,
# равную количеству цифр в этом факториале. Выведите результат.
def factorial_and_power(n):
    factorial_num = math.factorial(n)
    num_len = len(str(factorial_num))
    result = factorial_num ** num_len
    print(f"Факториал числа {n}: {factorial_num}")
    print(f"Количество цифр в факториале: {num_len}")
    print(f"Результат возведения факториала в степень {num_len}: {result}")

factorial_and_power(7)
print('=============================================')
# Задание 3: Перемешивание списка и выбор элемента
# Напишите функцию, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Перемешайте список и выберите один случайный элемент. Выведите результат.
def random_numbs(n):
    numbers = random.sample(range(1, 100), n)
    random_num = random.choice(numbers)
    print("Список случайных чисел:", numbers)
    print("Случайное выбранное число:", random_num)

random_numbs(10)

print('=============================================')
# Задание 4: Отбрасывание дробной части и факториал
# Напишите программу, которая принимает дробное число, отбрасывает его дробную часть,
# а затем вычисляет факториал полученного целого числа. Выведите результат.
def fractional_number(n):
    int_number = math.trunc(n)
    frac_number = math.factorial(int_number)

    print(f'факториал полученного целого числа: {frac_number}')
fractional_number(6.33)
print('=============================================')
# Задание 5: Генерация и округление случайного числа
# Напишите программу, которая генерирует случайное дробное число в диапазоне от 1.5 до 10.5,
# округляет его до ближайшего целого в меньшую и большую сторону, а затем выводит результаты.
def random_numbers(a, b):
    rand_num = random.uniform(a, b)
    round_up = math.ceil(rand_num)
    round_down = math.floor(rand_num)
    print(f'Округление до ближайшего целого в большую сторону: {round_up}')
    print(f'Округление до ближайшего целого в меньшую сторону: {round_down}')
random_numbers(1.5, 10.5)
print('=============================================')
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
#
# После завершения работы в виртуальной среде, её можно деактивировать: deactivate