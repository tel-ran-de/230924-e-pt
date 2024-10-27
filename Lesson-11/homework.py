# exercises.py

# Упражнение 1: Проверка простых чисел в диапазоне
# Напишите программу, которая выводит все простые числа в диапазоне от 2 до 50.
# Используйте вложенный цикл for для перебора чисел в указанном диапазоне.
# Внутри вложенного цикла while используйте для проверки, является ли число простым.
# Число является простым, если оно делится только на 1 и на само себя.
# Для каждого числа в диапазоне от 2 до 50, проверьте, делится ли оно на любое число меньше него (кроме 1).

for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Упражнение 2: Таблица умножения
# Создайте программу, которая выводит таблицу умножения размером 10x10.
# Используйте вложенные циклы for для создания строк и столбцов таблицы.
# Форматируйте вывод так, чтобы таблица выглядела аккуратно.

print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n" + "-" * 45)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

# Упражнение 3: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.

print([number for number in range(1, 1001) if number % 7 == 0])

# Упражнение 4: Напишите программу с помощью генераторов списков,
# которая найдёт все числа от 1 до 1000, в которых есть цифра 3.

print([number for number in range(1, 1001) if '3' in str(number)])

# Упражнение 5: Напишите программу с помощью генераторов списков,
# которая посчитает количество пробелов в строке
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'.

some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
print(len([char for char in some_string if char == ' ']))

# Упражнение 6: Напишите программу с помощью генераторов списков,
# которая создаст список всех гласных букв в строке
# some_string = 'the quick brown fox jumps over the lazy dog'.

some_string = 'the quick brown fox jumps over the lazy dog'
print([char for char in some_string if char in 'aeiou'])

# Упражнение 7: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу 3x3 из чисел от 20 до 28
# Ожидаемая матрица:
# [20, 21, 22]
# [23, 24, 25]
# [26, 27, 28]

matrix = [[20 + i + j * 3 for i in range(3)] for j in range(3)]
row_sums = [sum(row) for row in matrix]
for row in matrix:
    print(row)
print("Суммы элементов в каждом ряду:", row_sums)

# Упражнение 8: Подсчет количества четных и нечетных чисел в матрице
# Дана матрица
# matrix = [
#     [2, 5, 8, 11],
#     [14, 17, 20, 23],
#     [26, 29, 32, 35],
#     [38, 41, 44, 47]
# ]

matrix = [
    [2, 5, 8, 11],
    [14, 17, 20, 23],
    [26, 29, 32, 35],
    [38, 41, 44, 47]
]

for row in matrix:
    even_count = len([num for num in row if num % 2 == 0])
    odd_count = len([num for num in row if num % 2 != 0])
    print(f"Строка: {row}")
    print(f"Количество четных чисел: {even_count}")
    print(f"Количество нечетных чисел: {odd_count}")

# Упражнение 9: Поиск минимального и максимального значения в матрице
# Дана матрица
# matrix = [
#     [34, 23, 18],
#     [14, 55, 27],
#     [19, 42, 31]
# ]

matrix = [
    [34, 23, 18],
    [14, 55, 27],
    [19, 42, 31]
]

for row in matrix:
    min_value = min(row)
    max_value = max(row)
    print(f"Строка: {row}")
    print(f"Минимальное значение: {min_value}")
    print(f"Максимальное значение: {max_value}")

# Упражнение 10: Перемножение матриц
# Создайте с помощью генераторов списков две матрицы размером 3x3 со значениями от 1 до 9 и от 9 до 1.
# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrix1 = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
matrix2 = [[9 - (i + j * 3) for i in range(3)] for j in range(3)]

product = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

for row in matrix1:
    print(row)

print()

for row in matrix2:
    print(row)

print()

for row in product:
    print(row)
