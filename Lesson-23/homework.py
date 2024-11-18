# Тема: Сортировка с использованием sort и sorted

# Задача 1: Сортировка списка чисел по возрастанию и убыванию
# Дан список чисел `[10, 3, 7, 1, 9, 4]`.
# 1. Отсортируйте список по возрастанию с помощью метода `sort`.
# Ожидаемый результат: [1, 3, 4, 7, 9, 10]
# 2. Отсортируйте список по убыванию с помощью функции `sorted`.
# Ожидаемый результат: [10, 9, 7, 4, 3, 1]

# Исходный список
numbers = [10, 3, 7, 1, 9, 4]

# 1. Сортировка по возрастанию с использованием метода sort
numbers.sort()
print("Сортировка по возрастанию (sort):", numbers)  # Ожидаемый результат: [1, 3, 4, 7, 9, 10]

# 2. Сортировка по убыванию с использованием функции sorted
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Сортировка по убыванию (sorted):", sorted_numbers_desc)  # Ожидаемый результат: [10, 9, 7, 4, 3, 1]


# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']

# Исходный список строк
strings = ["house", "cat", "elephant", "car", "building"]

# Сортировка списка по длине строк с использованием функции sorted
sorted_by_length = sorted(strings, key=len)
print("Список, отсортированный по длине:", sorted_by_length)  # Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']

# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Исходный список кортежей
tuples_list = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Сортировка по второму элементу кортежа с использованием метода sort
tuples_list.sort(key=lambda x: x[1])
print("Список, отсортированный по второму элементу:", tuples_list)

# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

# Исходный список словарей
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]

# Сортировка по значению ключа 'age' с использованием функции sorted
sorted_people = sorted(people, key=lambda person: person["age"])
print("Список, отсортированный по возрасту:", sorted_people)
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]

# Исходный список кортежей
tuples_list = [(3, 5), (1, 9), (4, 2), (6, 3)]

# Сортировка по сумме элементов каждого кортежа с использованием метода sort
tuples_list.sort(key=lambda x: sum(x))
print("Список, отсортированный по сумме элементов:", tuples_list)

# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']

# Исходный список
mixed_list = ["tree", 3, "mountain", 1, "river", 2]

# Извлечение только строк из списка
strings_only = [item for item in mixed_list if isinstance(item, str)]

# Сортировка строк по алфавиту
sorted_strings = sorted(strings_only)
print("Список строк, отсортированных по алфавиту:", sorted_strings)

# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]

# Исходный список словарей
books = [
    {"title": "Book A", "price": 15.99},
    {"title": "Book B", "price": "free"},
    {"title": "Book C", "price": 9.99}
]

# Фильтрация словарей, где значение 'price' является числом
valid_books = [book for book in books if isinstance(book["price"], (int, float))]

# Сортировка отфильтрованных словарей по значению ключа 'price'
sorted_books = sorted(valid_books, key=lambda book: book["price"])
print("Список книг, отсортированный по цене:", sorted_books)

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]

# Ошибка в выводе
# Исходный список кортежей
# tuples = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]
#
# # Фильтрация кортежей: проверяем, что второй элемент состоит только из алфавитных символов
# valid_tuples = [
#     t for t in tuples
#     if all(word.isalpha() for word in t[1].split())
# ]
# # Сортировка кортежей по количеству слов во втором элементе
# sorted_tuples = sorted(valid_tuples, key=lambda t: len(t[1].split()))
# print("Список кортежей, отсортированный по количеству слов во втором элементе:", sorted_tuples)

# Верное решение:
# Исходный список кортежей

tuples = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]

# Фильтрация кортежей: проверяем, что второй элемент состоит только из алфавитных символов
valid_tuples = [
    t for t in tuples
    if all(word.isalpha() for word in t[1].split())
]

# Сортировка кортежей сначала по количеству слов во втором элементе, затем по числовому значению первого элемента
sorted_tuples = sorted(valid_tuples, key=lambda t: (len(t[1].split()), t[0]))

# Вывод результата
print("Список кортежей, отсортированный по количеству слов во втором элементе:", sorted_tuples)

# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]

# Исходный список словарей
countries = [
    {"country": "USA", "capital": "Washington"},
    {"country": "UK", "capital": "London"},
    {"country": "Australia", "capital": "Canberra"}
]

# Проверяем хотя бы одно значение ключа 'capital' имеет длину больше 6
if any(len(country["capital"]) > 6 for country in countries):
    # Сортировка словарей по длине значений ключа 'capital'
    sorted_countries = sorted(countries, key=lambda country: len(country["capital"]))
    print("Список стран, отсортированный по длине значений 'capital':", sorted_countries)
else:
    print("Нет ни одного значения 'capital' с длиной больше 6.")

# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']

# Исходный список
items = ["engineering", 2, "artificial", 3.14, "intelligence"]

# Функция для подсчета гласных в строке
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

# Фильтрация строк с проверкой типа
strings_only = [item for item in items if isinstance(item, str)]

# Сортировка строк по количеству гласных
sorted_strings = sorted(strings_only, key=count_vowels)
print("Список строк, отсортированный по количеству гласных:", sorted_strings)

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]

# Исходный список списков
lists = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]

# Фильтрация списков, где все элементы положительные
positive_lists = [lst for lst in lists if all(x > 0 for x in lst)]

# Сортировка отфильтрованных списков по минимальному значению элемента
sorted_lists = sorted(positive_lists, key=min)
print("Список списков, отсортированный по минимальному значению:", sorted_lists)


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
# {'username': 'alice', 'status': 'active', 'status': 'ACTIVE'}
sorted_users = list(map(lambda x: {**x, 'status': x['status'].upper()}, sorted_users))
# {**x, 'status': x['status'].upper()} Создает новый словарь, который является копией исходного словаря x,
# но с измененным значением по ключу 'status'.
# **x: Это синтаксис "распаковки" словаря в новый словарь, что означает копирование всех ключей и значений из x
print(sorted_users)

# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

users = [
    {"username": "alice", "status": "active"},
    {"username": "bob", "status": "inactive"},
    {"username": "charlie", "status": "active"}
]

sorted_users = sorted(users, key=lambda x: x['status'])
# {'username': 'alice', 'status': 'active', 'status': 'ACTIVE'}
sorted_users = list(map(lambda x: {**x, 'status': x['status'].upper()}, sorted_users))
print(sorted_users)


# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]

# Список времени выполнения запросов в миллисекундах
execution_times = [120, 30, 150, 90]

# Список соответствующих URL
urls = ["/home", "/login", "/profile", "/settings"]

# Сортировка времени выполнения запросов по возрастанию
sorted_execution_times = sorted(execution_times)

# Использование zip для объединения отсортированных времен выполнения с URL
combined = list(zip(sorted_execution_times, urls))

print("Объединенные и отсортированные данные:", combined)

# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]

# Исходный список URL
urls = ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]

# Сортировка URL по длине
sorted_urls = sorted(urls, key=len)

# Фильтрация URL, которые содержат подстроку 'example'
filtered_urls = list(filter(lambda url: "example" in url, sorted_urls))

print("Отсортированные и отфильтрованные URL:", filtered_urls)
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']


