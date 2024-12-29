# Ex 1
# Создайте класс `Temperature` с методами для преобразования температуры из градусов Цельсия в Фаренгейты и Кельвины.
# Реализуйте методы как статические.
from gc import get_count


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return {celsius * 9 / 5 + 32}

    @staticmethod
    def celsius_to_kelvin(celsius):
        return {celsius + 273.15}

celsius_temp = 12

fahrenheit_temp = Temperature.celsius_to_fahrenheit(celsius_temp)
kelvin_temp = Temperature.celsius_to_kelvin(celsius_temp)

print(f"{celsius_temp}°C  Фаренгейта: {fahrenheit_temp}°F")
print(f"{celsius_temp}°C  Кельвина: {kelvin_temp}K")





# #### Задание 2:
# Создайте класс `Counter` с атрибутом класса `count`,
# который будет отслеживать количество созданных экземпляров класса.
# Реализуйте метод класса `get_count`, который возвращает текущее значение `count`.







class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

print(Counter.get_count())
