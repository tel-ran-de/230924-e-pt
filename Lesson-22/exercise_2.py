# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]






# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']



iter_1 = [i for i in range(1, 6)]
iter_2 = [i**2 for i in iter_1 ]

iter_zip = zip(iter_1, iter_2)
print(list(iter_zip))

lambda_list = list(map(lambda pair: f"{pair[0]}: {pair[1]}", zip(iter_1, iter_2)))

print(lambda_list)





numbers = iter(range(1, 6)),                                        "от 1 до 5""Итератор чисел"
squares = iter(x ** 2 for x in range(1, 6)),                        "от 1 до 5""Итератор квадратов"
result = map(lambda x: f"{x[0]}: {x[1]}", zip(numbers, squares)),   "zip для чисел и квадратов"

print(list(result))









# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.




def process_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def filter_and_transform(filename):
    lines = process_file(filename)
    result = map(lambda line: line.upper(), filter(lambda line: 'Python' in line, lines))
    return result


filename = 'example.txt'
for line in filter_and_transform(filename):
    print(line)