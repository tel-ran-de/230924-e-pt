# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
def iteration():
	try:
		while True:
			print(next(iter_numbs))
	except StopIteration:
		print("finish")
numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iter_numbs = iter(numbs)

iteration()

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
gen = (x ** 2 for x in range (11))

try:
	while True:
		print(next(gen))
except StopIteration:
	print("finish")

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
def satz_gen(exemple):
	words = exemple.split()
	for word in words:
		yield word

exemple = "На душе у него было гнусно, как никогда."
gen = satz_gen(exemple)

try:
	while True:
		print(next(gen))
except StopIteration:
	print("Конец")

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def gen_func():
	for x in range(11):
		if x % 2 == 0:
			yield x * 2
		else:
			yield x
a = gen_func()
print(set(list(a)))


# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
def gen_sum():
	for x in range(21):
		if x % 3 == 0:
			yield x
i = gen_sum()
print(sum(i))

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
def gen_string():
	x = sentence.split()
	for word in x:
		yield len(word)
sentence = "Write a generator that returns word lengths from a given sentence"
w = gen_string()
z = list(w)

print(min(z))
print(max(z))

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
x_word = 'this'
def gen_filter(file_path = "text_files/data.txt", f = x_word):
	with open (file_path) as file:
		for line in file.readlines():
			if f in line.lower():
				yield line
gen = gen_filter()
for line in gen:
	print(list(gen))

# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt


# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
