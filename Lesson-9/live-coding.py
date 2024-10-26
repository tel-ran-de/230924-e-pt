# Тема 1. Продемонстрируйте и объясните в режиме live-coding:
# - создание списка,

print('Тема 1')
fruits = ['apple', 'banana', 'peach']
print(fruits)

# - доступ к элементам списка,
print(fruits[0])  # apple
print(fruits[2])  # peach

# - изменение значения элемента списка,
fruits[1] = 'orange'
print(fruits)

# - получение среза,
print(fruits[1:3])

# - создание и работу с вложенными списками.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1])
print(matrix[1][1])

# сравнение списков
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)


# жизненные примеры
users = [
    ['user1', 'password', 'email1@example.com'],
    ['user2', 'password', 'email2@example.com'],
    ['user3', 'password', 'email3@example.com'],
]


# Тема 2. Продемонстрируйте и объясните в режиме live-coding:
# - Использование различных методов списков.
print('Тема 2')
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

numbers.extend([5, 6])
print(numbers)

numbers.insert(1, 1.5)
print(numbers)

numbers.remove(1.5)
print(numbers)

# .pop(<индекс>)
popped_number = numbers.pop(3)  # по умолчанию удаляет последний элемент
print(popped_number)
print(numbers)

numbers.clear()
print(numbers)

numbers = [1, 2, 3, 2, 2]
index_of_2 = numbers.index(2)
print(index_of_2)

count_of_2 = numbers.count(2)
print(count_of_2)

numbers.sort()
print(numbers)

numbers.reverse()


# - Изменяемость списков и неизменяемость строк

# string = 'hello'
# string[0] = 1  # TypeError: 'str' object does not support item assignment

string = 'hello'
print(id(string))
print(string)
string = string.replace('e', 'a')
print(id(string))
print(string)

movies = [["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
print(*movies, sep='\n')
print(movies, sep='\n')

