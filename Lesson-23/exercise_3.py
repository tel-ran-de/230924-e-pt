# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineer", 2, "artificial", 3.14, "intel"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['intel', 'artificial', 'engineer']
# Исходный список
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
# Исходный список URL
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
#  { "url": "/api/admin", "status": 403 },
#  { "url": "/api/data", "status": 404 }]`.
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
