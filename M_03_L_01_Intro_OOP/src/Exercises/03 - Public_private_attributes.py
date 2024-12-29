# Ex 1
# Создайте класс `BankAccount` с публичным атрибутом `owner` и приватным атрибутом `__balance`.
# Реализуйте методы для внесения депозита и снятия денег, обеспечивая корректность операций
# (например, нельзя снять больше, чем есть на балансе).




class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Инициализация владельца счета и начального баланса
        self.owner = owner
        self.__balance = initial_balance  # Приватный атрибут для баланса


    def deposit(self, amount):
        """Метод для внесения депозита на счет"""
        if amount > 0:
            self.__balance += amount
            print(f"На счет {self.owner} внесено {amount} единиц. Текущий баланс: {self.__balance}.")
        else:
            print("Сумма депозита должна быть положительной.")


    def withdraw(self, amount):
        """Метод для снятия денег с счета"""
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
        elif amount > self.__balance:
            print("Недостаточно средств на счете.")
        else:
            self.__balance -= amount
            print(f"Со счета {self.owner} снято {amount} единиц. Текущий баланс: {self.__balance}.")


    def get_balance(self):
        """Метод для получения текущего баланса"""
        return self.__balance

account = BankAccount("Иван", 1000)  # Создаем счет с начальным балансом 1000
print(f"Начальный баланс: {account.get_balance()}")

account.deposit(500)  # Вносим депозит 500
account.withdraw(200)  # Снимаем 200
account.withdraw(1500)  # Пытаемся снять больше, чем есть на счете
account.withdraw(-100)  # Пытаемся снять отрицательную сумму



#
# Ex 2
# Создайте класс `Product` с публичным атрибутом `name` и приватным атрибутом `__price`.
# Реализуйте методы для получения и изменения цены,
# добавив проверки на корректность (цена не может быть отрицательной).





class Product:
    def __init__(self, name, price):
        """Инициализация продукта с названием и ценой"""
        self.name = name
        self.__price = price  # Приватный атрибут для цены
        if self.__price < 0:
            raise ValueError("Цена не может быть отрицательной.")

    def get_price(self):
        """Метод для получения текущей цены продукта"""
        return self.__price

    def set_price(self, price):
        """Метод для изменения цены продукта"""
        if price < 0:
            print("Ошибка: цена не может быть отрицательной.")
        else:
            self.__price = price
            print(f"Цена продукта '{self.name}' была изменена на {self.__price}.")


product = Product("Ноутбук", 1500)  # Создаем продукт с ценой 1500
print(f"Цена продукта '{product.name}': {product.get_price()}")

product.set_price(1800)  # Меняем цену на 1800
product.set_price(-500)  # Пытаемся установить отрицательную цену
print(f"Обновленная цена продукта '{product.name}': {product.get_price()}")