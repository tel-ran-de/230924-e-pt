# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']


# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]


# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]


tuples_1 = [(8, "ultra very high"), (3, "high"), (1, "low"), (4, "medium"), (6, "very high"), (9, "the biggest 1")]
tuples_2 = [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]
tuples_3 = [(8, "ultra very high"), (3, "high"), (1, "low"), (4, "medium"), (6, "very high")]

all_alphabetic = all(all(c.isalpha() or c.isspace() for c in item[1]) for item in tuples_1)
sorted_tuples = sorted(tuples_1, key=lambda item: len(item[1].split()) if all_alphabetic else 0)
print(sorted_tuples)

all_alphabetic = all(all(c.isalpha() or c.isspace() for c in item[1]) for item in tuples_2)
sorted_tuples = sorted(tuples_2, key=lambda item: len(item[1].split()) if all_alphabetic else 0)
print(sorted_tuples)

all_alphabetic = all(all(c.isalpha() or c.isspace() for c in item[1]) for item in tuples_3)
sorted_tuples = sorted(tuples_3, key=lambda item: len(item[1].split()) if all_alphabetic else 0)
print(sorted_tuples)


# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]

countries = [
    {"country": "USA", "capital": "Washington"},
    {"country": "UK", "capital": "London"},
    {"country": "Australia", "capital": "Canberra"}
]
any_long_capital = any(len(item["capital"]) > 6 for item in countries)
if any_long_capital:
    sorted_countries = sorted(countries, key=lambda x: len(x['capital']))
    print(sorted_countries)
else:
    print('Ни одна длина значения capital не больше 6')

# print(sorted(countries, key=lambda x: len(x['capital'])) if any_long_capital else 'Ни одна длина значения capital не больше 6')
