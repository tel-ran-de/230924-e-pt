```python
# Упражнение 1: Проверка простых чисел в диапазоне

print("Простые числа в диапазоне от 2 до 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Упражнение 2: Таблица умножения

print("\nТаблица умножения 10x10:")
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n---------------------------------------------")

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

# Упражнение 1: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.

numbers_divisible_by_7 = [num for num in range(1, 1001) if num % 7 == 0]
print("\nЧисла от 1 до 1000, которые делятся на 7:", numbers_divisible_by_7)

# Упражнение 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.

numbers_with_3 = [num for num in range(1, 1001) if '3' in str(num)]
print("\nЧисла от 1 до 1000, в которых есть цифра 3:", numbers_with_3)

# Упражнение 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'.

some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
space_count = sum(1 for char in some_string if char == ' ')
print("\nКоличество пробелов в строке:", space_count)

# Упражнение 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
# some_string = 'the quick brown fox jumps over the lazy dog'.

some_string = 'the quick brown fox jumps over the lazy dog'
vowels = [char for char in some_string if char.lower() in 'aeiou']
print("\nГласные буквы в строке:", vowels)

# Упражнение 5: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу 3x3 из чисел от 20 до 28

matrix = [[20 + i + j * 3 for i in range(3)] for j in range(3)]
print("\nМатрица 3x3 из чисел от 20 до 28:")
for row in matrix:
    print(row)

row_sums = [sum(row) for row in matrix]
print("\nСумма элементов в каждом ряду:", row_sums)

# Упражнение 6: Подсчет количества четных и нечетных чисел в матрице

matrix = [
    [2, 5, 8, 11],
    [14, 17, 20, 23],
    [26, 29, 32, 35],
    [38, 41, 44, 47]
]

even_counts = [sum(1 for num in row if num % 2 == 0) for row in matrix]
odd_counts = [sum(1 for num in row if num % 2 != 0) for row in matrix]

print("\nКоличество четных чисел в каждом ряду:", even_counts)
print("Количество нечетных чисел в каждом ряду:", odd_counts)

# Упражнение 7: Поиск минимального и максимального значения в матрице

matrix = [
    [34, 23, 18],
    [14, 55, 27],
    [19, 42, 31]
]

min_values = [min(row) for row in matrix]
max_values = [max(row) for row in matrix]

print("\nМинимальные значения в каждом ряду:", min_values)
print("Максимальные значения в каждом ряду:", max_values)

# Упражнение 8: Перемножение матриц

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

product = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

print("\nМатрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nПроизведение матриц:")
for row in product:
    print(row)
```

### Подробные комментарии по решению Упражнения 8 с перемножением матриц

1. **Создание матриц**:
    ```python
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    ```
    - Создаем две матрицы `matrix1` и `matrix2` размером 3x3.
    - `matrix1` содержит значения от 1 до 9.
    - `matrix2` содержит значения от 9 до 1.

2. **Вычисление произведения матриц**:
    ```python
    product = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    ```
    - Используем генераторы списков для создания результирующей матрицы `product`.
    - Внешний генератор списков `for i in range(3)` создает строки результирующей матрицы.
    - Внутренний генератор списков `for j in range(3)` создает элементы каждой строки результирующей матрицы.
    - Для каждого элемента результирующей матрицы вычисляем сумму произведений соответствующих элементов строк и столбцов исходных матриц.
    - Вложенный генератор списков `sum(matrix1[i][k] * matrix2[k][j] for k in range(3))` вычисляет сумму произведений элементов строки `i` матрицы `matrix1` и столбца `j` матрицы `matrix2`.

3. **Вывод исходных матриц и результата их произведения**:
    ```python
    print("\nМатрица 1:")
    for row in matrix1:
        print(row)

    print("\nМатрица 2:")
    for row in matrix2:
        print(row)

    print("\nПроизведение матриц:")
    for row in product:
        print(row)
    ```
    - Выводим исходные матрицы `matrix1` и `matrix2`.
    - Выводим результирующую матрицу `product`.

### Ожидаемый вывод программы

```
Матрица 1:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Матрица 2:
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]

Произведение матриц:
[30, 24, 18]
[84, 69, 54]
[138, 114, 90]
```

Этот код вычисляет произведение двух матриц размером 3x3 и выводит исходные матрицы и результат их произведения.