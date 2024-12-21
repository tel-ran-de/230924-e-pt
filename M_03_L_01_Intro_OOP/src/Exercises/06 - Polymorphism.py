# Ex 1
# Создайте базовый класс `Appliance` с методом `turn_on`, который должен быть переопределен в
# производных классах `WashingMachine` и `Refrigerator`.
# В каждом из производных классов метод `turn_on` должен выводить сообщение о том, что прибор включен.
# Создайте список различных приборов и продемонстрируйте полиморфизм, вызвав метод `turn_on` для каждого прибора.





class Appliance:

    def turn_on(self):
        raise NotImplementedError("turn_on переопределен в подклассе")


class WashingMachine(Appliance):
    def turn_on(self):
        print("Стиральная машина включена.")


class Refrigerator(Appliance):
    def turn_on(self):
        print("Холодильник включен.")


def main():
    appliances = [WashingMachine(), Refrigerator()]

    for appliance in appliances:
        appliance.turn_on()


if __name__ == "__main__":
    main()






# #### Задание 2:
# Создайте базовый класс `Employee` с методом `calculate_pay`,
# который должен быть переопределен в производных классах `SalariedEmployee` и `HourlyEmployee`.
# В классе `SalariedEmployee` метод должен рассчитывать ежемесячную зарплату на основе фиксированного оклада,
# а в классе `HourlyEmployee` — на основе количества отработанных часов и почасовой ставки.
# Продемонстрируйте полиморфизм, вызвав метод `calculate_pay` для объектов различных классов.




class Employee:
    def calculate_pay(self):
        raise NotImplementedError("Error")


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
       return self.hourly_rate * self.hours_worked


def main():
    salaried_employee = SalariedEmployee("Анна", 2500),        #   "фиксированный оклад"
    hourly_employee = HourlyEmployee("Иван", 180, 20),   #  "почасовая ставка и часы"
    employees = [salaried_employee, hourly_employee]
    for employee in employees:
        print(f"on i ona{employee.name} заработал: {employee.calculate_pay()} евро.")


if __name__ == "__main__":
    main()


