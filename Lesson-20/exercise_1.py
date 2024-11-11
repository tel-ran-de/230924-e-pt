# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
def division_num(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
    except TypeError:
        print("Вводите только числовые значения")
    else:
        return z
print(division_num(4, 0))
print(division_num(8, 4))
print(division_num(8, "a"))

# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.
def quetz_num():
    while True:
        try:
            user_num = int(input("Введите число: "))
            result = user_num ** 2
        except ValueError:
            print("Некорректный ввод.")
        else:
            return result
print(quetz_num())

# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
def kind_errors():
    try:
        file = open("examples.py", "r", encoding="utf-8")
        content = file.readline()
        print(content)
        file1 = open("C:/Windows/System32/example.txt", "w", encoding="utf-8")
        file1.write("Привет от Виктора!")
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Ошибка: нет доступа к файлу")
    except IOError:
        print("Ошибка ввода-вывода")
    else:
        print('Файл обработан. Файл закрыт.')
        file.close()
    finally:
        print('Операция завершена')
kind_errors()
