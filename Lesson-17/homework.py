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


# math_operations.py

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

# Этот блок выполняется, только если файл запускается напрямую
if __name__ == "__main__":
    print("Модуль запущен напрямую")






import math_operations

# Пример использования функций
a = 10
b = 5

# Умножение
result_multiply = math_operations.multiply(a, b)
print(f"{a} * {b} = {result_multiply}")

# Вычитание
result_subtract = math_operations.subtract(a, b)
print(f"{a} - {b} = {result_subtract}")

# Деление
result_divide = math_operations.divide(a, b)
print(f"{a} / {b} = {result_divide}")







# Тема: модули random, math
# Основные функции этих модулей есть в файле examples.

# Задание 1: Округление и вычисление квадратного корня
# Напишите функцию, которая принимает на вход два числа: одно для округления вверх, другое для округления вниз.
# Затем программа должна вычислить квадратный корень каждого округленного числа и вывести результаты.




import math


def round_and_sqrt(ceil_num, floor_num):
    # Округляем вверх и вниз
    ceil_rounded = math.ceil(ceil_num)
    floor_rounded = math.floor(floor_num)

    # Вычисляем квадратные корни
    sqrt_ceil = math.sqrt(ceil_rounded)
    sqrt_floor = math.sqrt(floor_rounded)

    print(f"Число {ceil_num} округлено вверх до {ceil_rounded}, квадратный корень: {sqrt_ceil}")
    print(f"Число {floor_num} округлено вниз до {floor_rounded}, квадратный корень: {sqrt_floor}")


# Пример использования
round_and_sqrt(7.3, 15.8)







# Задание 2: Факториал и возведение в степень
# Напишите функцию, которая вычисляет факториал числа, а затем возводит результат в степень,
# равную количеству цифр в этом факториале. Выведите результат.





import math


def factorial_and_power(number):
    # Вычисляем факториал
    factorial_result = math.factorial(number)

    # Считаем количество цифр в факториале
    digits_count = len(str(factorial_result))

    # Возводим факториал в степень, равную количеству цифр
    result = math.pow(factorial_result, digits_count)

    print(f"Факториал числа {number} равен {factorial_result}.")
    print(f"Результат возведения в степень {digits_count}: {result}")


# Пример использования
factorial_and_power(5)





# Задание 3: Перемешивание списка и выбор элемента
# Напишите функцию, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Перемешайте список и выберите один случайный элемент. Выведите результат.


import random


def shuffle_and_choose():
    # Генерация списка случайных чисел
    random_list = [random.randint(1, 100) for _ in range(10)]

    # Перемешивание списка
    random.shuffle(random_list)

    # Выбор случайного элемента
    chosen_element = random.choice(random_list)

    print(f"Перемешанный список: {random_list}")
    print(f"Случайно выбранный элемент: {chosen_element}")


# Пример использования
shuffle_and_choose()






# Задание 4: Отбрасывание дробной части и факториал
# Напишите программу, которая принимает дробное число, отбрасывает его дробную часть,
# а затем вычисляет факториал полученного целого числа. Выведите результат.




import math


def drop_fraction_and_factorial(number):
    # Отбрасываем дробную часть
    integer_part = math.floor(number)

    # Вычисляем факториал
    factorial_result = math.factorial(integer_part)

    print(f"Число {number} после отбрасывания дробной части: {integer_part}")
    print(f"Факториал {integer_part} равен: {factorial_result}")


# Пример использования
drop_fraction_and_factorial(7.85)





# Задание 5: Генерация и округление случайного числа
# Напишите программу, которая генерирует случайное дробное число в диапазоне от 1.5 до 10.5,
# округляет его до ближайшего целого в меньшую и большую сторону, а затем выводит результаты.




import random
import math


def generate_and_round():
    # Генерация случайного числа в диапазоне от 1.5 до 10.5
    random_number = random.uniform(1.5, 10.5)

    # Округление вниз и вверх
    rounded_down = math.floor(random_number)
    rounded_up = math.ceil(random_number)

    print(f"Сгенерированное число: {random_number}")
    print(f"Округлено вниз: {rounded_down}, округлено вверх: {rounded_up}")


# Пример использования
generate_and_round()






# Тема: Сторонние модули

# Задание: Установка Django в виртуальную среду
#
# 1. Установка виртуального окружения
# Создайте отдельную папку для выполнения задания. Перейдите в эту папку в терминале (команда cd <название папки>)
# Для создания виртуальной среды используйте модуль `venv`, который встроен в Python 3.
# Находясь в папке задания в терминале введите python -m venv myenv
#

bash
mkdir django_project
cd django_project

python -m venv myenv



# 2. Активация виртуальной среды
# После создания виртуального окружения, его нужно активировать.
# На Windows: myenv\\Scripts\\activate
# На MacOS и Linux: source myenv/bin/activate
#

myenv\Scripts\activate

source myenv/bin/activate

# 3. Установка Django
# Когда виртуальная среда активирована, можно установить Django с помощью `pip`.
# pip install django
#


bash
pip install django


# 4. Проверка установки Django
# После установки Django проверьте его версию, чтобы убедиться, что установка прошла успешно.
# django-admin --version
#

django-admin --version

4.1.7

# 5. Создайте файл requirements.txt, где будет указан django.
#
# После завершения работы в виртуальной среде, её можно деактивировать: deactivate


pip freeze > requirements.txt


makefile
Django==4.1.7

"deaktivazija"

deactivate


######################################################################



# Шаг 1: Создание папки и виртуального окружения

mkdir django_project
cd django_project
python -m venv myenv


# Шаг 2: Активация виртуального окружения
# Для Windows:

myenv\Scripts\activate
# Для MacOS/Linux:
source myenv/bin/activate


# Шаг 3: Установка Django

pip install django

# Шаг 4: Проверка установки Django

django-admin --version

# Шаг 5: Создание файла requirements.txt

pip freeze > requirements.txt

# Шаг 6: Деактивация виртуального окружения

deactivate

