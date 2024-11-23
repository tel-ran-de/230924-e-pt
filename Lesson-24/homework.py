# Тема: Модуль datetime
from collections.abc import ValuesView
from zipfile import compressor_names

from pkg_resources import empty_provider


# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45


# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.


# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.


# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.


# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.


# Тема: Модуль os

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.


# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.


# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".


# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".


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



class Company:
 company_name = "Killer Company"

 def __init__(self,company_name):
     self.company_name = company_name
     self.employees = []



 class Employee:

     def __init__(self,name,killer,salary):
         self.employees = []
         self.name = name
         self.killer = killer

 def add_employees(self, employee_name):
     if isinstance(employee, Employee):
         self.employees.append(employee_name)
     else:
         raise ValueError("employee dolschen wijasnitj")

company= Company("Killer Company")

company.company_name1 = "Killer"
employee1 = ("Employee:","Bob", "Soldat", 5000)
employee2 = ("Employee:", "Jana", "Soldat",3000)

company.add_employee1 = "Bob","Soldat - Sniper" , 5000
company.add_employee2 = "Jana","Soldatin - Hilfe" , 3000

print(f"Company name :{company.company_name1}")
print("Employees:",company.add_employee1 )
print("Employees:", company.add_employee2 )


#########################################################################################


class Company:
 company_name = "Killer Company"

 def __init__(self):
    self.employees = []




class Employee:

 def __init__(self,name,killer,salary):
     self.employees = []
     self.name = name
     self.killer = killer
     self.salary = salary


 def add_employees(self, employee_name):
     self.employees.append(employee_name)

 def get_employees(self):
     return self.employees



employee1 = Employee("Bob", "Soldat", 5000)
employee2 = Employee("Jana", "Soldat",3000)

company= Company()
company.company_name1 = "Killer"
company.company_name2 = "Bob" , "Jana"
company.add_employee1 = "Bob","Soldat - Sniper" , 5000
company.add_employee2 = "Jana","Soldatin - Hilfe" , 3000

print(f"Company name :{company.company_name1},{company.company_name2}")
print("Employees:",company.add_employee1 )
print("Employees:", company.add_employee2 )




########################################################################################################
########################################################################################################
########################################################################################################



class Library:
    def __init(self,total_books):
        self.total_books = total_books
        total_books = 0
        self.books = []


    def add_books(self,book_name):
        self.books.append(book_name)
        Library.total_books +=1
















def get_age(self):
    return self.__age


def set__age(self, age):
    if age > 0:
        self.__age = age
    else:
        print("Age muss be positive")

        print = Person("Alice", 30)
        print(Person.name)
        print(Person.age)










