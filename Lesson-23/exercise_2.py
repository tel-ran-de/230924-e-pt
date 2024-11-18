# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']

items = ["tree", 3, "mountain", 1, "river", 2]
# strings = list(filter(lambda x: isinstance(x, str), items))
sorted_strings = sorted(list(filter(lambda x: isinstance(x, str), items)), key=lambda x: x)
print(sorted_strings)

# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]
books = [
    {"title": "Book A", "price": 15.99},
    {"title": "Book B", "price": "free"},
    {"title": "Book C", "price": 9.99}
]
filtered_books = [book for book in books if isinstance(book["price"], (int, float))]
sorted_books = sorted(filtered_books, key=lambda x: x["price"])
print(sorted_books)

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]

tuples = [(8, "ultra very high"), (3, "high"), (1, "low"), (4, "medium"), (6, "very high"), (9, "the biggest 1")]
tuples_2 = [(8, "ultra very high"), (3, "high"), (1, "low"), (4, "medium"), (6, "very high")]

all_tuples = all(all(word.isalpha() or word.isspace() for word in t[1]) for t in tuples)
sorted_tuples = sorted(tuples, key=lambda x: len(x[1].split()) if all_tuples else 0)
print(sorted_tuples)

all_tuples_2 = all(all(word.isalpha() or word.isspace() for word in t[1]) for t in tuples_2)
sorted_tuples = sorted(tuples, key=lambda x: len(x[1].split()) if all_tuples else 0)
print(sorted_tuples)

# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]

countries = [
    { "country": "USA", "capital": "Washington" },
    { "country": "UK", "capital": "London" },
    { "country": "Australia", "capital": "Canberra" }
]
# if any(len(i['capital']) > 6 for i in countries):
#     sorted_countries = sorted(countries, key=lambda x: len(x['capital']))
#     print(sorted_countries)
# else:
#     print("Условие не выполнено.")
any_long_countres = any(len(i['capital']) > 6 for i in countries)
if any_long_countres:
    sorted_countries = sorted(countries, key=lambda x: len(x['capital']))
    print(sorted_countries)
else:
    print("Условие не выполнено.")