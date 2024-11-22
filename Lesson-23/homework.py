# Тема: Сортировка с использованием sort и sorted

# Задача 1: Сортировка списка чисел по возрастанию и убыванию
# Дан список чисел `[10, 3, 7, 1, 9, 4]`.
# 1. Отсортируйте список по возрастанию с помощью метода `sort`.
# Ожидаемый результат: [1, 3, 4, 7, 9, 10]
# 2. Отсортируйте список по убыванию с помощью функции `sorted`.
# Ожидаемый результат: [10, 9, 7, 4, 3, 1]
numbers = [10, 3, 7, 1, 9, 4]

numbers.sort()
print(numbers)

de_numbers = sorted(numbers, reverse=True)
print(de_numbers)
print('+==============================+')
# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']

str_list = ["house", "cat", "elephant", "car", "building"]
sorted_list = sorted(str_list, key=len)
print(sorted_list)
print('+==============================+')
# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

data = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_data = data.sort(key=lambda x: x[1])
print(data)
print('+==============================+')
# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
data = [{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)
print('+==============================+')
# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]
tuples_data = [(3, 5), (1, 7), (4, 2), (6, 3)]
tuples_data.sort(key=lambda x: sum(x))
print(tuples_data)
print('+==============================+')
# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']
str_list = ["tree", 3, "mountain", 1, "river", 2]
sorted_list = sorted([x for x in str_list if isinstance(x, str)])
print(sorted_list)
print('+==============================+')
# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]

tuples_data = [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }]
filter_data = [i for i in tuples_data if isinstance(i['price'],(int, float))]
sorted_data = sorted(filter_data, key=lambda x: x['price'])
print(sorted_data)
print('+==============================+')

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]

tuples_data = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]
# filter_data = [i for i in tuples_data if isinstance(i[1],str) and all(word.isalpha() for word in i[1].split())]
# sorted_tuples = sorted(filter_data, key=lambda x: len(x[1].split()))
# print(sorted_tuples)
all_alphabetic = all(all(c.isalpha() or c.isspace() for c in item[1]) for item in tuples_data)
sorted_tuples = sorted(tuples_data, key=lambda item: len(item[1].split()) if all_alphabetic else 0)
print(sorted_tuples)

print('+==============================+')
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
print('+==============================+')
# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']

list_data = ["engineer", 2, "artificial", 3.14, "intel"]
def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s if char in vowels)

strings = [item for item in list_data if isinstance(item, str)]
sorted_strings = sorted(strings, key=count_vowels)
print(sorted_strings)
print('+==============================+')

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]
list_data = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]

filter_data = [i for i in list_data if all(x > 0 for x in i)]
sorted_data = sorted(filter_data, key=lambda x: min(x))

print(sorted_data)
print('+==============================+')
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
tuples_list = [
    {"username": "alice", "status": "active"},
    {"username": "bob", "status": "inactive"},
    {"username": "charlie", "status": "active"}
]
sorted_t_lists = sorted(tuples_list, key=lambda x: x['status'])
status_upper = list(map(lambda x: {**x, 'status': x['status'].upper()}, sorted_t_lists))
print(status_upper)
print('+==============================+')
# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

urls_data = ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]
sorted_data = sorted(urls_data, key=len)
filter_data = list(filter(lambda x: "example" in x, sorted_data))
print(filter_data)

print('+==============================+')

# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]

time_list = [120, 30, 150, 90]
urls_data = ["/home", "/login", "/profile", "/settings"]

sorted_time_list = sorted(time_list)
sorted_time_urls = list(zip(sorted_time_list, urls_data))
print(sorted_time_urls)

print('+==============================+')
# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]

api_list = [{ "url": "/api/user", "status": 200 },
            { "url": "/api/admin", "status": 403 },
            { "url": "/api/data", "status": 404 }]

sorted_api_list = sorted(api_list, key=lambda x: x["status"])

api_data = list(map(lambda x: (x[0], x[1]['url'], x[1]['status']), enumerate(sorted_api_list)))

print(api_data)