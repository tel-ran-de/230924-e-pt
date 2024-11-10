import math_operations

# Используем функции из модуля math_operations
a = 10
b = 5

# Умножение
product = math_operations.multiply(a, b)
print(f"Произведение {a} и {b}: {product}")

# Вычитание
difference = math_operations.subtract(a, b)
print(f"Разность {a} и {b}: {difference}")

# Деление
try:
    quotient = math_operations.divide(a, b)
    print(f"Результат деления {a} на {b}: {quotient}")
except ValueError as e:
    print(e)
