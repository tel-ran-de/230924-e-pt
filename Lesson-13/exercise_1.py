# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
<<<<<<< HEAD
# Вывод функции: (21, 3.5, 3)
# numbers = [1, 2, 3, 4, 5, 6]
#
# def analyze_numbers(numbers):
#     summa_numbers = sum(numbers)
#     average = summa_numbers / len(numbers)
#     s1 = sum(1 for num in numbers if num % 2 == 0)
#     return summa_numbers, average, s1
# print(analyze_numbers(numbers))


# def revers_string(text):
#     return text[::-1]
# print(revers_string('I go to the theatre'))

=======
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)


>>>>>>> abb1210aa612fd57ba605d8fec7f203be4ab3ead
# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
<<<<<<< HEAD
def analyze_strings(strings):
    long_str = 0
    short_str = 999
    a_str = 0
    # longest = max(strings, key=len)
    for l in strings:
        if len(l) > long_str:
            long_str = len(l)
        if len(l) < short_str:
            short_str = len(l)
        if 'a' in l:
            a_str += 1
    return(long_str, short_str,a_str)

strings = ["apple", "banana", "cherry", "date"]


=======
# strings = ["apple", "banana", "cherry", "date"]
>>>>>>> abb1210aa612fd57ba605d8fec7f203be4ab3ead
# Вывод функции: ('banana', 'date', 3)


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
