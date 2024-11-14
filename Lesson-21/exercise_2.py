# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def wort_generator():
    for num in range(1, 11):
        if num % 2 == 0:
            yield num * 2
        else:
            yield  num
result_set = set(wort_generator())
print(result_set)


# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.

def wort_generator():
    for num in range(1, 21):
        if num % 3 == 0:
            yield num

result_set = sum(wort_generator())
print(result_set)
# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
def words_generator(sentence):
    for word in sentence.split():
        yield len(word)
sentence = "Write a generator that returns word lengths from a given sentence"
lengs = words_generator(sentence)
word_max = max(lengs)
word_min = min(words_generator(sentence))

print(word_min)
print(word_max)