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
numbers = [10, 3, 7, 1, 9, 4]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']

test_list = ["house", "cat", "elephant", "car", "building"]
print(sorted(test_list, key=len))

# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

test_list = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
test_list.sort(key=lambda x: x[1])
print(test_list)

# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

test_list = [{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]
result = sorted(test_list, key=lambda x: x['age'])
print(result)

# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]

test_list = [(3, 5), (1, 7), (4, 2), (6, 3)]
result = sorted(test_list, key=lambda x: x[0]+x[1])
print(result)

# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']

test_list = ["tree", 3, "mountain", 1, "river", 2]
strings_list = list(filter(lambda x: isinstance(x, str), test_list))
temp_result = list(map(lambda x: x.lower(), strings_list))
result = sorted(temp_result)
print(result)

# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]

test_list = [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" },
             { "title": "Book C", "price": 9.99 }]
temp_list = list(filter(lambda x: isinstance(x['price'], float), test_list))
result = sorted(temp_list, key=lambda x: x['price'])
print(result)

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]

test_list = [(5, 'here are four words'), (7, 'here is 1'), (3, "high"), (1, "low"), (4, "medium"), (6, "very high")]
temp_list = list(filter(lambda x: all(char.isalpha() or char.isspace() for char in x[1]), test_list))
result = sorted(temp_list, key=lambda x:len(x[1].split()))
print(result)

# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]

test_list = [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
             { "country": "Australia", "capital": "Canberra" }]
result = sorted(test_list, key=lambda x: len(x['capital'])) if any([len(x['capital']) > 6 for x in test_list]) \
         else test_list
print(result)

# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']

test_list = ["engineer", 2, "artificial", 3.14, "intell"]
temp_check_list = list(filter(lambda x: isinstance(x, str), test_list))
result = sorted(temp_check_list, key=lambda x: len(x))
print(result)

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]

test_list = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5], [1, 2, 3]]
temp_check_list = list(filter(lambda x: all(item > 0 for item in x), test_list))
#print(temp_check_list)
result = sorted(temp_check_list, key=lambda x: min(x))
print(result)

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

test_list = [{ "username": "alice", "status": "active" }, { "username": "bob", "status": "inactive" },
             { "username": "charlie", "status": "active" }]
sorted_list = sorted(test_list, key=lambda x: x['status'])
result = list(map(lambda x: x|{'status': x['status'].upper()}, sorted_list))
print(result)


# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

test_list = ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]
sorted_test_list = sorted(test_list, key=len)
filtered_test_list = list(filter(lambda x: "example" in x, sorted_test_list))
print(filtered_test_list)

# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]

exec_time_list = [120, 30, 150, 90]
urls = ["/home", "/login", "/profile", "/settings"]
sorted_list = sorted(exec_time_list)
result = list(zip(sorted_list, urls))
print(result)

# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]

test_list = [{ "url": "/api/user", "status": 200 },
             { "url": "/api/admin", "status": 403 },
             { "url": "/api/data", "status": 404 }]
sorted_list = sorted(test_list, key=lambda x: x['status'])
temp_list = list(zip(range(len(sorted_list)), sorted_list))
result = list(map(lambda x: (x[0], *(x[1].values())), temp_list))
print(result)