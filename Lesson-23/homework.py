# Тема: Сортировка с использованием sort и sorted

# Задача 1: Сортировка списка чисел по возрастанию и убыванию
# Дан список чисел `[10, 3, 7, 1, 9, 4]`.
# 1. Отсортируйте список по возрастанию с помощью метода `sort`.
# Ожидаемый результат: [1, 3, 4, 7, 9, 10]
# 2. Отсортируйте список по убыванию с помощью функции `sorted`.
# Ожидаемый результат: [10, 9, 7, 4, 3, 1]
numbers = [10, 3, 7, 1, 9, 4]
numbers.sort()
print("По возрастанию:", numbers)

sorted_numbers = sorted(numbers, key=lambda x: -x)
print("По убыванию:",sorted_numbers)

# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']

words = ["house", "cat", "elephant", "car", "building"]
sorted_words = sorted(words, key=len)
print(sorted_words)

# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

list_word = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
list_word.sort(key=lambda x: x[1])
print(list_word)

# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)

# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]
elements = [(3, 5), (1, 9), (4, 2), (6, 3)]
elements.sort(key=lambda x: sum(x))
print(elements)

# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']

items = ["tree", 3, "mountain", 1, "river", 2]
strings = list(filter(lambda x: isinstance(x, str), items))
sorted_strings = sorted(strings, key=lambda x: x)
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
    { "country": "USA", "capital": "Washington" },
    { "country": "UK", "capital": "London" },
    { "country": "Australia", "capital": "Canberra" }
]
if any(len(i['capital']) > 6 for i in countries):
    sorted_countries = sorted(countries, key=lambda x: len(x['capital']))
    print(sorted_countries)
else:
    print("Условие не выполнено.")

# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineer", 2, "artificial", 3.14, "intel"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']
data = ["engineer", 2, "artificial", 3.14, "intel"]

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word if char in vowels)

filtered_strings = [item for item in data if isinstance(item, str)]
sorted_strings = sorted(filtered_strings, key=lambda x: count_vowels(x))
print(sorted_strings)

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]

lists = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]
sorted_lists = sorted([lst for lst in lists if all(x > 0 for x in lst)], key=lambda x: min(x))
print(sorted_lists)

# Задача 3: Сортировка списка словарей по статусу пользователя и преобразование с помощью map
# **Задание:**
# Дан список словарей, представляющих пользователей веб-приложения
# [{ "username": "alice", "status": "active" }, { "username": "bob", "status": "inactive" },
#  { "username": "charlie", "status": "active" }]`.
# Отсортируйте пользователей по статусу, а затем используйте функцию `map`,
# чтобы преобразовать статусы в верхний регистр.
# Ожидаемый результат:
# [{'username': 'alice', 'status': 'ACTIVE'},
# {'username': 'charlie', 'status': 'ACTIVE'},
# {'username': 'bob', 'status': 'INACTIVE'}]
users = [
    {"username": "alice", "status": "active"},
    {"username": "bob", "status": "inactive"},
    {"username": "charlie", "status": "active"}
]
sorted_users = sorted(users, key=lambda x: x['status'])
sorted_users = list(map(lambda x: {**x, 'status': x['status'].upper()}, sorted_users))
print(sorted_users)

# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']
urls = [
    "https://example.com",
    "https://longexample.com/page",
    "http://short.io",
    "https://medium.com/article"
]
sorted_urls = sorted(urls, key=len)
filtered_urls = list(filter(lambda url: "example" in url, sorted_urls))
print(filtered_urls)

# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]

times = [120, 30, 150, 90]
urls = ["/home", "/login", "/profile", "/settings"]
sorted_times = sorted(times)
sorted_requests = list(zip(sorted_times, urls))
print(sorted_requests)

# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]
api_urls = [
    { "url": "/api/user", "status": 200 },
    { "url": "/api/admin", "status": 403 },
    { "url": "/api/data", "status": 404 }
]

sorted_responses = sorted(api_urls, key=lambda x: x['status'])
indexed_responses = zip(range(len(sorted_responses)), sorted_responses)
final_result = list(map(lambda x: (x[0], x[1]['url'], x[1]['status']), indexed_responses))
print(final_result)

