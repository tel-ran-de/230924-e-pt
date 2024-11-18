# Тема: Вложенные циклы


# Упражнение 1: Проверка простых чисел в диапазоне
#
# Напишите программу, которая выводит все простые числа в диапазоне от 2 до 50.
# Используйте вложенный цикл for для перебора чисел в указанном диапазоне.
# Внутри вложенного цикла while используйте для проверки, является ли число простым.
# Число является простым, если оно делится только на 1 и на само себя.
# Для каждого числа в диапазоне от 2 до 50, проверьте, делится ли оно на любое число меньше него (кроме 1).

numbers = list(range(2,51))
simple = []
for num in numbers:
    for divider in numbers:
        result = True
        if num > divider:
            if num%divider==0:
                print(num, divider)
                result = False
                break
    if result:
        simple.append(num)
print(simple)

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

numbers = list(range(1,11))
print(numbers)
print(' '*4, end='')
for num in numbers:
    print(f'{num:4}', end='')
print()
print('-'*44)
for num1 in numbers:
    print(f'{num1:3}|', end='')
    for num2 in numbers:
        print(f'{num1*num2:4}', end='')
    print()
'''

numbers = list(range(1,11))
print(numbers)
print(' '*4, end='')
for num in numbers:
    print(f'{num:4}', end='')
print()
print('-'*44)
for num1 in numbers:
    print(f'{num1:3}|', end='')
    for num2 in numbers:
        print(f'{num1*num2:4}', end='')
    print()
'''
# Тема: Генераторы списков

# Упражнение 1: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.

list_7 = [x for x in range(7,1001, 7)]
print(list_7)



# Упражнение 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.
list_3 = [x for x in range(1,1001) if str(x).find('3') >= 0]
print(list_3)

# Упражнение 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке
some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
result = sum(1 for char in some_string if char==' ')
print(result)

# Упражнение 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
some_string = 'the quick brown fox jumps over the lazy dog'
vowel_list = [x for x in some_string if x in 'eiuoa']
print(vowel_list)

=======
list_7 = [x for x in range(7,1001, 7)]
print(list_7)


# Упражнение 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.
list_3 = [x for x in range(1,1001) if str(x).find('3') >= 0]
print(list_3)

# Упражнение 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке
some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
result = sum(1 for char in some_string if char==' ')
print(result)

# Упражнение 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
some_string = 'the quick brown fox jumps over the lazy dog'
vowel_list = [x for x in some_string if x in 'eiuoa']
print(vowel_list)


# Упражнение 5: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу 3x3 из чисел от 20 до 28
# Ожидаемая матрица:
# [20, 21, 22]
# [23, 24, 25]
# [26, 27, 28]


matrix = [[x + 19  for x in range(1 + 3 * i, 1 + 3 * (i + 1))] for i in range(3)]
for row in matrix:
    print(row)
    print(sum(row))
# Напишите код для вычисления суммы элементов в каждом ряду (в каждом вложенном списке).

# Выведите получившиеся значения в консоль.


# Упражнение 6: Подсчет количества четных и нечетных чисел в матрице
# Дана матрица

matrix = [
     [2, 5, 8, 11],
     [14, 17, 20, 23],
     [26, 29, 32, 35],
     [38, 41, 44, 47]
 ]


# Напишите программу для подсчета четных и нечетных чисел в каждом вложенном списке (строке матрицы).

even_odd = [[sum(1 for el in row if el % 2 == 0), sum(1 for el in row if el % 2 == 1)] for row in matrix]
for row in even_odd:
    print(f"Количество четных чисел: {row[0]}")
    print(f"Количество нечетных чисел: {row[1]}")

# Упражнение 7: Поиск минимального и максимального значения в матрице
# Дана матрица
matrix = [
     [34, 23, 18],
     [14, 55, 27],
     [19, 42, 31]
 ]

even_odd = [[sum(1 for el in row if el % 2 == 0), sum(1 for el in row if el % 2 == 1)] for row in matrix]
for row in even_odd:
    print(f"Количество четных чисел: {row[0]}")
    print(f"Количество нечетных чисел: {row[1]}")

# Упражнение 7: Поиск минимального и максимального значения в матрице
# Дана матрица
matrix = [
     [34, 23, 18],
     [14, 55, 27],
     [19, 42, 31]
 ]

# Напишите программу для вывода минимального и максимального значений в каждом ряду (вложенном списке) матрицы.
min_max = [[min(row), max(row)] for row in matrix]
print(min_max)

# Упражнение 8: Перемножение матриц
#
# - Создайте с помощью генераторов списков две матрицы размером 3x3 со значениями от 1 до 9 и от 9 до 1.

matrix1 = [[x for x in range(1 + j*3, 1 + 3*(j+1))] for j in range(3)]
print(f'matrix1 = {matrix1}')
matrix2 = [[x for x in range(3*j, (j-1)*3, -1) ] for j in range(3, 0,-1)]
print(f'matrix2 = {matrix2}')

#     matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#
# - Используйте генераторы списков для вычисления произведения этих матриц.
#     product = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]


product = [[sum([matrix1[k][i] * matrix2[i][j] for i in range(3)]) for j in range(3)] for k in range(3)]
for row in matrix1:
    print(row)
print()
for row in matrix2:
    print(row)
for row in product:
    print(row)
print(product)
#
# - Выведите исходные матрицы и результат их произведения.

product = [[sum([matrix1[k][i] * matrix2[i][j] for i in range(3)]) for j in range(3)] for k in range(3)]
for row in matrix1:
    print(row)
print()
for row in matrix2:
    print(row)
for row in product:
    print(row)
print(product)
#

# - Выведите исходные матрицы и результат их произведения.'''

