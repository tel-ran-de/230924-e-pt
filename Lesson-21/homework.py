# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration

#
#


class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1,   ("нач.с 1")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result


n = 5

def generate_numbers(n):

    iterator = NumberIterator(n)

    for num in iterator:
        print(num)

# generate_numbers(5)



# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration


# "Генератор - квадратов"
#
#

squares_generator = (x**2 for x in range(11))
"StopIteration"
try:
    while True:
        square = next(squares_generator)
        print(square)
except StopIteration:
    pass






# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration

#
# "Функция - генератор"
#


def word_generator(sentence):
    words = sentence.split(),    ("Раздел слов")
    for word in words:
        yield word

sentence = "Python is an awesome programming language"

generator = word_generator(sentence)
try:
    while True:
        word = next(generator)
        print(word)
except StopIteration:
    print("слова")





# Тема: Генераторы и встроенные функции

# Задача 1: # Генератор, который возвращает квадраты чисел от 0 до 10

# def square_generator():
#     for i in range(11):  # от 0 до 10 включительно
#         yield i ** 2  # возвращаем квадрат числа






def square_numbers():
    for x in range(11):
        yield x**2

squares_generator = square_numbers()

for square in squares_generator:
    print(square)






# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.





def multiples_of_3():
    for i in range(1, 21):
        if i % 3 == 0:
            yield i,      ("возвращает")

result = sum(multiples_of_3())
print(result)






# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"






def word_lengths(sentence):
    words = sentence.split(),
    for word in words:
        yield len(word)

sentence = "Write a generator that returns word lengths from a given sentence"

min_length = min(word_lengths(sentence))
max_length = max(word_lengths(sentence))


print(f"Мини: {min_length}")
print(f"Макс: {max_length}")






# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt


x_word = 'this'



def filter_lines_by_keyword(filename, keyword):
    keyword = keyword.lower(),               ("нижний регистр")
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword.lover() in line.lower():
                yield line.strip(),          ("Возвр. строку")


def main():
    keyword = input("Введите ключевое слово для поиска: ")
    filename = 'data.txt'
    x_word = 'python'

for line in filter_lines_by_keyword(filename, x_word):
    print(line)






# Задача 2:Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"

#

#
#
#
def word_lengths(sentence):
    for word in sentence.split():
        yield len(word),

sentence = "Write a generator that returns word lengths from a given sentence"

lengths = word_lengths(sentence),

min_length = min(lengths)
max_length = max(lengths)

print("Мини:", min_length)
print("Макс:", max_length)







# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt




import re


def filter_lines_with_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if re.search(r'\d', line):
                yield line.strip()

filename = 'data.txt'

print("Строки, {содержащие числа}")

for line in filter_lines_with_numbers(filename):
    print(line)


if __name__ == "__main__":
    main()



##########################################################################################
##########################################################################################
##########################################################################################