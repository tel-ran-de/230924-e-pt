# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration



class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1, "Начинаем с числа 1"

    def __iter__(self):
        return self,  "Итератор возвращается"

    def __next__(self):
        if self.current > self.n:  # Когда current превышает n, исключение StopIteration
            raise StopIteration
        else:
            current_value = self.current
            self.current += 1,   "Увеличиваем значение на 1"
            return current_value

"задания итератора"
def create_number_iterator(n):
    return NumberIterator(n)

"Пример использования"
iterator = create_number_iterator(5)

for num in iterator:
   print(num)





# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration




"Генератор квадратов"

#squares_generator = (x**2 for x in range(11))

"next() извлечения и обработку StopIteration"

try:
    while True:
#       square = next(squares_generator)
    print(square)
except StopIteration:
    print("Генератор завершил работу.")





# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration





"Функция-генератор, возвращает слова по одному"
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

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.





def generate_numbers():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i * 2,  "Если число четное, удваиваем его"
        else:
            yield i,  "число нечетное, возвращаем без изменений"


result_set = set(generate_numbers())

"Вывод"
print(result_set)





# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.





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
        yield len(word),   "Возвращаем длину слова"

"строка"

sentence = "Write a generator that returns word lengths from a given sentence"



min_length = min(word_lengths(sentence))
max_length = max(word_lengths(sentence))

# Выводим результаты
print(f"Минимальная длина слова: {min_length}")
print(f"Максимальная длина слова: {max_length}"







# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

x_word = 'this'



def keyword_filter(filename, x_word):


    with open(filename, 'r') as file:

        for line in file:
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





# Генератор, который возвращает длины слов в строке
#    words = sentence.split()  # Разделяем строку на слова
#    for word in words:
#        yield len(word)  # Возвращаем длину каждого слова
#
# # Исходная строка
sentence = "Write a generator that returns word lengths from a given sentence"
#
# # Находим минимальную и максимальную длину с помощью функций min() и max()
min_length = min(word_lengths(sentence))
max_length = max(word_lengths(sentence))
#
# # Выводим результаты
print(f"Минимальная длина слова: {min_length}")
print(f"Максимальная длина слова: {max_length}"







# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt





import re

# Генератор для чтения строк из файла, содержащих числа
def read_lines_with_numbers(filename):
    with open(filename, 'r') as file:
        for line in file:
            if re.search(r'\d', line):  # Проверка, содержит ли строка хотя бы одно число
                yield line.strip()  # Возвращаем строку без символов новой строки

# Пример использования
filename = 'data.txt'

for line in read_lines_with_numbers(filename):
    print(line)