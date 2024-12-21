# Ex 1
# Создайте класс `Employee` с приватными атрибутами `__name` и `__salary`.
# Реализуйте геттеры и сеттеры для этих атрибутов, добавив проверку,
# что зарплата не может быть ниже минимальной зарплаты (например, 10000).

# Ex 2
# Создайте класс `Circle` с приватным атрибутом `__radius`.
# Реализуйте свойства (property) для получения и установки значения радиуса,
# а также метод для вычисления площади круга.




import math

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius


    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius dolschen bitj positiwnim.")
        self.__radius = value

    "площади круга"

    def area(self):
        return math.pi * (self.__radius ** 2)


circle = Circle(5)
print("Radius:", circle.radius)

"нового радиуса"

circle.radius = 10


print("New radius:", circle.radius)
print("Area of circle:", circle.area())

"значение радиуса (отрицательное)"
try:
    circle.radius = -3
except ValueError as e:
    print(e)
