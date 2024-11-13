# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def num_gen():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i * 2
        else:
            yield i
result = set(num_gen())
print("Множество чисел: ", result)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
def gen_num3():
    for i in range(1, 21):
        if i % 3 == 0:
            yield i
result_sum = sum(gen_num3())
print("Сумма чисел, кратные 3: ", result_sum)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"

def word_gen(sentence):
    words = sentence.split()
    for word in words:
        yield len(word)
sentence = "Write a generator that returns word lengths from a given sentence"
word_len = list(word_gen(sentence))
min_len = min(word_len)
max_len = max(word_len)
print(min_len)
print(max_len)