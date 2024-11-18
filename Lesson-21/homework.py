# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration




class NumberIterator:
    def __init__(self, n):
        self.n = n,  "Максимальное число"
        self.current = 1,  "число, начинается итерация"

    def __iter__(self):
        return self,  "Возвращаем  итератор"

    def __next__(self):
        if self.current > self.n:  # Если текущее число больше n, остановим итератор
            raise StopIteration
        current_value = self.current
        self.current += 1  # Переходим к следующему числу
        return current_value

# Функция для создания итератора
def create_number_iterator(n):
    return NumberIterator(n)

# Пример использования
n = 5,  "Максимальное число"
iterator = create_number_iterator(n)

for number in iterator:
    print(number),"Вывод"







# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration




#def square_generator():
#    for i in range(11):  # от 0 до 10 включительно
#        yield i ** 2  # возвращаем квадрат числа

#"использования генератора"
#gen = square_generator()

# Печать всех квадратов
#try:
#    while True:
#       print(next(gen))  # Получаем следующее значение из генератора
#except StopIteration:
#    print("Итерация завершена!")





# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration



"Функция-генератор"


def word_generator(sentence):
    words = sentence.split()  # Разделяем предложение на слова
    for word in words:
        yield word  # Возвращаем слово по одному

# Пример использования функции-генератора
sentence = "Python is an awesome programming language"

# Создаем генератор
generator = word_generator(sentence)

# Используем next() для извлечения слов и обработку исключения StopIteration
try:
    while True:
        word = next(generator)  # Получаем следующее слово
        print(word)
except StopIteration:
    print("Все слова")





# Тема: Генераторы и встроенные функции

# Задача 1: # Генератор, который возвращает квадраты чисел от 0 до 10
# def square_generator():
#     for i in range(11):  # от 0 до 10 включительно
#         yield i ** 2  # возвращаем квадрат числа
#
# # Пример использования генератора
# gen = square_generator()
#
# # Печать всех квадратов
# try:
#     while True:
#         print(next(gen))  # Получаем следующее значение из генератора
# except StopIteration:
#     print("Итерация завершена!")




#def generate_numbers():
#   for i in range(1, 11):
#       if i % 2 == 0:
#           yield i * 2,  "Если число четное, удваиваем его"
#       else:
#           yield i,  "число нечетное, возвращаем без изменений"


#result_set = set(generate_numbers())

#"Вывод"

#print(result_set)





# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.





def multiples_of_three():
    for i in range(1, 21):  # от 1 до 20 включительно
        if i % 3 == 0:  # проверяем, кратно ли число 3
            yield i  # если кратно 3, возвращаем это число

# Создаем генератор
gen = multiples_of_three()

# Используем функцию sum() для подсчета суммы чисел из генератора
total_sum = sum(gen)

# Выводим результат
print(f"Сумма чисел от 1 до 20, кратных 3: {total_sum}")


def multiples_of_three():
#   for num in range(1, 21):
        if num % 3 == 0:
            yield num


result_sum = sum(multiples_of_three())

"Вывод"
print(result_sum)





# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"





def word_lengths(sentence):
    words = sentence.split(),
    for word in words:
        yield len(word),  "Возвращаем длину слова"

"строка"

sentence = "Write a generator that returns word lengths from a given sentence"



min_length = min(word_lengths(sentence))
max_length = max(word_lengths(sentence))

# Выводим результаты
print(f"Минимальная длина слова: {min_length}")
print(f"Максимальная длина слова: {max_length}")







# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

x_word = 'this'





def keyword_filter(filename, x_word):


#   with open(filename, 'r') as file:

#       for line in file:
            "Приводим строку и ключевое слово к нижнему регистру для нечувствительности к регистрy"

            if x_word.lower() in line.lower():
                yield line.strip()  # Возвращаем строку без символов новой строки

"Пример использования генератора"
filename = 'data.txt'
keyword = 'Python'

# Используем генератор для получения строк, содержащих ключевое слово
for line in keyword_filter(filename, keyword):
    print(line)





# Задача 2:Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"






# Генератор, который возвращает длины слов из строки

def word_lengths(sentence):
    words = sentence.split()  # Разделяем строку на слова
    for word in words:
        yield len(word)  # Возвращаем длину каждого слова

# Заданная строка
sentence = "Write a generator that returns word lengths from a given sentence"

# Создаем генератор
gen = word_lengths(sentence)

# Используем функции min() и max() для нахождения минимальной и максимальной длины слов
min_length = min(gen)  # Минимальная длина
gen = word_lengths(sentence)  # Перезапускаем генератор, так как он исчерпан после первого использования
max_length = max(gen)  # Максимальная длина

# Выводим результаты
print(f"Минимальная длина слова: {min_length}")
print(f"Максимальная длина слова: {max_length







# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt


import re


def lines_with_numbers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Используем регулярное выражение для поиска чисел
            if re.search(r'\d', line):
                yield line.strip()  # Возвращаем строку, убрав лишние пробелы

# Пример использования генератора
file_path = 'data.txt'  # Путь к вашему файлу

# Используем генератор для вывода строк, содержащих числа
for line in lines_with_numbers(file_path):
    print(line)




##########################################################################################