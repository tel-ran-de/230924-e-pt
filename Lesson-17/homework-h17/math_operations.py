# 2. В этом файле определите три функции:
#     - `multiply(a, b)`: возвращает произведение двух чисел `a` и `b`.
#     - `subtract(a, b)`: возвращает разность между двумя числами `a` и `b`.
#     - `divide(a, b)`: возвращает результат деления числа `a` на `b`.
# 3. Включите конструкцию `if __name__ == "__main__"`, которая будет выполнять принт сообщения,
# если модуль запущен напрямую: “Модуль запущен напрямую”.

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    print('Модуль запущен напрямую')