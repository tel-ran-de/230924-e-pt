# Тема: Обработка исключений (try/except/else/finally)
from django.db.models.expressions import result


# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.

def divide_numbers(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"
    except ValueError:
        return "Ошибка: ввод не числовых значений!"
    else:
        return result
    finally:
        print("Функция выполнена")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 'a'))



# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.

try:
    number = float(input("Введите число: "))
    square = number * number
    print(f"Квадрат числа {number} равен {square}")
except ValueError:

    print("Ошибка: введено не числовое значение!")



# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
try:
    # Открытие файла для чтения
    file = open("text_files/data.txt", "r")

    # 2. Прочитайте весь контент файла и выведите его на экран.
    content = file.read()
    print("Содержимое файла:")
    print(content)

    # 3. Прочитайте первые 10 символов файла и выведите их на экран.
    file.seek(0)
    file_read_10 = file.read(10)
    print("\nПервые 10 символов файла:")
    print(file_read_10)

    # 4. Прочитайте одну строку из файла и выведите ее на экран.
    file.seek(0)
    file_line = file.readline()
    print("\nПервая строка файла:")
    print(file_line)

    # 5. Прочитайте все строки файла и выведите их на экран.
    file.seek(0)
    all_lines = file.readlines()
    print("\nВсе строки файла:")
    print(all_lines)

    # Закрытие файла
    file.close()
except FileNotFoundError:
    print("Ошибка: файл 'text_files/data.txt' не найден!")
except PermissionError:
    print("Ошибка: нет разрешения на доступ к файлу 'text_files/data.txt'!")
except IOError as e:
    print(f"Ошибка ввода-вывода: {e}")
finally:
    print("Попытка чтения файла завершена")


# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Число должно быть положительным")
  #     # Добавьте проверку на отрицательное число и возбуждение исключения
    return math.sqrt(number)
#
def safe_calculate_square_root(number):
     try:
         result = calculate_square_root(number)
         print(f"Квадратный корень из {number} равен {result}")
     except ValueError as e:
         print(f"Ошибка: {e}")
#
# # Тесты функции
safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным


# Задача 2. Допишите код ниже.
def convert_to_number(string):
#     # Добавьте проверку на некорректное значение и возбуждение исключения
    if not string.isdigit():
        raise ValueError("Введенное значение не является числом")
    return int(string)
def safe_convert_to_number(string):
     try:
         number = convert_to_number(string)
         print(f"Конвертированное число: {number}")
     except ValueError as e:
         print(f"Ошибка: {e}")
#
# # Тесты функции
safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом


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

import json#импортирую модуль чтоб работать с файлами где хранятся данные инвентаря

# Проект: Управление инвентарем в интернет-магазине с проверками на ошибки

FILENAME = 'inventory.json'#имя файла, в котором будут храниться данные инвентаря.

def load_inventory(filename):#загружаю данные из файла inventory.json
    try:
        with open(filename, 'r', encoding='utf-8') as file:#открываю файл для чтения
            return json.load(file)
    except FileNotFoundError:#пишу ошибки которые могут возникнуть
        print(f"Ошибка: файл '{filename}' не найден!")
        return []
    except PermissionError:
        print(f"Ошибка: нет разрешения на доступ к файлу '{filename}'!")
        return []
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")
        return []

def save_inventory(filename, inventory): #функция сохраняет данные инвентаря в файл inventory.json
    try:
        with open(filename, 'w', encoding='utf-8') as file:#открываю файл для записи
            json.dump(inventory, file, indent=4)
    except PermissionError:#пишу ошибки которые могут возникнуть
        print(f"Ошибка: нет разрешения на запись в файл '{filename}'!")
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")

def show_inventory(inventory):#отображаю список товаров. Если список пуст, выводится сообщение "Список товаров пуст".
    if not inventory:
        print("Список товаров пуст.")
    else:
        for item in inventory:#запись есть - выводится список товара с ценой и кол-м
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")

def add_item(inventory, product, price, count):#добавление нового товара в инвентарь
    try:#задаю корректный ввод, если цена или количество не являются числами, выводится сообщение об ошибке
        price = float(price)
        count = int(count)
        inventory.append({'product': product, 'price': price, 'count': count})
        save_inventory(FILENAME, inventory)
        print("Товар успешно добавлен.")
    except ValueError:
        print("Ошибка: введены некорректные данные!")

def remove_item(inventory, product):#функция удаляет товар из инвентаря.
    # Если товар найден и удален, данные сохраняются в файл.
    # Если товар не найден, выводится сообщение об ошибке
    initial_length = len(inventory)
    inventory[:] = [item for item in inventory if item['product'] != product]
    if len(inventory) < initial_length:
        save_inventory(FILENAME, inventory)
        print("Товар успешно удален.")
    else:
        print("Ошибка: товар не найден!")

def update_item(inventory, product, price=None, count=None):#функция обновляет название, цену или количество товара.
    # Если введены некорректные данные, выводится сообщение об ошибке.
    # Если товар не найден, также выводится сообщение об ошибке
    for item in inventory:
        if item['product'] == product:
            try:
                if price is not None:
                    item['price'] = float(price)
                if count is not None:
                    item['count'] = int(count)
                save_inventory(FILENAME, inventory)
                print("Товар успешно обновлен.")
                return
            except ValueError:
                print("Ошибка: введены некорректные данные!")
                return
    print("Ошибка: товар не найден!")

def find_item(inventory, product):#ищу товар по названию и вывожу его данные.
    # Если товар не найден, выводится сообщение об ошибке.
    found_items = [item for item in inventory if item['product'] == product]
    if found_items:
        for item in found_items:
            print(f"Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print("Товар не найден.")

def filter_by_price(inventory, max_price):#Функция для фильтрации товаров по цене
    try:
        max_price = float(max_price)
        filtered_items = [item for item in inventory if item['price'] < max_price]
        show_inventory(filtered_items)
    except ValueError:
        print("Ошибка: введены некорректные данные!")

def filter_by_count(inventory, max_count):#по колличеству
    try:
        max_count = int(max_count)
        filtered_items = [item for item in inventory if item['count'] < max_count]
        show_inventory(filtered_items)
    except ValueError:
        print("Ошибка: введены некорректные данные!")

# Использование
inventory = load_inventory(FILENAME)

# Меню
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
        show_inventory(inventory)
    elif choice == '2':
        product = input("Введите название товара: ")
        price = input("Введите стоимость товара: ")
        count = input("Введите количество товара: ")
        add_item(inventory, product, price, count)
    elif choice == '3':
        product = input("Введите название товара для удаления: ")
        remove_item(inventory, product)
    elif choice == '4':
        product = input("Введите название товара для обновления: ")
        price = input("Введите новую стоимость (или нажмите Enter для пропуска): ")
        count = input("Введите новое количество (или нажмите Enter для пропуска): ")
        update_item(inventory, product, price if price else None, count if count else None)
    elif choice == '5':
        product = input("Введите название товара для поиска: ")
        find_item(inventory, product)
    elif choice == '6':
        max_price = input("Введите максимальную стоимость: ")
        filter_by_price(inventory, max_price)
    elif choice == '7':
        max_count = input("Введите максимальное количество: ")
        filter_by_count(inventory, max_count)
    elif choice == '8':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")



#игра hangman.py с исключениями, чтобы программа не завершалась с ошибкой при некорректном вводе.
import random

# Список слов
words = ["mouse", "elephant", "duck", "cat", "dog", "horse"]
# Подключаю рандом для выбора слова
word = random.choice(words)
# Создаем переменные и присваиваем им начальные значения
# - записываем угаданные буквы в список, неправильные попытки и количество попыток
guessed_letters = []  # Список угаданных букв
wrong_attempts = 0
max_attempts = 6

def display_game_state():
    display_word = ""  # Пустая строка для записи и показа состояния отгадывания слова
    for letter in word:  # Проходим по каждой букве в загаданном слове
        if letter in guessed_letters:  # Если буква есть в guessed_letters
            display_word += letter  # Добавляем ее к строке display_word
        else:
            display_word += "*"  # Если нет, то ставим звезду
    print(display_word)

# Функция для обработки букв, принимает один аргумент letter
def process_letter(letter):
    global wrong_attempts
    if letter in word:  # Проверяем, содержится ли введенная буква в загаданном слове word
        guessed_letters.append(letter)  # Добавляем букву в guessed_letters, если она есть в word
    else:
        wrong_attempts += 1  # Иначе увеличиваем количество неправильных попыток на 1

def display_hangman(attempts):  # Берем один аргумент attempts
    stages = [  # Список отображения этапов угадывания
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]

    return stages[attempts]  # Возврат строки из списка этапов соответственно текущему количеству неправильных попыток

while wrong_attempts < max_attempts:  # В цикле пока число неправильных попыток меньше максимальных
    print(display_hangman(wrong_attempts))  # На начало каждой итерации отображаем этап виселицы
    display_game_state()  # Показываем текущее состояние слова
    try:
        letter = input("Введите букву: ").lower()
        if len(letter) != 1 or not letter.isalpha():  # Проверка на корректность ввода
            raise ValueError("Ошибка: введите одну букву.")
        if letter in guessed_letters:  # Если буква уже была угадана
            print("Вы уже угадали эту букву.")  # Выводится сообщение
            continue  # Идем на следующий круг
        process_letter(letter)  # Если буква не была угадана ранее, передаем букву в функцию process_letter для обработки
        if all(letter in guessed_letters for letter in word):  # После обработки буквы проверяем, угаданы ли все буквы в слове
            print(f"Поздравляем, вы выиграли! Загаданное слово: {word}")
            break
    except ValueError as e:
        print(e)
else:  # Если количество неправильных попыток равно максимальному значению, цикл завершается
    print(display_hangman(wrong_attempts))
    print(f"Вы проиграли! Загаданное слово было: {word}")  # Отображается сообщение о поражении



