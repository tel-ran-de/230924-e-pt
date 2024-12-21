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

squared_numbers = list(map(square, numbers))


print(squared_numbers)




# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: [2, 4, 6, 8, 10]




def is_even(digit):
    return digit % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)





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

result = list(zip(names, ages))

print(result)





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
print (list(str_numbers))




# Задача 5: Применение функции filter для отбора слов длиннее 4 символов
# Напишите функцию `longer_than_four`, которая принимает строку и возвращает `True`,
# если длина строки больше 4 символов, и `False` в противном случае. Используйте функцию `filter`,
# чтобы отобрать слова длиной больше 4 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
#
# words = ["apple", "kiwi", "banana", "pear"]
# Ожидаемый результат: ["apple", "banana"]





def longer_than_four(word):
    return len(word) > 4

words = ["apple", "kiwi", "banana", "pear"]

long_words = filter(longer_than_four, words)

print(list(long_words))






# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




numbers = (x for x in range(1, 21))

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))





# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']





numbers = iter(range(1, 6))

squares = iter(x ** 2 for x in range(1, 6))
result = map(lambda x: f"{x[0]}: {x[1]}", zip(numbers, squares))

print(list(result))





# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.






def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


lines = read_lines('example.txt')
filtered_lines = filter(lambda line: 'Python' in line, lines)
uppercase_lines = map(lambda line: line.upper(), filtered_lines), ("map верхний регистр")

for line in uppercase_lines:
    print(line)





# Тема: Дополнительная практика

# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]




def celsius_generator():
    for celsius in range(-10, 11):
        yield celsius

celsius_values = celsius_generator()
fahrenheit_values = map(lambda c: (9/5) * c + 32, celsius_values)

print(list(fahrenheit_values))






# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']




words = ["hello", "world", "python", "is", "awesome"]

long_words = filter(lambda word: len(word) > 5, words)
print(list(long_words))





# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']






def number_generator():
    for i in range(1, 4):
        yield i

"для кубов"
def cube_generator():
    for i in range(1, 4):
        yield i ** 3
"с zip"
result = list(map(lambda x: f"{x[0]}: {x[1]}", zip(number_generator(), cube_generator())))

print(result)






# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.





def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()



lines = read_lines('data.txt')

lines_with_numbers = filter(lambda line: any(char.isdigit() for char in line), lines)
numbers = map(lambda line: int(''.join(filter(str.isdigit, line))), lines_with_numbers)

print(list(numbers))





# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".






def read_file1(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def read_file2(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


file1_lines = read_file1('file1.txt')
file2_lines = read_file2('file2.txt')

zipped_lines = zip(file1_lines, file2_lines)


"map с лямбда"
formatted_lines = map(lambda x: f"{x[0]} - {x[1]}", zipped_lines)

for line in formatted_lines:
    print(line)



#############################################################################################################


