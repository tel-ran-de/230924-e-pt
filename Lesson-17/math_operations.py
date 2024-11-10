def multiply(a, b):
    """Returns the product of two numbers a and b."""
    return a * b

def subtract(a, b):
    """Returns the difference between two numbers a and b."""
    return a - b

def divide(a, b):
    """Returns the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Модуль запущен напрямую")