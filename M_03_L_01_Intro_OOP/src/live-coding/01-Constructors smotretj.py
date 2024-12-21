# Задание 1: Работа с методами __init__ и __del__.
# Создайте класс Book, который будет иметь атрибуты title, author и year.
# Реализуйте методы __init__ и __del__ для инициализации объектов и
# вывода сообщения при удалении объекта соответственно.
#
# Метод __init__ должен инициализировать атрибуты title, author и year.
# Метод __del__ должен выводить сообщение, содержащее название книги и автора, когда объект удаляется.
#
#



# Задание 2: Вызов конструктора базового класса.
#
# Создайте базовый класс Animal, который будет иметь атрибуты name и age.
# Затем создайте производный класс Dog, который будет наследовать от Animal и добавит атрибут breed.
# Реализуйте вызов конструктора базового класса внутри конструктора производного класса.
#
# Класс Animal должен иметь метод __init__, инициализирующий атрибуты name и age.
# Класс Dog должен наследовать от Animal и иметь свой метод __init__, который вызывает конструктор базового класса
# и инициализирует атрибут breed.




class Book:
    pass


class Animal:
    pass


class Dog(Animal):
    pass


def main():
    # Создание объекта
    book1 = Book("1984", "George Orwell", 1949)

    # Удаление объекта
    del book1

    # Создание объекта
    dog1 = Dog("Buddy", 3, "Golden Retriever")


if __name__ == "__main__":
    main()

# Book '1984' by George Orwell created.
# Book '1984' by George Orwell is being deleted.
# Animal 'Buddy' created, age: 3.
# Dog 'Buddy' of breed 'Golden Retriever' created.