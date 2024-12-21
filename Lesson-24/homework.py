# Тема: Модуль datetime
#
from collections.abc import ValuesView
from zipfile import compressor_names
from pkg_resources import empty_provider

from datetime import datetime
#
#
# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45
#
#
from datetime import datetime
#
#
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Текущая дата и время:", formatted_datetime)


# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.
#
# #
#
from datetime import datetime


birth_date = input("Введите вашу дату рождения (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
current_date = datetime.now()
age = current_date.year - birth_date.year
if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1
print("Ваш возраст:", age)

#
#
#
# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.
#
from datetime import datetime

event_date = input("Введите дату следующего мероприятия (YYYY-MM-DD): ")
event_date = datetime.strptime(event_date, "%Y-%m-%d")
current_date = datetime.now()
days_left = (event_date - current_date).days
print(f"До мероприятия осталось {days_left} дней.")


#
# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.
# #





from datetime import datetime

date_input = input("Введите дату (YYYY-MM-DD): ")
date_object = datetime.strptime(date_input, "%Y-%m-%d")
day_of_week = date_object.strftime("%A")
print(f"День недели для {date_input}:", day_of_week)
#
#





# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.
#




from datetime import datetime


date_1 = input("Введите первую дату (YYYY-MM-DD): ")
date_2 = input("Введите вторую дату (YYYY-MM-DD): ")

# "строки в объекты, даты"
date_1 = datetime.strptime(date_1, "%Y-%m-%d")
date_2 = datetime.strptime(date_2, "%Y-%m-%d")

# "Сравниваем"
if date_1 > date_2:
    print(f"Первая дата ({date_1.date()}) позже второй.")
elif date_1 < date_2:
    print(f"Вторая дата ({date_2.date()}) позже первой.")
else:
    print(" даты одинаковы.")
#
#
#
#
# # Тема: Модуль os
#
# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.
#

import os

 # 1."test_directory"
os.mkdir("test_directory")
print("Директория 'test_directory' успешно создана.")

# 2. Выводим список
print("\nСписок директорий в текущем каталоге:")
for item in os.listdir():
    if os.path.isdir(item):
        print(item)

# 3. Удаляем "test_directory"
os.rmdir("test_directory")
print("\nДиректория 'test_directory' успешно удалена.")

#
# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.
#


import os



# 1. "Создаем файл "temp_file.txt"

with open("temp_file.txt", "w") as file:
    file.write("Temporary content")
print("Файл 'temp_file.txt' создан и в него записан текст.")



# 2. "Переименовываем файл в "renamed_file.txt"

os.rename("temp_file.txt", "renamed_file.txt")
print("Файл переименован в 'renamed_file.txt'.")



# 3. "Выводим список всех файлов"

print("\nСписок файлов в текущем каталоге:")
for item in os.listdir():
    if os.path.isfile(item):
        print(item)





# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".
# #



import os


file_name = "example.txt"
if os.path.exists(file_name):
    file_size = os.path.getsize(file_name)
    print(f"Файл '{file_name}' найден. Размер файла: {file_size} байт.")
else:

    print("Файл не найден.")

#



# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".




import os


file_1 = input("Введите имя первого файла: ")
file_2 = input("Введите имя второго файла: ")

if os.path.exists(file_1) and os.path.exists(file_2):
    size_1 = os.path.getsize(file_1)
    size_2 = os.path.getsize(file_2)

    if size_1 > size_2:
        print(f"Файл '{file_1}' больше ({size_1} байт).")
    elif size_1 < size_2:
        print(f"Файл '{file_2}' больше ({size_2} байт).")
    else:
        print("Файлы имеют одинаковый размер.")
else:
    print("Один или оба файла не существуют.")

#
#


# Тема: Интеграционная практика.

# Проект: Перепишите проект из уроков 7-8, 14-15, добавив в него фичи 1 - 3 на основе модулей datetime и os.
#
# Фича 1. Добавьте в каждый товар дату и время его создания,
# а также дату и время обновления данных о товаре или количества товара.
#
# Фича 2: Логирование действий с товарами
# Создайте лог-файл, куда будет записываться история всех действий с товарами (добавление, удаление, обновление).
# Используйте модуль datetime для добавления временных меток к каждому действию с товарами.
#
# Фича 3. Резервное копирование данных:
# Используйте модуль os для создания резервных копий файла с товарами.
# Например, при каждом запуске программы создается копия файла с добавлением текущей даты и времени.
#
#
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
# Используйте файл как базу данных проекта.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.






import os
import datetime

# Файл для хранения товаров
inventory_file = "inventory.txt"
log_file = "inventory_log.txt"

# Функция для логирования действий
def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as log:
        log.write(f"{timestamp} - {action}\n")

# Функция для создания резервной копии файла инвентаря
def create_backup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"inventory_backup_{timestamp}.txt"
    with open(inventory_file, "r") as original_file:
        with open(backup_filename, "w") as backup_file:
            backup_file.write(original_file.read())
    log_action(f"Резервная копия создана: {backup_filename}")

# Чтение всех товаров из файла
def read_inventory():
    inventory = []
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                name = parts[0]
                price = float(parts[1])
                quantity = int(parts[2])
                created_at = parts[3]
                updated_at = parts[4]
                inventory.append({"name": name, "price": price, "quantity": quantity, "created_at": created_at, "updated_at": updated_at})
    return inventory

# "Сохранение в файл"
def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        for item in inventory:
            file.write(f"{item['name']},{item['price']},{item['quantity']},{item['created_at']},{item['updated_at']}\n")

# "Показать список"
def show_inventory():
    inventory = read_inventory()
    if inventory:
        print("Список товаров:")
        for item in inventory:
            print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}, "
                  f"Дата создания: {item['created_at']}, Дата обновления: {item['updated_at']}")
    else:
        print("Нет товаров в базе.")

# Добавить товар
def add_product():
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    created_at = updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    inventory = read_inventory()
    inventory.append({"name": name, "price": price, "quantity": quantity, "created_at": created_at, "updated_at": updated_at})
    save_inventory(inventory)
    log_action(f"Добавлен товар: {name}")

# Удалить товар
def remove_product():
    name = input("Введите название товара для удаления: ")
    inventory = read_inventory()
    inventory = [item for item in inventory if item['name'] != name]
    save_inventory(inventory)
    log_action(f"Удален товар: {name}")

# Обновить товар
def update_product():
    name = input("Введите название товара для обновления: ")
    inventory = read_inventory()
    for item in inventory:
        if item['name'] == name:
            print(f"Текущие данные товара: Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
            price = float(input("Введите новую цену товара: "))
            quantity = int(input("Введите новое количество товара: "))
            item['price'] = price
            item['quantity'] = quantity
            item['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_inventory(inventory)
            log_action(f"Обновлен товар: {name}")
            return
    print("Товар не найден.")

# Найти товар по названию
def find_product():
    name = input("Введите название товара для поиска: ")
    inventory = read_inventory()
    found = False
    for item in inventory:
        if item['name'] == name:
            found = True
            print(f"Товар найден: Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}, "
                  f"Дата создания: {item['created_at']}, Дата обновления: {item['updated_at']}")
            break
    if not found:
        print("Товар не найден.")

# Вывести товары по цене
def products_below_price():
    price = float(input("Введите максимальную цену для фильтрации: "))
    inventory = read_inventory()
    filtered = [item for item in inventory if item['price'] < price]
    if filtered:
        print("Товары ниже заданной цены:")
        for item in filtered:
            print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
    else:
        print("Нет товаров с такой ценой.")

# Вывести товары по количеству
def products_below_quantity():
    quantity = int(input("Введите минимальное количество для фильтрации: "))
    inventory = read_inventory()
    filtered = [item for item in inventory if item['quantity'] < quantity]
    if filtered:
        print("Товары с количеством меньше заданного:")
        for item in filtered:
            print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
    else:
        print("Нет товаров с таким количеством.")

# Главное меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Показать список товаров")
        print("2. Добавить товар")
        print("3. Удалить товар")
        print("4. Обновить товар")
        print("5. Найти товар по названию")
        print("6. Вывести товары с ценой ниже заданной")
        print("7. Вывести товары с количеством ниже заданного")
        print("8. Создать резервную копию данных")
        print("9. Выход")
        choice = input("Выберите действие (1-9): ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            find_product()
        elif choice == "6":
            products_below_price()
        elif choice == "7":
            products_below_quantity()
        elif choice == "8":
            create_backup()
        elif choice == "9":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    menu()





#
# class Company:
#  company_name = "Killer Company"
#
#  def __init__(self,company_name):
#      self.company_name = company_name
#      self.employees = []
#
#
#
#  class Employee:
#
#      def __init__(self,name,killer,salary):
#          self.employees = []
#          self.name = name
#          self.killer = killer
#
#  def add_employees(self, employee_name):
#      if isinstance(employee, Employee):
#          self.employees.append(employee_name)
#      else:
#          raise ValueError("employee dolschen wijasnitj")
#
# company= Company("Killer Company")
#
# company.company_name1 = "Killer"
# employee1 = ("Employee:","Bob", "Soldat", 5000)
# employee2 = ("Employee:", "Jana", "Soldat",3000)
#
# company.add_employee1 = "Bob","Soldat - Sniper" , 5000
# company.add_employee2 = "Jana","Soldatin - Hilfe" , 3000
#
# print(f"Company name :{company.company_name1}")
# print("Employees:",company.add_employee1 )
# print("Employees:", company.add_employee2 )
#
#
# #########################################################################################
#
#
# class Company:
#  company_name = "Killer Company"
#
#  def __init__(self):
#      self.company_name = Company
#      self.employees = []
#
#
#
#
# class Employee:
#
#  def __init__(self,name,killer,salary):
#      self.employees = []
#      self.name = name
#      self.killer = killer
#      self.salary = salary
#
#
#  def add_employees(self, employee_name):
#      self.employees.append(employee_name)
#
#  def get_employees(self):
#      return self.employees
#
#
#
# employee1 = Employee("Bob", "Soldat", 5000)
# employee2 = Employee("Jana", "Soldat",3000)
#
# company= Company()
# company.company_name1 = "Killer"
# company.company_name2 = "Bob" , "Jana"
# company.add_employee1 = "Bob","Soldat - Sniper" , 5000
# company.add_employee2 = "Jana","Soldatin - Hilfe" , 3000
#
# print(f"Company name :{company.company_name1},{company.company_name2}")
# print("Employees:",company.add_employee1 )
# print("Employees:", company.add_employee2 )




########################################################################################################
########################################################################################################
########################################################################################################

#
#
# class Library:
#     def __init(self,total_books):
#         self.total_books = total_books
#         total_books = 0
#         self.books = []
#
#
#     def add_books(self,book_name):
#         self.books.append(book_name)
#         Library.total_books +=1
#
#
#
#
#
#
# def get_age(self):
#     return self.__age
#
#
# def set__age(self, age):
#     if age > 0:
#         self.__age = age
#     else:
#         print("Age muss be positive")
#
#         print = Person("Alice", 30)
#         print(Person.name)
#         print(Person.age)
#









