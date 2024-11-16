# Тема: map, filter, zip

# Задача 1: Применение функции map для преобразования чисел
# Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5]
# Ожидаемый результат: [1, 4, 9, 16, 25]



def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]

sguared_numbers = list(map(sguare, numbers))

print(sguared_numbers)


# Функция для возведения числа в квадрат
def square(x):
    return x ** 2

# Список чисел
numbers = [1, 2, 3, 4, 5]

# Применяем функцию square ко всем элементам списка с помощью map
squared_numbers = list(map(square, numbers))

# Выводим результат
print(squared_numbers)



# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: [2, 4, 6, 8, 10]



def is_even(digit):
    return True if digit % 2 == 0 else False

numbers = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(is_even, numbers)))




# Задача 3: Применение функции zip для объединения списков
# У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# и выведите результат.
#
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

"Используем zip для объединения списков"
result = list(zip(names, ages))
"Выводим результат"
print(list(list_x))





# Задача 4: Применение функции map для преобразования строк в числа
# Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# и выведите результат.
#
# str_numbers = ["1", "2", "3", "4", "5"]
# Ожидаемый результат: [1, 2, 3, 4, 5]


def to_int(string):
    return int(string)

str_numbers = ["1", "2", "3", "4", "5"]
print (list(str_stirng))



# Задача 5: Применение функции filter для отбора слов длиннее 4 символов
# Напишите функцию `longer_than_four`, которая принимает строку и возвращает `True`,
# если длина строки больше 4 символов, и `False` в противном случае. Используйте функцию `filter`,
# чтобы отобрать слова длиной больше 4 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
#
# words = ["apple", "kiwi", "banana", "pear"]
# Ожидаемый результат: ["apple", "banana"]



def longer_than_four(word_3):
    return len(word_3) > 3

words = ["apple", "kiwi", "banana","pear"]
print(list(filter(longer_than_four)))