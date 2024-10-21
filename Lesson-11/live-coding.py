# Тема: Вложенные циклы: for вложенный в for, for вложенный в while.
# # Покажите и объясните использования вложенных циклов в формате live-coding.
# cities = ['Tashkent', 'Tbilisi', 'Warsaw']
# for city in cities:
#     for char in city:
#         print(char)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# for row in matrix:
#     for element in row:
#         print(element)

numbers = list(range(1, 6))
i = 0

while i < len(numbers):
    for j in range(numbers[i]):
        print(j, end=' ')
    print()
    i += 1






# Тема: Генераторы списков (List comprehension). Вложенные циклы и вложенные генераторы списков.
# Продемонстрируйте и объясните использование генераторов списков.
# В том числе использование вложенных генераторов списков.
print('Генераторы списков (List comprehension)')
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
# squares = []
# for i in numbers:
#     squares.append(i ** 2)
squares = [i ** 2 for i in numbers]
print(squares)

print('Использование генератора списков для обработки строк')
text = 'Hello, world! Have A good day!'
vowels = [char for char in text if char.lower() in 'aeiou']
print(vowels)
words = [word for word in text.split() if word.istitle()]
print(words)

print('Использование генератора для обработки матриц')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
flattened = [element for row in matrix for element in row]
print(flattened)

print('Вложенные генераторы списков')
n = 10
matrix =[[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
print(matrix)

print('Вложенные генераторы для обработки матриц')
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
normalized = [[element / 10 for element in row] for row in matrix]
print(normalized)





# Тема: Итератор и итерируемые объекты. Функции iter и next. Сравнение iter и next с циклом for и функцией range.
# Продемонстрируйте создание итератора и использование функций iter и next.
