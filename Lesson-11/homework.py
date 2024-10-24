# Тема: Вложенные циклы

# Упражнение 1: Проверка простых чисел в диапазоне
#
# Напишите программу, которая выводит все простые числа в диапазоне от 2 до 50.
# Используйте вложенный цикл for для перебора чисел в указанном диапазоне.
# Внутри вложенного цикла while используйте для проверки, является ли число простым.
# Число является простым, если оно делится только на 1 и на само себя.
# Для каждого числа в диапазоне от 2 до 50, проверьте, делится ли оно на любое число меньше него (кроме 1).

numbers = list(range(2, 51))
for numb in numbers:
    while numb % numb == 0 and numb % 1 == 0:
        print(numb)
        break

for numb in numbers:
    for div in range(2, numb):
        if numb % div == 0:
            print(numb)
            break


# Упражнение 2: Таблица умножения

# - Создайте программу, которая выводит таблицу умножения размером 10x10.
# - Используйте вложенные циклы `for` для создания строк и столбцов таблицы.
# - Форматируйте вывод так, чтобы таблица выглядела аккуратно.

# Ожидаемый вывод программы:

#      1   2   3   4   5   6   7   8   9  10
# ---------------------------------------------
#  1 |   1   2   3   4   5   6   7   8   9  10
#  2 |   2   4   6   8  10  12  14  16  18  20
#  3 |   3   6   9  12  15  18  21  24  27  30
#  4 |   4   8  12  16  20  24  28  32  36  40
#  5 |   5  10  15  20  25  30  35  40  45  50
#  6 |   6  12  18  24  30  36  42  48  54  60
#  7 |   7  14  21  28  35  42  49  56  63  70
#  8 |   8  16  24  32  40  48  56  64  72  80
#  9 |   9  18  27  36  45  54  63  72  81  90
# 10 |  10  20  30  40  50  60  70  80  90 100

print('    ', end='')
for i in range(1, 11):
    print(f'{i:4}', end='')
print('\n---------------------------------------------')

for i in range(1, 11):
    print(f'{i:2} |', end='')
    for j in range(1, 11):
        print(f'{i * j:4}', end='')
    print()

# Тема: Генераторы списков

# Упражнение 1: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.

numbers = list(range(1, 1001))
kratnoe_7 = [numb for numb in numbers if numb % 7 == 0]
print(kratnoe_7)

# Упражнение 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.

numbers = list(range(1, 1001))
soderjat_3 = [numb for numb in numbers if "3" in str(numb)]
print(soderjat_3)

# Упражнение 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'.

some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
probel = [spase for spase in some_string if spase in " "]
print(len(probel))

# Упражнение 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
# some_string = 'the quick brown fox jumps over the lazy dog'.

some_string = 'the quick brown fox jumps over the lazy dog'
vowels = [char for char in some_string if char in 'aeiou']
print(len(vowels))

# Упражнение 5: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу 3x3 из чисел от 20 до 28
# Ожидаемая матрица:
# [20, 21, 22]
# [23, 24, 25]
# [26, 27, 28]

matrix = [[numb for numb in range(row * 3 + 20, row *3 + 23)] for row in range(3)]
for row in matrix:
    print(row)

# Напишите код для вычисления суммы элементов в каждом ряду (в каждом вложенном списке).
# Выведите получившиеся значения в консоль.


# Упражнение 6: Подсчет количества четных и нечетных чисел в матрице
# Дана матрица
# matrix = [
#     [2, 5, 8, 11],
#     [14, 17, 20, 23],
#     [26, 29, 32, 35],
#     [38, 41, 44, 47]
# ]
#
# Напишите программу для посчета четных и нечетных чисел в каждом вложенном списке (строке матрицы).
# Выведите значения в констоль:
# print(f"Количество четных чисел: ")
# print(f"Количество нечетных чисел: ")


# Упражнение 7: Поиск минимального и максимального значения в матрице
# Дана матрица
# matrix = [
#     [34, 23, 18],
#     [14, 55, 27],
#     [19, 42, 31]
# ]

# Напишите программу для вывода минимального и максимального значений в каждом ряду (вложенном списке) матрицы.


# Упражнение 8: Перемножение матриц
#
# - Создайте с помощью генераторов списков две матрицы размером 3x3 со значениями от 1 до 9 и от 9 до 1.
#     matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#
# - Используйте генераторы списков для вычисления произведения этих матриц.
#     product = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
#
# - Выведите исходные матрицы и результат их произведения.