# FIXED

# Цикл while. Операторы break, continue, else.

# while
# i = 0  # i, j, k - нормальные абстрактные названия для переменных
# while i < 5:
#     print(i)
#     i += 1
# Вывод 0 1 2 3 4

# password = ''
# while password != 'secret':
#     password = input('Введите пароль: ')
# print('Пароль верный')

# break c while
# i = 0
# while True:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# continue c while
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# else с while
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print('Цикл завершён')
#
# word = ''
# while word != 'soft_stop':
#     word = input('Введите слово: ')
#     if word == 'STOP':
#         print('цикл остановлен с помощью break, else не будет выполнен')
#         break
# else:
#     print('Цикл был выполнен полностью и был запущен оператор else')


# Тема: Цикл for

# Продемонстрируйте создание и использование цикла for.
# Показать использование функций range, enumerate.

# for
# cities = ['Tbilisi', 'Berlin', 'Kogon', 'Beijin', 'London']
# for city in cities:
#     print(city)
# print('Tbilisi')
# ...
# print('London')

# range
# print(list(range(5)))  # арифметическая прогрессия от 0 до 4
# print(list(range(10, 21)))
# print(list(range(10, 100, 10)))

# for и range
# for i in range(10, 100, 10):
#     print(i)

# enumerate - первый аргумент коллекция, второй аргумент с какого числа начать отсчёт
# countries = ['Germany', 'Italy', 'Brazil', 'Georgia', 'Italy']
# for index, country in enumerate(countries, 1):
#     print(f'{index}. {country}')

# word = 'television noromende'
# for letter in word:
#     print(letter)

# fruits = ['banana', 'orange', 'apple', 'peach', 'pear']
# for fruit in fruits:
#     for letter in fruit:
#         print(letter, end=' ')
#     print()
