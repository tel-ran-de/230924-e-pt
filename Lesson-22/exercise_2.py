# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями
# from django.db.models.expressions import result
from tkinter.font import names

from django.template.defaultfilters import upper

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numbers = filter(lambda x: x % 2 == 0, (x for x in range(1,21)))
print(list(numbers))
# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']

numbers = iter(range(1,6))
squared_numbers = iter(i ** 2 for i in range(1,6))
zip_number = zip(numbers, squared_numbers)

format_number = list(map(lambda i: f"{i[0]}: {i[1]}", zip_number))
print(format_number)

# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.

def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
file_path = "text_files/example.txt"
lines = file_reader(file_path)
filtered_lines = filter(lambda line: 'Python' in line, lines)
upper_lines = map(lambda line: line.upper(), filtered_lines)
print(list(upper_lines))