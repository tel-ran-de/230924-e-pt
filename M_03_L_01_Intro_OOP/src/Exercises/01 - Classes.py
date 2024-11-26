# Ex 1
# Создайте базовый класс `Person` с атрибутами `name` и `age`.
# Затем создайте два производных класса `Student` и `Teacher`.
# Класс `Student` должен иметь дополнительный атрибут `student_id`, а класс `Teacher` — атрибут `subject`.
# Реализуйте методы для вывода информации о каждом объекте.





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print (f"Name:{self.name}, Age:{self.age}")



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        print(f'Class Student __init__(student_id={self.student_id})')



class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        print(f'Class Teacher __init__(subject={self.subject})')



def main():
    person = Student("Maxim", 43, 11)
    student = Student("Maxim", 43, 12)
    teacher = Teacher("Maxim", 43, "математика")
if __name__ == '__main__':
    main()




# Ex 2
# Создайте класс `Vehicle` с атрибутами `make` и `model`.
# Создайте производный класс `Car` с дополнительным атрибутом `num_doors` (количество дверей) и
# производный класс `Motorcycle` с атрибутом `has_sidecar` (имеет ли мотоцикл коляску).
# Реализуйте метод, который выводит полное описание транспортного средства.






class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model),  "родительского класса"
        self.num_doors = num_doors,     "количество дверей"

    def describe(self):
        return f"{self.make} {self.model} с {self.num_doors} дверями"
        "описание машины, количество дверей"

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar,    "наличие коляски"

    def describe(self):

        sidecar_status = "с коляской" if self.has_sidecar else "без коляски"
        return f"{self.make} {self.model} {sidecar_status}"

"Пример "

vehicle1 = Vehicle("Toyota", "Corolla")
car1 = Car("Honda", "Civic", 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", True)

print(vehicle1.describe())  # Toyota Corolla
print(car1.describe())      # Honda Civic с 4 дверями
print(motorcycle1.describe())  # Harley-Davidson Sportster с коляской
