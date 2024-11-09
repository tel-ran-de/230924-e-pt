def multiply(a, b):
    return a * b
def subtract(a, b):
    return a - b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль!"

if __name__ == "__main__":
    print("Модуль запущен напрямую")
print(multiply(8, 3))
print(divide(8, 2))
print(subtract(8, 2))