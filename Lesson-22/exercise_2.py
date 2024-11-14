# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def numb_gen():
    for i in range(1, 21):
        yield i

print(list(filter(lambda x: x % 2 == 0, numb_gen())))


# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
numbers = (i for i in range(1, 6))
squer_numbers = (i * i for i in range(1, 6))
list_iter = list(zip(numbers, squer_numbers))
print(list(map(lambda x: f"{x[0]}: {x[1]}", list_iter)))


# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

filter_lines = filter(lambda line: "Python" in line, file_reader("text_files/example.txt"))
upper_lines = map(lambda line: line.upper(), filter_lines)
for line in upper_lines:
    print(line)


