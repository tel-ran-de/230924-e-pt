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
print()

numbers = [10, 3, 7, 1, 9, 4]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)




# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']




my_list = ["house", "cat", "elephant", "car", "building"]
sorted_list = sorted(my_list, key=len)
print(my_list)





# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]




numbers_value = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
numbers_value.sort(key=lambda x:x[1])
print(numbers_value)




# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]





people = [{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]
people_sorted = sorted(people, key=lambda person: person['age'])
print(people_sorted)





# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]





numbers_value = [(3, 5), (1, 7), (4, 2), (6, 3)]
numbers_value.sort(key=lambda x:sum(x))
print(numbers_value)





# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']





items = ["tree", 3, "mountain", 1, "river", 2]
sorted_strings = sorted(filter(lambda x: isinstance(x, str), items))
print(sorted_strings)





# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}





books = [{ "title": "Book A", "price": 15.99 },{ "title": "Book B", "price": "free" },{ "title": "Book C", "price": 9.99 }]

filtered_books = filter(lambda book: isinstance(book['price'], (int, float)), books)
sorted_books = sorted(filtered_books, key=lambda book: book['price'])
print(sorted_books)





# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]





tuples = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]


filtered_tuples = filter(lambda x: all(word.isalpha() for word in x[1].split()), tuples)
sorted_tuples = sorted(filtered_tuples, key=lambda x: len(x[1].split()))
print(sorted_tuples)






# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]




countries = [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
 { "country": "Australia", "capital": "Canberra" }]

if any(len(country['capital']) > 6 for country in countries):
    sorted_countries = sorted(countries, key=lambda x: len(x['capital']))
    print(sorted_countries)
else:
    print("Нет стран больше 6")




# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']





items = ["engineering", 2, "artificial", 3.14, "intelligence"]
filtered_strings = filter(lambda x: isinstance(x, str), items)

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for letter in word if letter in vowels)
sorted_strings = sorted(filtered_strings, key=lambda x: count_vowels(x))

print(sorted_strings)







# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]





lists = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]
filtered_lists = filter(lambda lst: all(x > 0 for x in lst), lists)
sorted_lists = sorted(filtered_lists, key=lambda lst: min(lst))

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
    { "username": "alice", "status": "active" },
    { "username": "bob", "status": "inactive" },
    { "username": "charlie", "status": "active" }
]
sorted_users = sorted(users, key=lambda user: user['status'])
updated_users = list(map(lambda user: {**user, 'status': user['status'].upper()}, sorted_users)),

print(updated_users)





# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']






urls = ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"],
sorted_urls = sorted(urls, key=len)
filtered_urls = filter(lambda url: "example" in url, sorted_urls)
result = list(filtered_urls)

print(result)





# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]





execution_times = [120, 30, 150, 90]
urls = ["/home", "/login", "/profile", "/settings"]

sorted_times_with_urls = sorted(zip(execution_times, urls))
result = list(sorted_times_with_urls)
print(result)





# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]




sorted_responses = sorted('api_responses', key=lambda response: response['status'])
numbered_responses = zip(range(len(sorted_responses)), sorted_responses)
result = list(map(lambda item: (item[0], item[1]['url'], item[1]['status']), numbered_responses))

print(result)



###########################################################################################################