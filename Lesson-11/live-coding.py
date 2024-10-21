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









# Тема: Итератор и итерируемые объекты. Функции iter и next. Сравнение iter и next с циклом for и функцией range.
# Продемонстрируйте создание итератора и использование функций iter и next.
