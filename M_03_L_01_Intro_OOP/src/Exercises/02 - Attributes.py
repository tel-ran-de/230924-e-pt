# Ex 1
# Создайте класс `Library`, у которого будет атрибут класса `total_books` и
# атрибут объекта `books` (список книг в данной библиотеке).
# Реализуйте методы для добавления книги в библиотеку и вывода общего количества книг во всех библиотеках.



class Library:
    total_books = 0

    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        Library.total_books += 1
        print(f"Книга '{book_name}' добавлена в библиотеку.")

    @classmethod
    def get_total_books(cls):
        return cls.total_books


library1 = Library()
library2 = Library()

library1.add_book("1989")
library1.add_book("Termintor 1")

library2.add_book("Termintor 2")

print(Library.get_total_books()),     "количество книг - всех библиотеках:"
print(library1.books),                "Книги в первой библиотеке:"
print(library2.books),                "Книги во второй библиотеке:"






# Ex 2
# Создайте класс `Company` с атрибутом класса `company_name` и
# атрибутом объекта `employees` (список сотрудников).
# Реализуйте методы для добавления сотрудника и вывода списка всех сотрудников данной компании.





class Company:
 company_name = "Killer Company"

 def __init__(self):
     self.company_name = Company
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



company= Company()
company.company_name1 = "Killer"
company.company_name2 = "Bob" , "Jana"


employee1 = Employee("Bob", "Soldat", 5000)
employee2 = Employee("Jana", "Soldat",3000)

company.add_employee1 = "Bob","Soldat - Sniper" , 5000
company.add_employee2 = "Jana","Soldatin - Hilfe" , 3000

print(f"Company name :{company.company_name1},{company.company_name2}")
print("Employees:",company.add_employee1 )
print("Employees:", company.add_employee2 )